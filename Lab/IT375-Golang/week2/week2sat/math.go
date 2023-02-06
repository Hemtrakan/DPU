package math

// Average use for find the average number in the array
func Average(xs []float64) float64{
	total := float64(0)
	for _,x := range xs{
		total += x
	}
	return total / float64(len(xs))
}

func Sum(x, y int) (total int){
	total = x + y
	return total
}

func Minus(x, y int) (total int){
	total = x - y
	return total
}