import datetime
import os
import pickle
from parse import *

entry = str(raw_input("journal: "))

when = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['when']
what = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['what']
why = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['why']
# How to make "where" optional? 
where = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['where']
# convert rating string into number
rating = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['rating']

entry_list = [what, why, where, rating]


# 	def day(date_string):
# 		today = dateime.date.today()
# 		date_string = date_string.strip().lower().replace('/',' ').replace('-', ' ').replace(',',' ')
# 		#if date_string 

journal = dict()
try:
	with (open('test.txt','rb')) as openfile:
		print "something"
		while True:
			try:
				journal = pickle.load(openfile)
				#journal.update(pickle.load(openfile))
			except EOFError:
				break
except IOError:
	print "We're here"
	with (open('test.txt','wb')) as f:
		pickle.dump(journal,f)

print journal


journal.update({when:entry_list})

with open('test.txt', 'wb') as f:
	pickle.dump(journal,f)

print '\n'
print journal



