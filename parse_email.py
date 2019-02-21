#!/bin/python

#Author:	Yoan Hermida
#Date:		14 June 2015
#Purpose:	Take monolithic text file of emails and split into 
#			multiple text files to be able to import into mail program.

import re

#Take the input.
txt = open('txt/file/path/here').read()

#Split based on condition, in this case that it contains -- End -- at the end of each message.
emailList = re.split(r'-- End --', txt)

i = 0
for emails in emailList:
	#Open file to be written to, using iterator to increment filename by 1.
	file = open('output/files/path/here/'+str(i)+'.txt', 'w')
	file.write(emailList[i])
	i += 1