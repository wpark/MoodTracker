import datetime
import os
import pickle
from parse import *

entry = str(raw_input("journal: "))

when = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['when']
what = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['what']
why = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['why']
where = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['where']
rating = parse("On {when}, I felt {what}, because {why}, at {where}, rated {rating},", entry).named['rating']

entry_list = [what, why, where, rating]

journal = dict()
journal[when]=entry_list
with open("table.txt", "a+") as f:
	pickle.dump(journal, f)

objects = []
with (open("table.txt", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
print objects
# store_file.close()


#print entry


#journal[when] = entry
#print journal
# class Entry:
# 	def __init__(self, when, ewhat, why, where, rating):
# 		self.when = when
# 		self.what = what
# 		self.why = why
# 		self.where = where
# 		self.rating = rating

# 		if (when == None):
# 			raise	
# 		else:
# 			self.date = day(when) 
# 		self.entry_list = [what, why, where, rating]

# 	def day(date_string):
# 		today = dateime.date.today()
# 		date_string = date_string.strip().lower().replace('/',' ').replace('-', ' ').replace(',',' ')
# 		#if date_string 


# class Journal(Entry):
# 	# key <- date
# 	# values <- [what, why, where, rating]
#     def __init__(self, Entry):
# 		self.data = {date: [Entry.what, why, where, rating]}
	
# 	# def update(self, data, int):
# 	# 	data[int]=





