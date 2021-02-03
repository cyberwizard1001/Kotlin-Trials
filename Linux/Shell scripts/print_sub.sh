#!/bin/bash

echo Please enter folder name:

read folder

find "$folder" -type d -empty | cat > file.txt


