#!/bin/bash

for i in 1 2 4 8
do
	for j in 1 2 4 8
	do
	echo "perf stat -d ./demo/demo_toy_problem.py $i $j" > ./testScript$i$j.sh
	chmod 755 ./testScript$i$j.sh
        sudo /home/edwardpei/Downloads/pmu-tools-master/toplev.py -l3 -I 1000 -x, -o plot/no$i$j.csv ./testScript$i$j.sh
	sudo /home/edwardpei/Downloads/pmu-tools-master/tl-barplot.py --cpu C0-T0 plot/no$i$j.csv -o visualOutput/graph$i$j.png
	done
done
exit 0
