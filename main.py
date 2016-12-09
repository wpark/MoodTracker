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

# entry_list = [what, why, rating, color]

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

	return errorHandling(entry_list, when_date, color)



def errorHandling(entry_components, when_datetime, color_string):
	if (color_string in availableCol) and (when_datetime != None) and (entry_components[2].isdigit()):
		add_entry(entry_components, when_datetime)
	# check if the input for date is in a right format.
	elif (when_datetime == None):
		print ("Error: Please check if the date is in a right format.")
	# check if the input for rating is a digit
	elif (entry_components[2].isdigit() != True):
		print ("Error: Please check if the rating is a digit.")
	# check if the character input for color is one of the available colors
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
		#print "empty dictionary"

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
		pass

	#global orderedJournal
	print orderedJournal	
	graph.drawGraph(orderedJournal)



# Menu options

def print_menu():       
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Write a journal entry"
    print "2. Graph that shows the trend of your moods from previous entries"
    print "3. Menu Option 3"
    print "4. Exit"
    print 67 * "-"


loop=True      
  
while loop:         
    print_menu()    
    choice = input("Enter your choice [1-4]: ")
     
    if choice==1:     
        print "Writing an entry..."
        startEntry()
        ## You can add your code or functions here
    elif choice==2:
        print "Creating a graph..."
        createGraph()
        ## You can add your code or functions here
    elif choice==3:
        print "list mode"
        ## You can add your code or functions here
    elif choice==4:
        print "Exiting..."
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")


