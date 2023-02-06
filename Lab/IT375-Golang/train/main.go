package main

import "fmt"

type name struct {
	FName string
	LName string
	age   string
	tel   []string
}

var s = []name{
	{
		FName: "chiorapon",
		LName: "hemtrakan",
		age:   "25",
		tel: []string{
			"0815476439",
			"0931120081",
		},
	},
	{
		FName: "bell",
		LName: "kub",
		age:   "21",
		tel:   nil,
	},
}


func main() {
	var data1 []name
	for _, m1 := range s {
		tel := []string{}
		var telArr string
		for _, m2 := range m1.tel {
			telArr = m2
			tel = append(tel, telArr)
		}

		name1 := name{
			FName: m1.FName,
			LName: m1.LName,
			age:   m1.age,
			tel:   tel,
		}
		data1 = append(data1, name1)
	}

	for i := 2; i <= 12; i++ {
		for j := 1; j <= 12; j++ {
			x := i * j
			fmt.Printf("%v x %v = %v \n", i, j, x)
		}
		fmt.Println("<--------------------->")
	}

	fmt.Println("Data : ", data1)
}
