#!/usr/bin/python3

input = open("input/day02.txt")

# format: [min, max, letter, password]

passwords = []

for line in input:
	dash_loc = line.find("-")
	space_loc = line.find(" ")
	colon_loc = line.find(":")
	passwords.append([line[:dash_loc],line[dash_loc+1:space_loc],line[space_loc+1:colon_loc],line[colon_loc+2:-1]])
	
sum = 0

for pw in passwords:
	cnt = pw[3].count(pw[2])
	if (cnt >= int(pw[0]) and cnt <= int(pw[1])):
		sum += 1
	
print("Solution to part a:",sum)

sum = 0

for pw in passwords:
	pos1 = pw[3][int(pw[0])-1] == pw[2]		# -1 because their indices start at 1
	pos2 = pw[3][int(pw[1])-1] == pw[2]
	
	if pos1 and pos2:
		pass
	elif pos1 or pos2:
		sum += 1
		
print("Solution to part b:",sum)
		
	
	
