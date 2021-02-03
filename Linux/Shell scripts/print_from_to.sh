#!/bin/bash

echo "Enter the first number: "
read num1

echo "Enter the second number:"
read num2

for i in {$num1..$num2}; do
    printf "$i " 
done

printf "\n"

