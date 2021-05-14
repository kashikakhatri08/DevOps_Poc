#! /bin/bash

string1="hello"
echo $"hey:"$string1

 my_function(){
 
local abc=${string1}
if [ "$string1" = "hello" ]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
 
}
my_function
