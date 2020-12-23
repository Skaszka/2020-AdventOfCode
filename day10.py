#!/usr/bin/python3

from math import factorial

def get_difs(input):

	difs = {1:0, 2:0, 3:0}
	dif_list = []
	
	for i in range(len(input)-1):
		dif = input[i+1] - input[i]
		if dif not in difs:
			print("Error - difference too great", input[i], input)
			exit()
		difs[dif] += 1
		dif_list.append(dif)

	return difs, dif_list
	
def calc_num_solutions(dif_list):

	sets_of_ones = []
	sum = 0
	for entry in dif_list:
		if entry == 1:
			sum += 1
		elif entry == 3:
			if sum != 0 and sum != 1:	# if sum is 0 or 1, then this one is immutable - it's a 3 3 or a 3 1 3 so nothing can be skipped
				sets_of_ones.append(sum)
			sum = 0
		else:
			print("Error, saw a dif that was not a 1 or 3.")
			exit()
	#print(sets_of_ones)

	# if dif is 3, it is required.	
	# maybe it makes sense to treat 3s like gates? y. anything before or after a 3 is a separate group
		# checked actual data and I don't have to worry about 2s. bless
	# with 1s, can combine into 2s or 3s, but nothing higher
	
	# If a set contains n elements whith m1 identical elements of a certain kind, m2 identical elements of another kind, m3 identical elements of another kind, ..., and mk identical elements of another kind, the number of permutations is equal to n!/m1! x m2! x m3! x ... x mk!
	# thank u google
	
	# ^ so this is nice but I just realized that the actual dataset I have has no sequences of 1s that are longer than 4
	# so for that I can just hardcode something quick and easy... maybe I will come back to implement something that works more broadly
	# 4 ones is 7 combinations (...)
	# 3 ones is 4 combinations ( 1 1 1 or 2 1 or 1 2 ) 
	# 2 ones is 2 combinations ( 1 1 or 2 )
	
	num_combos = 1
	
	for entry in sets_of_ones:
		if entry == 4:
			num_combos *= 7
		elif entry == 3:
			num_combos *= 4
		elif entry == 2:
			num_combos *= 2
		else:
			print("Error, saw a set of ones > 4.")
			exit()
		
	return num_combos
	
def calc_single_permutation( permutation_set ):	# expects [#1s, #2s, #3s]
	numerator = factorial( sum(permutation_set) )
	denominator = factorial(permutation_set[0]) * factorial(permutation_set[1]) * factorial(permutation_set[2]) 
	return int(numerator/denominator)
	
def calc_permutations(number_of_ones):

	sum = 0
	permutation_set = [ number_of_ones, 0, 0 ]
	# get all combos of 1 and 2
	
	sum += 1	# for initial permutation_set
	
	while (permutation_set[0] > 1):		# get all combos of 1 and 2
		permutation_set[0] -= 2
		permutation_set[1] += 1
		sum += calc_single_permutation(permutation_set)
	
	permutation_set[0] += 2*permutation_set[1] 
	permutation_set[1] = 0
	
	while (permutation_set[0] > 2):		# get all combos of 1 and 3
		permutation_set[0] -= 3
		permutation_set[2] += 1
		sum += calc_single_permutation(permutation_set)
		
	permutation_set[0] += 3*permutation_set[2] 
	permutation_set[2] = 0
	
	while (permutation_set[0] > 1):		# get all combos of 2 and 3 (and leftover 1)
		if (permutation_set[1] > 0):
			permutation_set[0] -= 1
			permutation_set[1] -= 1
			permutation_set[2] += 1
		else:
			permutation_set[0] -= 2
			permutation_set[1] += 1
		if (permutation_set[1] > 0) and (permutation_set[2] > 0):	# if there are both 2 and 3
			sum += calc_single_permutation(permutation_set)
	
	return sum

def thoughts_on_handling_twos():

	# 2s: if preceded by a 1, double the amount of solutions
	# 2s: if followed by a 1, double the amount of solutions [again]
	# maybe treat it as a soft gate - it is basically a 3 but also can set one of the following for each entry in sets_of_ones:
	# preceded_by_two bool and followed_by_two bool
	# BUT when checking permutations, make sure it doubles ONLY THE PERMUTATIONS THAT END/BEGIN WITH ONES
	# this will not be all of them
	return
	
def calc_num_solutions_v2(dif_list):	# here is the nicer more broad version I mentioned! ...it still doesn't handle 2s, though

	sets_of_ones = []
	sum = 0
	for entry in dif_list:
		if entry == 1:
			sum += 1
		elif entry == 3:
			if sum != 0 and sum != 1:	# if sum is 0 or 1, then this one is immutable - it's a 3 3 or a 3 1 3 so nothing can be skipped
				sets_of_ones.append(sum)
			sum = 0
		else:
			print("Error, saw a dif that was not a 1 or 3.")
			exit()
			
	num_combos = 1
	
	for entry in sets_of_ones:
		num_combos *= calc_permutations(entry)
		
	return num_combos

if __name__ == "__main__":

	input = open("input/day10.txt").read().split('\n')[:-1]
	for i in range(len(input)):
		input[i] = int(input[i])
	
	input.sort()
	input.insert(0,0)		# add the charging outlet
	input.append(input[-1] + 3)		# add your device's adapter
	
	difs,dif_list = get_difs(input)
	
	#print(input)
	#print(difs)
	#print(dif_list)
	
	print("Solution to part a:", difs[1]*difs[3])
	print("Solution to part b:", calc_num_solutions_v2(dif_list))