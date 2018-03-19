import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv


x = []
y = []

with open('myLatencyCSV.csv','r') as csvfile:	
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(float(row[0]))
		y.append(float(row[1]))
	fig = plt.figure()
	plt.plot(x,y)
	plt.xlabel('input size')
	plt.ylabel('finishing time')
	plt.title("Latency")
	plt.legend()
	fig.savefig('latency.png', dpi=fig.dpi)
	

