#!/usr/bin/python3

if __name__ == "__main__":
	
	input = open("input/day06.txt")
	
	group = set()
	group_counts = []
	
	for line in input:
		if line == '\n':
			group_counts.append(len(group))
			#print(group)
			group.clear()
		else:
			for char in line[:-1]:
				group.add(char)
	
	group_counts.append(len(group))	# for the last group
	
	print("Solution to part a:", sum(group_counts) )
	
	# there's probably a nicer, cleaner way that does part a and b at once, but this works
	
	input = open("input/day06.txt")
	
	group_first = set()
	group_second = set()
	first_line = True
	
	group_counts = []
	
	for line in input:
		if line == '\n':
			group_counts.append(len(group_first))
			group_first.clear()		
			first_line = True
		elif first_line == True:
			first_line = False
			for char in line[:-1]:
				group_first.add(char)
		else:
			for char in line[:-1]:
				group_second.add(char)
			group_first = group_first.intersection(group_second)
			group_second.clear()
						
	group_counts.append(len(group_first))	# for the last group
	
	print("Solution to part b:", sum(group_counts) )
	
		 
