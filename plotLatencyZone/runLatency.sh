#!/bin/bash

./demo/getTimeForPred.sh
cd ./demo/res/
mv TimeFor1.csv TimeFor0.csv 
python getCombinedCSV.py
python getFinalPLot.py
exit 0
