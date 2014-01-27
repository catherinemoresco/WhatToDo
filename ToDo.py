import csv, datetime, random

todo = {} 
timeframes = {"Overdue": (-9999999, 0), "Today": (0,1) , "Tomorrow": (1, 2), "This Week": (2, 7), "This Month": (7, 30), "Distant Future": (30, 9999999)} # Temporal categories into which events will fall
compliments = {1: "You can do it!", 2: "You rock. I am so proud of you.", 3: "Success is in your blood.", 4: "You deserve success.", 5: "You are a go getter!", 6: "You are unstoppable.", 7: "I wouldn't want to be a to-do list program for anyone other than a superhero like yourself. Good job.", 8: "The world will know of your greatness.", 9: "I love you."}


list1 = open('list.csv', "rb") # Open and read CSV file containing saved to-do list data
reader = csv.reader(list1)
today = datetime.date.today()


for row in reader: # Read CSV file data into todo dictionary as a datetime.date object
	todo[row[0]] = datetime.date(int(row[1]), int(row[2]), int(row[3]))

def timediff(timedue): # Find the number of days between two datetime.date items
	return (timedue - today).days

def collectbytime(frame): # Groups and prints items in todo based on due date
	print frame + ":"
	itemcount = 0
	for item in todo:
		if timediff(todo[item]) >= timeframes[frame][0] and timediff(todo[item]) < timeframes[frame][1]:
			print '- ' + item
			itemcount += 1
	if itemcount == 0:
		print "- -----"
	print
	return 0

def isvaliddate(date): # Checks if a date string is valid
		try:
			splitdate = map(int, date.split('/'))
			date = datetime.date(splitdate[2], splitdate[0], splitdate[1])
			return True
		except:
			return False

def printlist(): # Prints list
	for frame in ["Overdue" ,"Today", "Tomorrow", "This Week", "This Month", "Distant Future"]:
		collectbytime(frame)

def add(): # Adds a new item to list, asking for its name and due date
	name = raw_input("What is your task called?\n")
	date = raw_input("Please enter the date the task is due, in mm/dd/yyyy form.\n")
	if isvaliddate(date):
		splitdate = map(int, date.split('/'))
		todo[name] = datetime.date(splitdate[2], splitdate[0], splitdate[1])
	else:
		print "I'm sorry, I don't recognize that input. Please make sure the date is in mm/dd/yyyy form."

def delete(name): # Remove item from list
	del todo[name]

def save_list(): # Save list to text file
	list1.close()
	slist = open('list.csv', 'wb')	
	writer = csv.writer(slist)
	for item in todo:
		row = item, todo[item].year, todo[item].month, todo[item].day
		writer.writerow(row)
	slist.close()


print "\nHello! Here's your to-do list: \n"
printlist()
while True:
	command = raw_input("What would you like to do next? Please input 'P' to print your list again, 'A' to add an item, or 'C' to complete an item. Enter 'S' to save your list or Q' to save your list and quit.\n")
	if command == "P":
		printlist()
	elif command == "A":
		add()
		printlist()
	elif command == "C":
		delete(raw_input("Which item have you completed?\n"))
		printlist()
		print compliments[random.randrange(1, 9)]
	elif command == "S":
		save_list()
	elif command == "Q":
		save_list()
		quit()
	else: 
		print "I'm sorry, I don't understand that command."
