package main

import "fmt"

func main(){
	var array[5] int

	for i := 0; i < len(array); i++{
		array[i] = i
	}

	square(&array)

	fmt.Println((array))
}

func square(array*[5] int){
	for i := 0; i < len(array); i++{
		array[i] = array[i] * 100
	}
}