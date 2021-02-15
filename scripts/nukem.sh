#! /bin/bash
export AMPY_PORT=/dev/ttyACM0
echo "This will delete *all* files from your pico."
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    ampy ls | while read line ;
        do
        echo $line ; ampy rm $line ;
        done
fi