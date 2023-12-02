#!/bin/bash

# Piping is basically sending the output of first command into second command.
ls | wc -l # counts how many files are there in this director

# ls output all the file names as a string, and wc -l counts how many lines are there in input.

ls | grep sh # This command searches for all the files that contain sh()