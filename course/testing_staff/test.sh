#!/bin/sh

START_TIME=$(date +%N)
./prog `cat input.txt` > output.txt
END_TIME=$(date +%N)
echo $(($END_TIME - $START_TIME))

