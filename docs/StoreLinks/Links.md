# About $Send_links 
This command lets users access all messages which contain URLs. The messages Containing URL are automatically get appended in a file and the file is attached when the $send_links command is input.


# Location of Code
The code that implements the above-mentioned functionality is located in cogs/links.py.

# Code Description

### Functions

1. def on_message(self, message):
   The function gets called when a new message is in the group. It checks if the message contains a URL, if yes then the message will be stored in a file. 
2. def send_links(self, ctx):
   The function gets called when a user sends $send_links. The links.txt file is sent as an attachment in return.
   
# How to run it? 
  You are on the server that has the Classmate Bot active and online. All you have to do is enter the command $send_links in return the bot will send a text file that contains all messages with URL.
 
