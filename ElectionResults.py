#!/usr/bin/env python3
"""
Jenny Bloom
09/12/2015
Homework #3

This assignment analyzes student council presidential election data and 
reports the data derived from four major divisions, each of which have 
several items.
"""
import sys

file_name = sys.argv[1] #store argument into variable "file_name"
dataDict = {} #create universe - generate empty space for dictionary.
print(file_name)
f = open(file_name, 'r') #Open file_name (.txt containing Election Results)
for line in f:
	splitLine = line.split()
	dataDict [splitLine[0] + ' ' + splitLine[1]] = int(splitLine[2]) + int(splitLine[3]) + int(splitLine[4]) + int(splitLine[5]) #Generates dictionary of total amount of votes each candidate received.
print(dataDict)
f.close() #Close file when done creating dictionary from the election results.

total_votes = sum(dataDict.values()) #Gives total number of votes counted in the dictionary
print(total_votes)
max_votes = max(dataDict.values()) #Gives highest number of votes counted inside the dictionary
print(max_votes)

templateHeader = "{0:^15}{1:>8}{2:>10}" #Header for output. First in set refers to column #, second in set refers to spacing, operators refer to ^center-aligned, >right aligned respectively.
print("\n")
print(templateHeader.format("Candidate", "Votes", "Percent")) #titles of header
print(templateHeader.format("=========", "=====", "=======")) # funny bars for some unknown formatting purpose.

template = "{0:^15}{1:>8}{2:>8}" #Table formatting underneath the header columns. Could have used format() also, but didn't know I could use functions yet.

for i, n, in dataDict.items():
	percentage = int((n/total_votes) * 100)
	print(template.format(i,n, percentage) + "%") #prints the creation of percentage from the total votes and the number of votes per name stored in 'n'. 'i' is the counter to run through the dictionary.
	
print("\n")
print("The winner is " + max(dataDict, key=dataDict.get) + " with " + str(max_votes) + " votes.")
print("\n")
print("Total votes polled: " + str(total_votes))
print("\n") 

f.close()

