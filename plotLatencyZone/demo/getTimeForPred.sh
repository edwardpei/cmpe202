#!/bin/bash
mkdir ./testScripts

	for j in 1 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
	do
	perf stat -d -o ./res/TimeFor$j.csv ./latencyTest.py $j
	done

exit 0
