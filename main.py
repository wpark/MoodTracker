import os
import pickle
from parse import *
import parseDate
import collections
import view

# global variable dictionary
global orderedJournal
orderedJournal = dict()

availableCol = frozenset(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'nc'])

# entry_list = [what, why, rating, color]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError, ValueError):
    #     pass

    return False


def startEntry():
	print "\n"
	print "Follow the rules laid out below to write your journal."
	print "On {date}, I felt {what}, because {reason}, rated {number for rating}, color {character},"
	print "And the characters you can enter to choose a color for a bar in the graph are the following:"
	print "b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, nc = default"

	entry = str(raw_input("Enter your journal: "))

	when = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['when']
	what = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['what']
	why = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['why']
	rating = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['rating']
	# b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white
	color = parse("On {when}, I felt {what}, because {why}, rated {rating}, color {color},", entry).named['color']

	color = color.lower().strip()
	entry_list = [what, why, rating, color]
	when_date = parseDate.convertDate(when)

	return errorHandling(entry_list, when_date, color)



def errorHandling(entry_components, when_datetime, color_string):
	if (color_string in availableCol) and (when_datetime != None) and (is_number(entry_components[2])):
		add_entry(entry_components, when_datetime)
	# check if the input for date is in a right format.
	elif (when_datetime == None):
		print ("Error: Please check if the date is in a right format.")
	# check if the input for rating is a number
	elif (is_number(entry_components[2]) != True):
		print ("Error: Please check if the rating is a number.")
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

		# sort dictionary in the chronological order
		orderedJournal = collections.OrderedDict(sorted(journal.items()))
		#print '\n'
		#print orderedJournal
	else:
		print "not empty"
		pass

	#print orderedJournal	
	view.drawGraph(orderedJournal)


def createList():
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

		# sort dictionary in the chronological order
		orderedJournal = collections.OrderedDict(sorted(journal.items()))
		#print '\n'
		#print orderedJournal
	else:
		# Dictionary not empty
		pass

	#print orderedJournal	
	view.listmode(orderedJournal)




# Menu options

def print_menu():       
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Write a journal entry"
    print "2. Graph to see the trend of your moods from previous entries"
    print "3. List to see your previous entries"
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
        print "Creating a list..."
        createList()
        ## You can add your code or functions here
    elif choice==4:
        print "Exiting..."
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")


