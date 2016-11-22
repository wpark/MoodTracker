import os
import pickle
from parse import *
import parseDate

entry = str(raw_input("journal: "))

when = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['when']
what = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['what']
why = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['why']
# How to make "where" optional? 
where = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['where']
# convert rating string into number
rating = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['rating']


entry_list = [what, why, where, rating]
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

	print journal

	journal.update({when_datetime:entry_components})
	with open('journal.txt', 'wb') as f:
		pickle.dump(journal,f)

	print '\n'
	print journal

# sort dictionary in the chronological order

add_entry(entry_list, when_date)


