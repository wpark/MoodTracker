import datetime

# store_file = open("Table.txt", "w")
# store_file.write("something")
# store_file.close()


class Entry:

	def __init__(self, when=None, what=None, why=None, where=None, rating=0):
		if (when == Nones) {		
		}
		else {
		self.date = day(when) 
		}
		self.entry_list = [what, why, where, rating]

	def day(date_string):
		today = dateime.date.today()
		date_string = date_string.strip().lower().replace('/',' ').replace('-', ' ')



class Journal(Entry):
	# key <- date
	# values <- [what, why, where, rating]
	data = dict()
	
	# def update(self, data, int):
	# 	data[int]=




something = Entry()
print(something.entry_list)


# class Mapping:
# 	def __init__(self, iterable):
# 		self.entry_list = [Entry.when, Entry.what, Entry.why, Entry.where]
# 		self.__update(iterable)

# 	def update(self, iterable):
# 		for item in iterable:
# 			self.entry_list.append(item)

# 	__update = update


# class MappingSubclass(Mapping):
# 	def update(self,key,values):
# 		for item in zip(keys, values):
# 			self.entry_list.append(item)

