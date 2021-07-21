import os
import time
import datetime
import getpass
import sys


choice = raw_input("Do you want to send a message to all users or one user? (All/One)"
# get message from the user
if choice == "One":
	receiver = raw_input("Enter the name of the user you want to send the message to: ")
elif choice == "All":
	receiver = "all"
else:
	print("Wrong choice!")
	sys.exit()
msg = raw_input("Enter the message you want to send: ")

# set up entities to be logged like username and timestamp
username = getpass.getuser()
timestamp = datetime.datetime.fromtimestamp(time.time())

# send the message using the wall command
if choice == "One":
	command = "write " + receiver + msg
elif choice == "All":
	command = "wall " +  msg
os.system(command)

#logging the message
logname = "messages.log"
log = username + "," + receiver + "," + msg + "," + str(timestamp)
with open(logname, "a") as myfile:
  myfile.write(log)
  myfile.write("\n")
