import os
import time
import logging
  
# get message from the user.
msg = print("Enter the message you want ot send: ")

# set up entities to be logged like username and timestamp.
username = getpass.getuser()
timestamp = time.time()
receiver = "all"

# send the messsage using the wall command.
command = "wall " + msg
os.system(command)

# logging the message.
logname = "messages.log"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(username)s, %(receiver)s %(msg)s %(timestamp)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("message logging")

self.logger = logging.getLogger('urbanGUI')