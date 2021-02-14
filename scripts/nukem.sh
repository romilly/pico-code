#! /bin/bash
export AMPY_PORT=/dev/ttyACM0
ampy ls | while read line ; do echo $line ; ampy rm $line ; done