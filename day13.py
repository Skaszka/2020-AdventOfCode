#!/usr/bin/python3

def get_ref_and_multiplier(start_point, ref_point_a, bus_id_a, ref_point_b, bus_id_b):
	time_point = start_point
	
	first_match = 0
	second_match = 0
	
	while(True):	
		if (time_point + (ref_point_b - ref_point_a))%bus_id_b != 0:
			time_point += bus_id_a
		elif first_match != 0:
			second_match = time_point
			diff = second_match - first_match
			break
		else:
			first_match = time_point
			time_point += bus_id_a
	
	return (first_match-ref_point_a, diff)
	

if __name__ == "__main__":
	
	input = open("input/day13.txt").read().split("\n")[:-1]
	
	arrival_time = int(input[0])
	buses = input[1].split(",")
	
	closest_id = -1
	closest_time = -1
	
	for bus in buses:
		if bus == 'x':
			continue
		i = 0
		while (int(bus) * i < arrival_time):
			i += 1
		if closest_time == -1 or (int(bus) * i) < closest_time:
			closest_time = int(bus) * i
			closest_id = int(bus)
	
	
	print("Solution to part a is:", closest_id  * (closest_time - arrival_time))
	
	i = 0
	mult = 1
	bus_time_list = []
	
	for bus in buses:
		if bus != 'x':
			bus_time_list.append( (int(bus), i) )
			mult *= int(bus)
		i += 1
			
	bus_time_list.sort(reverse=True)
	#print(bus_time_list)
	
	time_point = bus_time_list[0][0]
	ref_point = bus_time_list[0][1]
	diff = bus_time_list[0][0]
	
	for i in range(1, len(bus_time_list)):
		time_point, diff = get_ref_and_multiplier(time_point, ref_point, diff, bus_time_list[i][1], bus_time_list[i][0])
		ref_point = 0
	
	print("Solution to part b is:", time_point)
	
	exit()
	
	# below can be found attempt 1 and various notes
	
	ref_point = bus_time_list[0][1]
	multiplier = bus_time_list[0][0]
	bus_time_list.pop(0)
	multiple = multiplier
	
	while(True):	
		print(multiplier, end="\r")
		flag = True
		for entry in bus_time_list:
			if (multiplier + (entry[1] - ref_point))%entry[0] != 0:
				multiplier += multiple
				flag = False
				break
		if flag == True:
			break
	
	print("Solution to part b is:", multiplier-ref_point)
	

	# SO I know that the DIFFERENCE between convergent solutions is going to be the product of all the IDs
	# HOWEVER... the first convergence can be lower than that (and will be)
	# HOWEVER HOWEVER... is it possible to figure out what that will be using just two of the entries?
	# like, the difference of that is going to be a denominator of the FULL difference
	# so maybe we can find offset?
	
	# eg, 468 is the first occurence of 59 and 19 - multiple 1121
	# logically, 1068781 - 468 should be divisible by 1121
	# it is! the result is 953
	# is 953 the remaining multiples, ie 31, 13, 7? ...fuck, no it's not
	
	# ATTEMPT 2
	# discover which are divisors of largest number so they don't have to be checked?
	# or, divisors of any numbers? find divisors to reduce what needs to be checked...
	# WAIT HOLD UP
	# if you run this on any two of these, can you then use THAT as a metric?
	# or, as a multiplier source?
	# find the diff, then add that diff each time until you get something that fits with the next num, then add THAT dif each time?