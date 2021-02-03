#!/bin/bash

file="$1"
bytec=$(wc -c $1) 
wordc=$(wc -w $1) 

echo "Words: $wordc"
echo "Bytes: $bytec"