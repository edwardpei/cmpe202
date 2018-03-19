#!/bin/bash
for i in 1 2 4 8
do
	for j in 1 2 4 8
	do
	perf stat -d -o ./perfRes$i$j ./demo/demo_toy_problem.py $i $j
	done
done
exit 0

