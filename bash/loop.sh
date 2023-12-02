#!/bin/bash

ARRAY=(1 2 3 4 5 6 7 8 9 10)

# For loop looks pretty similar to python for loop
for NUMBER in ${ARRAY[@]}
do
    echo $NUMBER
done

# You can also do something like for i in range(10) in bash
for NUMBER in $(seq 0 9) # It is inclusive on both ends
do
    echo $NUMBER
done

NUMBER=10

# While loop
while [ $NUMBER -gt 0 ]
do
    NUMBER=$((NUMBER - 1)) #(()) Does mathematical operation
    echo $NUMBER
done