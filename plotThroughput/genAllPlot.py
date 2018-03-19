import matplotlib.pyplot as plt
import csv

x = [8,4,2,1]
y11 = []
y12 = []
y13 = []
y14 = []

y21 = []
y22 = []
y23 = []
y24 = []

y31 = []
y32 = []
y33 = []
y34 = []

with open('mycsv.csv','r') as csvfile:

    plots = csv.reader(csvfile, delimiter=',')
    plots = list(plots)
    for i in range(0, len(plots)):
	    if(i < 4):
            	y11.append( float(plots[i][5]) / float(plots[i][4]) )
           	y21.append( float(plots[i][7]) / float(plots[i][6]) )
            	y31.append( float(plots[i][3]) / float(plots[i][2]) )

	    elif(i < 8):
            	y12.append( float(plots[i][5]) / float(plots[i][4]) )
           	y22.append( float(plots[i][7]) / float(plots[i][6]) )
            	y32.append( float(plots[i][3]) / float(plots[i][2]) )
	    elif(i < 12):
            	y13.append( float(plots[i][5]) / float(plots[i][4]) )
           	y23.append( float(plots[i][7]) / float(plots[i][6]) )
            	y33.append( float(plots[i][3]) / float(plots[i][2]) )
	    else: 
            	y14.append( float(plots[i][5]) / float(plots[i][4]) )
           	y24.append( float(plots[i][7]) / float(plots[i][6]) )
            	y34.append( float(plots[i][3]) / float(plots[i][2]) )

    fig = plt.figure()
    plt.plot(x, y11, label='singleThread')
    plt.plot(x, y12, label='twoThread')
    plt.plot(x, y13, label='fourThread')
    plt.plot(x, y14, label='EightThread')

    plt.xlabel('scale of insts')
    plt.ylabel('bMPKI')
    plt.title("compositive branch MPKI graph")
    plt.legend()
    fig.savefig('branchMPKI.png', dpi=fig.dpi)

    fig = plt.figure()
    plt.plot(x, y21, label='eightThread')
    plt.plot(x, y22, label='fourThread')
    plt.plot(x, y23, label='twoThread')
    plt.plot(x, y24, label='singleThread')

    plt.xlabel('scale of insts')
    plt.ylabel('Load Misses Ratio')
    plt.title("compositive Load Misses Ratio")
    plt.legend()
    fig.savefig('LOAD MISS RATIO OF L1.png', dpi=fig.dpi)

    fig = plt.figure()
    plt.plot(x, y31, label='eightThread')
    plt.plot(x, y32, label='fourThread')
    plt.plot(x, y33, label='twoThread')
    plt.plot(x, y34, label='singleThread')

    plt.xlabel('scale of insts')
    plt.ylabel('IPC')
    plt.title("compositive IPC plot")
    plt.legend()
    fig.savefig('IPC.png', dpi=fig.dpi)

