#!/usr/bin/python3

def change_direction(current_direction, command):
	action = command[0]
	magnitude = int(command[1:])
	
	# 60%360 = 60
	#-60%360 = 300
	
	directions_bylet = {'N':0, 'E':90, 'S':180, 'W':270}
	directions_bydeg = {0:'N', 90:'E', 180:'S', 270: 'W'}
	
	current_degree = directions_bylet[current_direction]
	if action == 'R':
		current_degree += magnitude
	elif action == 'L':
		current_degree -= magnitude
	
	current_degree = current_degree%360
	
	current_direction = directions_bydeg[current_degree]
	
	return current_direction

def change_position(x_position, y_position, current_direction, command):
	action = command[0]
	magnitude = int(command[1:])
	
	if (action == 'N') or (action == 'F' and current_direction == 'N'):
		y_position += magnitude
	elif (action == 'S') or (action == 'F' and current_direction == 'S'):
		y_position -= magnitude
	elif (action == 'W') or (action == 'F' and current_direction == 'W'):
		x_position -= magnitude
	elif (action == 'E') or (action == 'F' and current_direction == 'E'):
		x_position += magnitude
	elif (action == 'L') or (action == 'R'):
		current_direction = change_direction(current_direction, command)
	return (x_position, y_position, current_direction)

def rotate_waypoint(waypoint_x, waypoint_y, command):
	action = command[0]
	magnitude = int(command[1:])
	
	rotation_times =int(magnitude/90)
	
	if action == 'R': # rotate right times rotation times
		for i in range(rotation_times):
			temp_x = waypoint_x
			temp_y = waypoint_y
			# pos x turns into negative y
			# pos y turns into pos x
			waypoint_x = temp_y
			waypoint_y = -temp_x
			
	if action == 'L': # rotate left times rotation times
		for i in range(rotation_times):
			temp_x = waypoint_x
			temp_y = waypoint_y
			# pos x turns into pos y
			# pos y turns into neg x
			waypoint_x = -temp_y
			waypoint_y = temp_x
	
	return waypoint_x, waypoint_y

def change_position_by_waypoint(x_position, y_position, waypoint_x, waypoint_y, command):
	action = command[0]
	magnitude = int(command[1:])
	
	if (action == 'F'):
		y_position += waypoint_y * magnitude
		x_position += waypoint_x * magnitude		
	elif (action == 'N'):
		waypoint_y += magnitude
	elif (action == 'S'):
		waypoint_y -= magnitude
	elif (action == 'W'):
		waypoint_x -= magnitude
	elif (action == 'E'):
		waypoint_x += magnitude
	elif (action == 'L') or (action == 'R'):
		waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, command)
	return (x_position, y_position, waypoint_x, waypoint_y)

if __name__ == "__main__":
	
	input = open("input/day12.txt")
	
	instructions = input.read().split("\n")[:-1]
	
	x_position = 0	# positive is east, negative is west
	y_position = 0	# positive is north, negative is south
	current_direction = 'E'
	
	for instruction in instructions:
		x_position, y_position, current_direction = change_position(x_position, y_position, current_direction, instruction)
	
	print("Solution to part a is:", abs(x_position) + abs(y_position))
	
	x_position = 0	# positive is east, negative is west
	y_position = 0	# positive is north, negative is south
	waypoint_x = 10
	waypoint_y = 1
		
	for instruction in instructions:
		x_position, y_position, waypoint_x, waypoint_y = change_position_by_waypoint(x_position, y_position, waypoint_x, waypoint_y, instruction)
		#print(instruction)
		#print(x_position, y_position, current_direction)
	
	print("Solution to part b is:", abs(x_position) + abs(y_position))