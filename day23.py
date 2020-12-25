#!/usr/bin/python3

def play_move(current_cup_index, cup_circle):
	current_cup_value = cup_circle[current_cup_index]
	
	#print("current cup:", current_cup_value, "from index:", current_cup_index)
	
	removed_cups = []
	for i in [0,1,2]:
		if current_cup_index+1 > len(cup_circle):
			removed_cups.append(  cup_circle.pop( 0 ) )
		else:
			removed_cups.append(  cup_circle.pop( (current_cup_index+1) % len(cup_circle) ) )
	
	#print("pick up:", removed_cups, end = "     ")
	
	next_cup_value = ( current_cup_value - 1 )
	if next_cup_value == 0: next_cup_value = 9
	
	while next_cup_value not in cup_circle:
		next_cup_value -= 1
		if next_cup_value == 0: next_cup_value = 9
			
	#print("destination:", next_cup_value, end = "     ")
			
	insert_index = cup_circle.index(next_cup_value) + 1
	
	removed_cups = removed_cups[::-1]
	
	for i in [0,1,2]:
		cup_circle.insert(insert_index, removed_cups.pop(0) )
	
	#print(cup_circle)
	
	current_cup_index = cup_circle.index(current_cup_value) 
	
	return cup_circle, current_cup_index

def play_move_v2(current_cup, cup_circle):
	removed_cups = []
	
	# find cups to be removed
	removed_cups.append(cup_circle[ current_cup ])
	removed_cups.append(cup_circle[ removed_cups[0] ])
	removed_cups.append(cup_circle[ removed_cups[1] ])
	
	# "remove"
	new_next_cup = cup_circle[ removed_cups[2] ]
	cup_circle[current_cup] = new_next_cup
	
	# find where to insert
	insertion_cup = current_cup - 1	# the cup with a label equal to the current cup's label minus one
	# If this would select one of the cups that was just picked up, 
	# the crab will keep subtracting one until it finds a cup that wasn't just picked up
	# If at any point in this process the value goes below the lowest value on any cup's label, 
	# it wraps around to the highest value on any cup's label instead.
	if insertion_cup == 0:
		insertion_cup = 1000000
	while insertion_cup in removed_cups:
		insertion_cup -= 1	
		if insertion_cup == 0:
			insertion_cup = 1000000
	cup_following_insertion = cup_circle[insertion_cup]
	
	# "insert"
	cup_circle[insertion_cup] = removed_cups[0]
	# removed cup 0 should still link to 1 and 1 should still link to 2
	cup_circle[ removed_cups[2] ] = cup_following_insertion
	
	current_cup = new_next_cup
	
	return current_cup

def print_order_after(cup_value, cup_circle):
	
	while cup_circle[0] != cup_value:
		cup_circle.append(cup_circle.pop(0))
	cup_circle.pop(0)
	
	string = ""
	for num in cup_circle:
		string += str(num)
		
	return string

def fetch_index_of_one(cup_circle):
	
	index = cup_circle.index(1) 
	
	return index

if __name__ == "__main__":
		
	cup_circle = [int(num) for num in open("input/day23.txt").read() ]
	
	print(cup_circle)
	# counterclockwise <-  -> clockwise
	
	num_moves = 100
	num_cups = len(cup_circle)
	current_cup_index = 0
	
	for i in range(num_moves):
		cup_circle, current_cup_index = play_move(current_cup_index, cup_circle)
		current_cup_index += 1
		if current_cup_index >= num_cups: current_cup_index = 0
	
	print("Solution to part a is:", print_order_after(1, cup_circle))
	
	
	
	cup_circle = [int(num) for num in open("input/day23.txt").read() ]
	
	# not sure how to approach this one... it will take forever to run like above
	# as in, 1000 moves is about a minute, so would need about 10k minutes to run it
	
	num_moves = 10000000
	num_cups = len(cup_circle)
	current_cup_index = 0
	
	dict_cups = {}
	# thank u internet for "hint hint think about dicts" suggestion
	
	for i in range(len(cup_circle) - 1):
		dict_cups[ cup_circle[i] ] = cup_circle[i+1]
	
	dict_cups[ cup_circle[-1] ] = 10
	
	for i in range(10,1000000):
		dict_cups[i] = i+1
	dict_cups[1000000] = cup_circle[0]
	
	current_cup = cup_circle[0]
	for i in range(num_moves):
		print(i, end="\r")
		current_cup = play_move_v2(current_cup, dict_cups)
	#print(dict_cups)
		
	
	print("Solution to part b is:", dict_cups[1] * dict_cups[dict_cups[1]])
	