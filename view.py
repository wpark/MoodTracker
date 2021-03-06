import numpy as np
import matplotlib.pyplot as plt
import collections
import time, datetime


#exDict = collections.OrderedDict([(datetime.date(2016, 11, 11), ['test2', 'test2', '8', 'g']), (datetime.date(2016, 11, 12), ['weird', 'weird', '1.1', 'nc']), (datetime.date(2016, 11, 13), ['blue', 'blue', '1', 'nc']), (datetime.date(2016, 11, 27), ['test', 'test', '6', 'r']), (datetime.date(2016, 11, 29), ['this', 'this', '6', 'c']), (datetime.date(2016, 11, 30), ['success', 'success', '7', 'y'])])

def drawGraph(dictionary):
	N = len(dictionary)
    
    #y-axis  
	ratings = []
	for k, v in dictionary.items():
		ratings.append(float(v[2]))

	ratings = tuple(ratings)

	#x-axis
	dates = []
	for k, v in dictionary.items():
		dates.append(k.strftime('%m-%d-%Y'))

	dates = tuple(dates)

	ind = np.arange(N)
	width = 0.35


	p = plt.bar(ind, ratings, width, color = "#AAF0D1", edgecolor = "#AAF0D1")

	#colors
	colors = []
	for k, v in dictionary.items():
		colors.append(v[3])

	for i in range(N):
		# default color
		if colors[i] == 'nc':
			pass
		else:
			p[i].set_color(colors[i])


	plt.xticks(ind + width/2, dates)


	plt.ylabel('Rating')
	plt.xlabel("Dates")
	plt.yticks(np.arange(0, 11, 1))
	
	plt.title("Mood Tracker")
	plt.show()


def listmode(dictionary):
 	n = 1

 	for key, value in dictionary.items():
 		print str(n) + ". " + str(key)  
 		print "What: "+ str(value[0])
 		print "Why: " + str(value[1])
 		print "Rating: " + str(value[2])
 		print '\n'
 		n += 1

		
