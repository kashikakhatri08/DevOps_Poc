 #! /bin/bash
 
fun(){

echo "recieved parameter in script1 from jenkins job : $1"
. ScriptTest2.sh $1

}

fun $1
