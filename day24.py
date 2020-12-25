#!/usr/bin/python3


def get_bounds(coordinates): # x is 1 if above or below, 2 otherwise; y in multiples of 2
	
	min_x, max_x, min_y, max_y = (0,0,0,0)
	
	for x in coordinates:
		if x > max_x:	max_x = x
		elif x < min_x: min_x = x
		for y in coordinates[x]:
			if y > max_y:	max_y = y
			elif y < min_y:	min_y = y
				
	max_x += 2
	min_x -= 2
	max_y += 2
	min_y -= 2
	
	return min_x, max_x, min_y, max_y



def check_neighbors(coordinates, coord):
	neighbor_sum = 0
	colour = 1
	
	x = coord[0]
	y = coord[1]
	
	if x in coordinates and y in coordinates[x]:
		colour = 0
	
	to_check = []
	to_check.append( ( x+2, y ) )
	to_check.append( ( x-2, y ) )
	to_check.append( ( x+1, y+2 ) )
	to_check.append( ( x+1, y-2 ) )
	to_check.append( ( x-1, y+2 ) )
	to_check.append( ( x-1, y-2 ) )
	
	for entry in to_check:
		if entry[0] in coordinates and entry[1] in coordinates[entry[0]]:
			neighbor_sum += 1
	
	return colour, neighbor_sum

	
def day_update(coordinates, min_x, max_x, min_y, max_y):
	
	new_coordinates = {}
	sum_black = 0
	
	for x in range(min_x, max_x+1):
		for y in range(min_y, max_y+2, 2):
			colour, neighbor_sum = check_neighbors(coordinates, (x,y) )
			if colour == 0 and 0 < neighbor_sum <= 2:
				if x in new_coordinates:
					new_coordinates[x].append(y)
				else:
					new_coordinates[x] = [y]
				sum_black += 1
			elif colour == 1 and neighbor_sum == 2:
				if x in new_coordinates:
					new_coordinates[x].append(y)
				else:
					new_coordinates[x] = [y]
				sum_black += 1
	
	return new_coordinates, sum_black
	
	
def parse_coordinate(line):
	
	x = 0
	y = 0
	
	i = 0
	
	while i<len(line):
		if line[i] == 'e':
			x += 2
		elif line[i] == 'w':
			x -= 2
		else:
			direction = line[i:i+2]
			i+=1
			
			if direction == "ne":
				x += 1
				y += 2
			elif direction == "nw":
				x -= 1
				y += 2
			elif direction == "se":
				x += 1
				y -= 2
			elif direction == "sw":
				x -= 1
				y -= 2
		
		i+=1
	
	return (x, y)
	

if __name__ == "__main__":
	
	data = open("input/day24.txt").read()[:-1].split("\n")
	
	coordinates = {} 
	# originally this was a list of coords. but this got horribly inefficient past ~1000 entries
	# so now it's a dict of lists
	# it still starts slowing down marginally once you hit 2000+ entries, but the whole thing runs in < 5 seconds
	
	sum_coords = 0
	
	for line in data:
		x, y = parse_coordinate(line)
		if x in coordinates and y in coordinates[x]:
			sum_coords -= 1
			coordinates[x].remove(y)	# because it's just gonna be flipped back
		elif x in coordinates:
			coordinates[x].append(y)
			sum_coords += 1
		else:
			coordinates[x] = [y]
			sum_coords += 1
	
	print("Solution to part a is:", sum_coords)
	#exit()
	#print(coordinates)
	
	num_days_to_run = 100
	
	for i in range(1, num_days_to_run+1):
		min_x, max_x, min_y, max_y = get_bounds(coordinates)
		coordinates, sum_black = day_update(coordinates, min_x, max_x, min_y, max_y)
		#print("Day",i,": ", sum_black)
	
	
	
	print("Solution to part b is:", sum_black)
	