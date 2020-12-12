#!/usr/bin/python3

def count_surrounding_occupied_seats(seating_chart, y, x, x_max, y_max):
	surround_count = 0
	check_positions = []
	check_positions.append([y-1, x])
	check_positions.append([y+1, x])
	check_positions.append([y, x-1])
	check_positions.append([y, x+1])
	check_positions.append([y-1, x-1])
	check_positions.append([y+1, x-1])
	check_positions.append([y-1, x+1])
	check_positions.append([y+1, x+1])
	
	for entry in check_positions:
		if -1 not in entry and not entry[1] == x_max and not entry[0] == y_max :	# remember that bug_map is [y][x]
			if seating_chart[entry[0]][entry[1]] == '#':
				surround_count+=1
	return surround_count

def process_seating_change(seating_chart):
	new_chart = []
	for entry in seating_chart:
		new_chart.append(entry.copy())
	
	y_max = len(seating_chart)
	x_max = len(seating_chart[0])
	
	for y in range(y_max):
		for x in range(x_max):
			if seating_chart[y][x] == '.':
				pass
			elif seating_chart[y][x] == 'L':
				if count_surrounding_occupied_seats(seating_chart, y, x, x_max, y_max) == 0:
					new_chart[y][x] ='#'
			elif seating_chart[y][x] == '#':
				if count_surrounding_occupied_seats(seating_chart, y, x, x_max, y_max) >= 4:
					new_chart[y][x] ='L'
			else:
				print("Something went wrong, got an unknown character.")
	
	return(new_chart)

def check_single_direction(seating_chart, y, x, x_max, y_max, direction):
	# direction is (+y, +x)
	y += direction[0]
	x += direction[1]
	
	while (-1 < y <y_max) and (-1 < x < x_max):
		if seating_chart[y][x] == 'L':
			return 0
		elif seating_chart[y][x] == '#':
			return 1
		y += direction[0]
		x += direction[1]
	
	return 0


def count_surrounding_occupied_seats_v2(seating_chart, y, x, x_max, y_max):
	surround_count = 0
	
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (0, 1))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (0, -1))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (1, 0))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (-1, 0))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (1, -1))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (1, 1))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (-1, -1))
	surround_count += check_single_direction(seating_chart, y, x, x_max, y_max, (-1, 1))
	
	return surround_count

def process_seating_change_v2(seating_chart):
	new_chart = []
	for entry in seating_chart:
		new_chart.append(entry.copy())
	
	y_max = len(seating_chart)
	x_max = len(seating_chart[0])
	
	for y in range(y_max):
		for x in range(x_max):
			if seating_chart[y][x] == '.':
				pass
			elif seating_chart[y][x] == 'L':
				if count_surrounding_occupied_seats_v2(seating_chart, y, x, x_max, y_max) == 0:
					new_chart[y][x] ='#'
			elif seating_chart[y][x] == '#':
				if count_surrounding_occupied_seats_v2(seating_chart, y, x, x_max, y_max) >= 5:
					new_chart[y][x] ='L'
			else:
				print("Something went wrong, got an unknown character.")
	
	return(new_chart)

def count_total_taken_seat(seating_chart):
	sum = 0
	for line in seating_chart:
		for entry in line:
			if entry == '#':
				sum += 1
	return sum

def print_seating_chart(seating_chart):
	for line in seating_chart:
		for entry in line:
			print(entry,end="")
		print()
	return

if __name__ == "__main__":
	
	input = open("input/day11.txt")
	
	seating_chart = input.read().split("\n")[:-1]
	seating_chart_b = seating_chart.copy()
	for i in range(len(seating_chart)):
		seating_chart[i] = [char for char in seating_chart[i]]
		seating_chart_b[i] = [char for char in seating_chart[i]]
		
	while(True):
		temp_chart = process_seating_change(seating_chart)
		if temp_chart == seating_chart:
			seating_chart = temp_chart
			break
		else:
			seating_chart = temp_chart
	
	#print_seating_chart(seating_chart)
	print("Solution to part a is:",count_total_taken_seat(seating_chart))
	
	while(True):
		temp_chart = process_seating_change_v2(seating_chart_b)
		if temp_chart == seating_chart_b:
			seating_chart_b = temp_chart
			break
		else:
			seating_chart_b = temp_chart
	
	print("Solution to part b is:",count_total_taken_seat(seating_chart_b))
		 
