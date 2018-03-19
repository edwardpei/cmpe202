#!/bin/bash
./generateAllTestRes.sh
python toCSV.py 
pyhton genAllPlot.py 

exit 0

