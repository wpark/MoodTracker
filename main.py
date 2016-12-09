import os
import pickle
from parse import *
import parseDate
import collections
import graph

# global variable dictionary
global orderedJournal
orderedJournal = dict()

availableCol = frozenset(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'nc'])

# entry = str(raw_input("journal: "))

# when = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['when']
# what = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['what']
# why = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['why']
# # How to make "where" optional? 
# rating = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['rating']

# # b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white
# color = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['color']

# color = color.lower().strip()
# entry_list = [what, why, rating, color]
# when_date = parseDate.convertDate(when)
# # check if the rating is a number

def startEntry():
	entry = str(raw_input("journal: "))

	when = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['when']
	what = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['what']
	why = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['why']
	# How to make "where" optional? 
	rating = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['rating']
	# b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white
	color = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['color']

	color = color.lower().strip()
	entry_list = [what, why, rating, color]
	when_date = parseDate.convertDate(when)

	return checkColorDate(entry_list, when_date, color)



def checkColorDate(entry_components, when_datetime, color_string):
	if (color_string in availableCol) and (when_datetime != None):
		add_entry(entry_components, when_datetime)
	elif (when_datetime == None):
		print ("Error: Please check if the date is in the right format.")
	else:
		print ("Error: Please make sure the chracter(s) you entered for color is one of the below." + "\n" + "b, g, r, c, m, y, k, w, nc")
		return


def add_entry(entry_components, when_datetime):
	journal = dict()
	try:
		with (open('journal.txt','rb')) as openfile:
			while True:
				try:
					#journal = pickle.load(openfile)
					journal.update(pickle.load(openfile))
				except EOFError:
					break
	except IOError:
		with (open('journal.txt','wb')) as f:
			pickle.dump(journal,f)

#	print journal

	journal.update({when_datetime:entry_components})

	# sort dictionary in the chronological order
	global orderedJournal
	orderedJournal = collections.OrderedDict(sorted(journal.items()))

	with open('journal.txt', 'wb') as f:
		pickle.dump(orderedJournal,f)

def createGraph():
	global orderedJournal
	if len(orderedJournal) == 0:
		print "empty dictionary"

		journal = dict()
		try:
			with (open('journal.txt','rb')) as openfile:
				while True:
					try:
						journal.update(pickle.load(openfile))
					except EOFError:
						break
		except IOError:
			with (open('journal.txt','wb')) as f:
				pickle.dump(journal,f)
		
		#print journal

		# sort dictionary in the chronological order
		#global orderedJournal
		orderedJournal = collections.OrderedDict(sorted(journal.items()))
		#print '\n'
		#print orderedJournal
	else:
		print "not empty"

	#global orderedJournal	
	graph.drawGraph(orderedJournal)

