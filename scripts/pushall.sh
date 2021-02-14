#! /bin/bash
export AMPY_PORT=/dev/ttyACM0
cd $1
for file in *.py
do
     echo $file
     ampy put "$file" 
done

