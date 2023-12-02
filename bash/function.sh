#!/bin/bash

# Function can't have name same as any built-in commands. It will overwrite the built-in command.
my_fun(){
    echo "Hello world"
}

my_fun

# You can also use positional arguments for functions
greetings(){
    echo "Hello $1" # This is positional argument from the function calling. This is how to pass in parameters to function.
    #They are different from positional arguments from executing the file.
    local a=100 # Use local variables with command local
}

greetings Danjie