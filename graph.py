import numpy as np
import matplotlib.pyplot as plt
import collections
import time, datetime
#import main

# get the dictionary from main
#exDict = collections.OrderedDict([(datetime.date(2016, 11, 11), ['test2', 'test2', '8', 'g']), (datetime.date(2016, 11, 12), ['weird', 'weird', '1.1', 'nc']), (datetime.date(2016, 11, 13), ['blue', 'blue', '1', 'nc']), (datetime.date(2016, 11, 27), ['test', 'test', '6', 'r']), (datetime.date(2016, 11, 29), ['this', 'this', '6', 'c']), (datetime.date(2016, 11, 30), ['success', 'success', '7', 'y'])])
#journalEntries = 

def drawGraph(dictionary):
	N = len(dictionary)
	#print N
    
    #y-axis  
	ratings = []
	for k, v in dictionary.items():
		ratings.append(float(v[2]))

	ratings = tuple(ratings)
	print ratings

	#x-axis
	dates = []
	for k, v in dictionary.items():
		dates.append(k.strftime('%m-%d-%Y'))

	dates = tuple(dates)

	ind = np.arange(N)
	width = 0.35
	opacity = 0.4


	p = plt.bar(ind, ratings, width, color = "#AAF0D1", edgecolor = "#AAF0D1")

	#p = plt.bar(ind, ratings, width, alpha = opacity, color = "r")

	#colors
	colors = []
	for k, v in dictionary.items():
		colors.append(v[3])
	print colors

	for i in range(N):
		if colors[i] == 'nc':
			pass
		else:
			p[i].set_color(colors[i])

	# p[0].set_color('y')
	# p[1].set_color('m') #magenta
	# p[2].set_color('c') #cyan

	plt.xticks(ind + width/2, dates)


	plt.ylabel('Rating')
	plt.xlabel("Dates")
	plt.yticks(np.arange(0, 11, 1))
	
	plt.title("Mood Tracker")
	plt.show()


# def listmode(dictionary):
# 	n = len(dictionary)

# 	for k, v in dictionary.items():
		
