#!/bin/bash

ARRAY=(1 2 3 hello world)

# Use {} to surround the array to print element in the list
# Use [] to decide which element to print and use @ if you want to print all elements.
echo ${ARRAY[4]}