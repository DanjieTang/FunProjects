#!/bin/zsh
# The first line needs to be shebang line. 
# This is actually for zsh(mac terminal), if you want to use bash(linux terminal) use #!/bin/bash

# This is print
echo "Hello world" # It is a good convention to use "" to denote string

# This is a variable, global variables have all capital + _ naming convention.
FIRST_NAME="Danjie" 
LAST_Name="Tang" # Wh
echo "Hello" $FIRST_NAME $LAST_Name # Each command will take a line. First "word" is the command