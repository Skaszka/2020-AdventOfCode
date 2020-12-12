#!/usr/bin/python3

def return_contained_contiguous(range_to_check, invalid_number):
	# add continuously, incrementing index
	# if your sum is over invalid_number, return... [0], I guess?
	# do the same if you hit the end of the list and are still lower than invalid_number... tho if that happens, u hecked up
	# otherwise, return the range!
	sum = 0
	end = 0
	for i in range(len(range_to_check)):
		sum += range_to_check[i]
		if sum >= invalid_number:
			end = i+1
			break
			
	if sum == invalid_number:
		return range_to_check[0:end]
	elif sum > invalid_number:
		return [0]
	else:
		print("May have gotten invalid input.")
		return [0]

def is_sum_of_two(preamble, number):
	preamble.sort()
	low = 0
	high = 0
	while preamble:
		low = preamble.pop(0)
		if low*2>number:
			return False
		for entry in preamble:
			if low+entry==number:
				high = entry
				break
		if high!=0:
			return True
	return False

if __name__ == "__main__":

	input = open("input/day09.txt").read().split('\n')[:-1]
	preamble_length = 25
	
	for i in range(len(input)):
		input[i] = int(input[i])
	
	invalid_number = 0
	for i in range(preamble_length, len(input)):
		preamble = input[i-preamble_length:i]
		number = input[i]
		if not is_sum_of_two(preamble, number):
			invalid_number = number
			break
	
	found_contiguous = [0]
	for i in range(len(input)):
		found_contiguous = return_contained_contiguous(input[i:], invalid_number)
		if found_contiguous != [0]:
			break
			
	found_contiguous.sort()
	encryption_weakness = found_contiguous[0] + found_contiguous[-1]
	
	print("Solution to part a:", invalid_number)
	print("Solution to part b:", encryption_weakness)
	