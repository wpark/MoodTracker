import numpy as np
import matplotlib.pyplot as plt
import collections
import time, datetime
#import main

exDict = collections.OrderedDict([(datetime.date(2016, 11, 8), ['another test', 'another test', 'another test', '3']), (datetime.date(2016, 11, 9), ['print', 'print', 'print', '9']), (datetime.date(2016, 11, 10), ['this', 'this', 'this', '4']), (datetime.date(2016, 11, 11), ['nothing', 'nothing', 'nothing', '3']), (datetime.date(2016, 11, 12), ['this', 'this', 'this', '5']), (datetime.date(2016, 11, 14), ['test2', 'test2', 'test2', '1']), (datetime.date(2016, 11, 15), ['test3', 'test3', 'test3', '2']), (datetime.date(2016, 11, 18), ['test', 'test', 'test', '0']), (datetime.date(2016, 11, 22), ['stressed', 'i had a lot of homework', 'school', '2']), (datetime.date(2016, 11, 23), ['bored', 'i had to pack', 'school', '3']), (datetime.date(2016, 11, 24), ['a little bad', 'i was getting sick', 'school', '3']), (datetime.date(2016, 11, 25), ['excited', 'it was thanksgiving', 'oregon', '8']), (datetime.date(2016, 11, 26), ['full', 'I ate too much to eat', 'portland', '6']), (datetime.date(2016, 11, 27), ['tired', 'i was travelling', 'oregon', '5']), (datetime.date(2016, 11, 28), ['sick', 'I have a flu', 'everywhere', '1']), (datetime.date(2016, 11, 30), ['still sick', 'i still have the flu', 'school', '3'])])

def drawGraph(dictionary):
	N = len(dictionary)
	#print N
    
    #y-axis  
	ratings = []
	for k, v in dictionary.items():
		ratings.append(int(v[3]))

	ratings = tuple(ratings)
	print ratings

	#x-axis
	dates = []
	for k, v in dictionary.items():
		dates.append(k.strftime('%m-%d'))

	dates = tuple(dates)

	ind = np.arange(N)
	width = 0.35
	opacity = 0.4

	p = plt.bar(ind, ratings, width, color = "#AAF0D1")
	#p = plt.bar(ind, ratings, width, alpha = opacity, color = "r")
		#edgecolor = 'b')
	# p[0].set_color('y')
	# p[1].set_color('m') #magenta
	# p[2].set_color('c') #cyan

	plt.xticks(ind + width, dates)


	plt.ylabel('Rating')
	plt.xlabel("Dates")
	plt.yticks(np.arange(0, 11, 1))
	
	plt.title("Mood Tracker")
	plt.show()

drawGraph(exDict)