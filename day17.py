#!/usr/bin/python3


def print_coord_map(coord_map, x_range, y_range, z_range):
	for z in range( z_range[0], z_range[1]):
		print("z =", z)
		for y in range( y_range[0], y_range[1]):
			for x in range( x_range[0], x_range[1]):
				print(coordinates[(x,y,z)], end="")
			print()
		print()

def count_neighbors(coord_map, coord, x_range, y_range, z_range):
	possible_locations = [ ]
	
	for z in ( coord[2]-1, coord[2], coord[2]+1):
		for y in ( coord[1]-1, coord[1], coord[1]+1):
			for x in ( coord[0]-1, coord[0], coord[0]+1):
				possible_locations.append( (x,y,z) )
				
	possible_locations.remove(coord)
	sum = 0
	
	for entry in possible_locations:
		if entry in coord_map and coord_map[entry] == '#':
			sum += 1
	
	return sum

def simulate_cycle(coord_map, x_range, y_range, z_range):
	new_coord_map = {}
	for z in range( z_range[0]-1, z_range[1]+1):
		for y in range( y_range[0]-1, y_range[1]+1):
			for x in range( x_range[0]-1, x_range[1]+1):
				coord = (x,y,z)
				neighbors = count_neighbors(coord_map, coord, x_range, y_range, z_range)
				if coord in coord_map and coord_map[coord] == '#':
					if 2 <= neighbors <= 3:
						new_coord_map[coord] = '#'
					else:
						new_coord_map[coord] = '.'
				else:
					if neighbors == 3:
						new_coord_map[coord] = '#'
					else:
						new_coord_map[coord] = '.'
					
	x_range = (x_range[0]-1, x_range[1]+1)
	y_range = (y_range[0]-1, y_range[1]+1)
	z_range = (z_range[0]-1, z_range[1]+1)
	
	return new_coord_map, x_range, y_range, z_range


def count_neighbors_v2(coord_map, coord, x_range, y_range, z_range, w_range):
	possible_locations = [ ]
	
	for w in ( coord[3]-1, coord[3], coord[3]+1):
		for z in ( coord[2]-1, coord[2], coord[2]+1):
			for y in ( coord[1]-1, coord[1], coord[1]+1):
				for x in ( coord[0]-1, coord[0], coord[0]+1):
					possible_locations.append( (x,y,z, w) )
				
	possible_locations.remove(coord)
	sum = 0
	
	for entry in possible_locations:
		if entry in coord_map and coord_map[entry] == '#':
			sum += 1
	
	return sum

def simulate_cycle_v2(coord_map, x_range, y_range, z_range, w_range):
	new_coord_map = {}
	for w in range( w_range[0]-1, w_range[1]+1):
		for z in range( z_range[0]-1, z_range[1]+1):
			for y in range( y_range[0]-1, y_range[1]+1):
				for x in range( x_range[0]-1, x_range[1]+1):
					coord = (x,y,z,w)
					neighbors = count_neighbors_v2(coord_map, coord, x_range, y_range, z_range, w_range)
					if coord in coord_map and coord_map[coord] == '#':
						if 2 <= neighbors <= 3:
							new_coord_map[coord] = '#'
						else:
							new_coord_map[coord] = '.'
					else:
						if neighbors == 3:
							new_coord_map[coord] = '#'
						else:
							new_coord_map[coord] = '.'
					
	x_range = (x_range[0]-1, x_range[1]+1)
	y_range = (y_range[0]-1, y_range[1]+1)
	z_range = (z_range[0]-1, z_range[1]+1)
	w_range = (w_range[0]-1, w_range[1]+1)
	
	return new_coord_map, x_range, y_range, z_range, w_range

def count_active_cells(coord_map):
	sum = 0
	for entry in coord_map:
		if coord_map[entry] == '#':
			sum += 1
	return sum
		
		
if __name__ == "__main__":
	
	input = open("input/day17.txt").read().split("\n")[:-1]
	
	coordinates = {}
	x_range = [0]
	y_range = [0]
	z_range = [0,1]	
	
	y = 0
	for line in input:
		x = 0
		for char in line:
			coordinates[ (x, y, 0) ] = char
			x += 1
		y += 1
	x_range.append(x)
	y_range.append(y)
		
	#print_coord_map(coordinates, x_range, y_range, z_range)
	#print(count_active_cells(coordinates))
	
	for i in range(6):
		coordinates, x_range, y_range, z_range = simulate_cycle(coordinates, x_range, y_range, z_range)
			
		
	print("Solution to part a is:", count_active_cells(coordinates))
	
	
	
	coordinates = {}
	x_range = [0]
	y_range = [0]
	z_range = [0,1]	
	w_range = [0,1]
	
	y = 0
	for line in input:
		x = 0
		for char in line:
			coordinates[ (x, y, 0, 0) ] = char
			x += 1
		y += 1
	x_range.append(x)
	y_range.append(y)
	
	
	for i in range(6):
		print("Simulation " + str(i), end="\r")
		coordinates, x_range, y_range, z_range, w_range = simulate_cycle_v2(coordinates, x_range, y_range, z_range, w_range)
	
	
	print("Solution to part b is:", count_active_cells(coordinates))
	