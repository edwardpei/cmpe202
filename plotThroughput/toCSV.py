import re
import csv
import sys


newFileName = 'res'
##open(newFileName, 'w').write("thread scale cycle inst branch branchMisses\n")              no need for this if using pyplot

for i in [1,2,4,8]:
   for j in [1,2,4,8]:
	filename = 'perfRes' + str(i) + str(j) 
	pattern  = '\s*(.*?)\s*(instructions|cycles|branches|branch-misses|L1-dcache-loads|L1-dcache-load-misses|LLC-loads|LLC-load-misses)'                   
	new_file = []

###    #    1.56  insn per cycle
	#  \n|\s(.*?)\sinstructions\\n|\s(.*?)\sbranches\s/#|\s(.*?)\sbranch-misses\s/#
	# Make sure file gets closed after being iterated
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

	paraNoComma = []
	for num in new_file:
		paraNoComma.append(num.replace(",",""))
	print paraNoComma

	with open(newFileName, 'a') as f:
	     # go to start of file
	     # actually write the lines	     
	     	f.write(str(i) + " " + str(j) + " " + paraNoComma[0] + " ")
	     	f.write(paraNoComma[1] + " ")
	     	f.write(paraNoComma[2] + " ")
	     	f.write(paraNoComma[3] + " ")
	     	f.write(paraNoComma[4] + " ")
	     	f.write(paraNoComma[5] + " ")
	     	f.write(paraNoComma[6] + " ")
	     	f.write(paraNoComma[7] + "\n")



txt_file = r"res"
csv_file = r"mycsv.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = ' ')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)
