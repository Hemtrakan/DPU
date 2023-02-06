package main

import (
	"fmt"
	"math"
	"strings"
)

type Rectangle struct {
	x1, y1, x2, y2 float64
}

func distance(x1, y1, x2, y2 float64) float64 {
	a := x2 - x1
	b := y2 - y1
	return math.Sqrt(a*a + b*b)
}

func (r *Rectangle) area() float64 {
	l := distance(r.x1, r.y1, r.x1, r.y2)

	w := distance(r.x1, r.y1, r.x2, r.y1)

	return l * w
}
func main() {
	r := Rectangle{
		0,
		0, 10, 10,
	}
	fmt.Println(r.area())

	fmt.Println(strings.Index("123","4"))
	fmt.Println(strings.Join([]string{"bell","kub"},"_"))
	fmt.Println(strings.Repeat("a",5))
	fmt.Println(strings.Replace("aaaa","a","b",1))
	fmt.Println(strings.Split("a-b-d-e-q-we","-"))
	test := "TEST"
	fmt.Println(strings.ToLower(test))
	test = "test"
	fmt.Println(strings.ToUpper(test))
	arr := []byte("test")
	str := string(arr)
	fmt.Println(str)
}


//func main(){
//	Name := "Chirapon Hemtrakan"
//	name := strcon.SwapCase(Name)
//	fmt.Println("Name : ",name)
//}
