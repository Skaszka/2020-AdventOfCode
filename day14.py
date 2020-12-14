#!/usr/bin/python3

def return_masked_integer(binary_value, binary_mask):
	
	for i in range(len(binary_mask)):
		if binary_mask[i] == 'X':
			pass	# don't do anything to value
		elif binary_mask[i] == '1':
			binary_value[i] = 1
		elif binary_mask[i] == '0':
			binary_value[i] = 0
	
	binary_string = ""
	for i in binary_value:
		binary_string += str(i)
	
	return int(str(binary_string), 2)

def generate_masked_locations(masked_location):
	
	#print(masked_location)
	
	list_locations = [""]
	
	for char in masked_location:
		#print(char)
		#print(list_locations)
		if char == '0':
			for i in range(len(list_locations)):
				list_locations[i] += '0'
		elif char == '1':
			for i in range(len(list_locations)):
				list_locations[i] += '1'
		elif char == 'X':
			temp_list = list_locations.copy()
			for i in range(len(list_locations)):
				list_locations[i] += '1'
				temp_list[i] += '0'
			list_locations.extend(temp_list)
		else:
			print("error")
			
	#print(list_locations)
	
	return [int(entry, 2) for entry in list_locations]

def return_list_masked_locations(binary_location, binary_mask):
	
	masked_location = ""
	for i in range(len(binary_mask)):
		if binary_mask[i] == 'X':
			masked_location += 'X'	# don't do anything to value
		elif binary_mask[i] == '1':
			masked_location += '1' 
		elif binary_mask[i] == '0':
			masked_location += str(binary_location[i])
			
	#print(masked_location)
	
	return generate_masked_locations(masked_location)

if __name__ == "__main__":
	
	input = open("input/day14.txt").read().split("\n")[:-1]
	
	mem = {}
	
	binary_mask = ""
	
	for line in input:
		if "mask =" in line:
			binary_mask = line[7:]
		else:
			mem_index = line.find("]")
			equal_index = line.find("=")
			mem_location = int(line[4:mem_index])
			mem_value = int(line[equal_index+2:])
			temp_mem_value = [1 if digit=='1' else 0 for digit in bin(mem_value)[2:]]
			mem_value = [0 for i in range(len(binary_mask) - len(temp_mem_value))]
			mem_value.extend(temp_mem_value)
			mem[mem_location] = return_masked_integer(mem_value, binary_mask)
			
			
	
	print("Solution to part a is:", sum([mem[key] for key in mem]))
	
	mem = {}
	
	
	binary_mask = ""
	
	for line in input:
		if "mask =" in line:
			binary_mask = line[7:]
		else:
			mem_index = line.find("]")
			equal_index = line.find("=")
			mem_location = int(line[4:mem_index])
			mem_value = int(line[equal_index+2:])
			temp_mem_location = [1 if digit=='1' else 0 for digit in bin(mem_location)[2:]]
			mem_location = [0 for i in range(len(binary_mask) - len(temp_mem_location))]
			mem_location.extend(temp_mem_location)
			list_of_locations = return_list_masked_locations(mem_location, binary_mask)
			for entry in list_of_locations:
				mem[entry] = mem_value
	
	print("Solution to part b is:", sum([mem[key] for key in mem]))
	