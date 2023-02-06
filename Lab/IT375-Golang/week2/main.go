package main

import (
	math "chirapon/week2/week2sat"
	"fmt"
)

func main() {
	xs := []float64{1, 2, 3, 4}
	avg := math.Average(xs)
	fmt.Println("Average : ", avg)
	x := 12
	y := 8
	fmt.Printf("%v + %v = %v \n", x, y, math.Sum(x, y))
	fmt.Printf("%v - %v = %v \n", x, y, math.Minus(x, y))
}
