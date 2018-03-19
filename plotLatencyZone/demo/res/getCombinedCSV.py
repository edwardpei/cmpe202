import re
import csv
import sys

newFileName = 'CSVres'

for j in range(0,105,5):
	filename = 'TimeFor' + str(j) +'.csv'
	pattern  = '\s*(.*?)\s*seconds'                   
	new_file = []

	with open(filename, 'r') as f:
	   # Read the file contents and generate a list with each line
	   lines = f.readlines()

	# Iterate each line
	for line in lines:

	    # Regex applied to each line 
	    match = re.search(pattern, line)
	    if match:
		# Make sure to add \n to display correctly when we write it back
		new_line = match.group(1)
#		print new_line
		new_file.append(new_line)


	with open(newFileName, 'a') as f:
	     # go to start of file
	     # actually write the lines
                f.write(str(j) + " ")	     
	     	f.write(new_file[0] + '\n')




txt_file = r"CSVres"
csv_file = r"myLatencyCSV.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = ' ')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)
