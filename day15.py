#!/usr/bin/python3

def calc_next_num(i, current_number, last_time_said):	
	
	prev_number = current_number
	
	if prev_number in last_time_said:
		current_number = i - last_time_said[prev_number]
	else:
		current_number = 0
	last_time_said[prev_number] = i
	
	i+=1
	return i, current_number
	
	
	


if __name__ == "__main__":
	
	input = open("input/day15.txt").read().split(",")
	
	last_time_said = {}
	i = 1
	prev_number = 0
	
	for entry in input[:-1]:
		last_time_said[int(entry)] = i
		#print(i,":",entry)
		i+=1
	current_number = int(input[-1])
	
	while (i<2020):
		print(i,end="\r")
		i, current_number = calc_next_num(i, current_number, last_time_said)
		
	print("Solution to part a is:", current_number)
	
	while (i<30000000):
		print(i,end="\r")
		i, current_number = calc_next_num(i, current_number, last_time_said)
	
	print("Solution to part b is:", current_number)
	