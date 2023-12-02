#!/bin/bash

echo "What is your full name?"
read NAME

if [ "$NAME" == "Danjie Tang" ]; then
	echo "Hello boss"
elif [ "$NAME" == "abc" ]; then
	echo "Welcome, you have entered the secret key"
else
	echo "Wrong user"
fi
