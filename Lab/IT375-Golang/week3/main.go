package main

import (
	"encoding/json"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"strconv"
	"time"
)

type Name struct {
	StudentID string    `json:"student_id,omitempty"`
	FName     string    `json:"f_name,omitempty"`
	LName     string    `json:"l_name,omitempty"`
	CreatedOn time.Time `json:"created_on"`
	//รหัสนักศึกษา ชื่อ นามสกุล เวลา
}

//Store for the Notes collection
var noteStore = make(map[string]Name)

//Variable to generate key for the collection
var id int = 0

func GetNoteHandler(w http.ResponseWriter, r *http.Request) {
	var notes []Name
	for _, v := range noteStore {
		notes = append(notes, v)
	}
	w.Header().Set("Content-Type", "application/json")
	j, err := json.Marshal(notes)
	if err != nil {
		panic(err)
	}
	w.WriteHeader(http.StatusOK)
	w.Write(j)
}

func PostNoteHandler(w http.ResponseWriter, r *http.Request) {
	var notes Name
	//Decode the incoming Note json
	err := json.NewDecoder(r.Body).Decode(&notes)
	if err != nil {
		panic(err)
	}
	notes.CreatedOn = time.Now()
	id++
	k := strconv.Itoa(id)
	noteStore[k] = notes
	j, err := json.Marshal(notes)
	if err != nil {
		panic(err)
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	w.Write(j)
}

func PutNoteHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	k := vars["id"]
	var noteToUpd Name
	//Decode the incoming Note json
	err := json.NewDecoder(r.Body).Decode(&noteToUpd)
	if err != nil {
		panic(err)
	}
	if note, ok := noteStore[k]; ok {
		noteToUpd.CreatedOn = note.CreatedOn
		//delete existing item and add the update item
		delete(noteStore, k)
		noteStore[k] = noteToUpd
	} else {
		log.Printf("Couldn’tfindkeyofNote %s to", k)
	}
	w.WriteHeader(http.StatusNoContent)
}

func DeleteNoteHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	k := vars["id"]
	//Remove from store
	if _, ok := noteStore[k]; ok {
		//delete existing item
		delete(noteStore, k)
	} else {
		log.Printf("Couldn’t find key of note %s to delete", k)
	}
	w.WriteHeader(http.StatusNoContent)
}

func main() {
	r := mux.NewRouter().StrictSlash(false)
	r.HandleFunc("/api/notes", GetNoteHandler).Methods("GET")
	r.HandleFunc("/api/notes", PostNoteHandler).Methods("POST")
	r.HandleFunc("/api/notes/{id}", PutNoteHandler).Methods("PUT")
	r.HandleFunc("/api/notes/{id}", DeleteNoteHandler).Methods("DELETE")
	server := &http.Server{
		Addr:    ":8080",
		Handler: r,
	}
	log.Println("Listening...")
	server.ListenAndServe()
}
