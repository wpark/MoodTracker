import os
import pickle
from parse import *
import parseDate
import collections

# global variable dictionary
orderedJournal = dict()


availableCol = frozenset(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'nc'])

entry = str(raw_input("journal: "))

when = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['when']
what = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['what']
why = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['why']
# How to make "where" optional? 
#where = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['where']
rating = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['rating']

# b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white
color = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['color']

color = color.lower().strip()
entry_list = [what, why, rating, color]
when_date = parseDate.convertDate(when)
# check if the rating is a number


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
		print "We're here"
		with (open('journal.txt','wb')) as f:
			pickle.dump(journal,f)

#	print journal

	journal.update({when_datetime:entry_components})

	# sort dictionary in the chronological order
	global orderedJournal
	orderedJournal = collections.OrderedDict(sorted(journal.items()))

	with open('journal.txt', 'wb') as f:
		pickle.dump(orderedJournal,f)



#add_entry(entry_list, when_date)
checkColorDate(entry_list, when_date, color)
print '\n'
print orderedJournal
# print orderedJournal.items()[1]


