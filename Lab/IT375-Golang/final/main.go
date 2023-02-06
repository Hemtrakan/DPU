package main

import (
	"fmt"
)

func lenCalculate(str string) int {
	return len(str)
}

func calSum(num int) int {
	return num + 13
}

func calMinus(num int) int {
	return num - 3
}

func main() {
	NameArr := []string{"Apollo", "Athena", "Artemis", "Zeus", "Aphrodite"}
	for _, Name := range NameArr {
		lenName := lenCalculate(Name)
		if lenName == 7 {
			fmt.Printf("Length of %v is %v \n", Name, lenName)
			fmt.Printf("Calculate is %v \n", lenName)
		}
		if lenName > 7 {
			fmt.Printf("Length of %v is %v \n", Name, lenName)
			fmt.Printf("Calculate is %v \n", calSum(lenName))
		}
		if lenName < 7 {
			fmt.Printf("Length of %v is %v \n", Name, lenName)
			fmt.Printf("Calculate is %v \n", calMinus(lenName))
		}
	}
}
