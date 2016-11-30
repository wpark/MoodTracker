import os
import pickle
from parse import *
import parseDate
import collections

# global variable dictionary
orderedJournal = dict()

entry = str(raw_input("journal: "))

when = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['when']
what = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['what']
why = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['why']
# How to make "where" optional? 
where = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['where']
rating = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['rating']

# b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white
color = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating}, color {color}", entry).named['color']


entry_list = [what, why, where, rating, color]
when_date = parseDate.convertDate(when)

def add_entry(entry_components, when_datetime):
	journal = dict()
	try:
		with (open('journal.txt','rb')) as openfile:
			print "something"
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



add_entry(entry_list, when_date)
#print '\n'
print orderedJournal
# print orderedJournal.items()[1]


