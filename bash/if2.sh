#!/bin/bash

echo "Please enter how old are you"
read AGE

if [ $AGE -ge 65 ] ; then
	echo "You are too old to drink alcohol"
elif [ $AGE -ge 19 ] ; then
	echo "You are legally allowed to buy alcohol"
elif [ $AGE -eq 18 ] ; then
	echo "You can't buy alcohol yet, but you will be able to next year"
else
	echo "WTF you want to buy alcohol?"
fi
