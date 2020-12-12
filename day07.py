#!/usr/bin/python3

def num_bags_containing_this_colour(bag_dictionary, colour):
	containing_colours = set()
	still_need_to_check = set()
	still_need_to_check.add(colour)

	while (still_need_to_check):
		checking = still_need_to_check.pop()
		if checking not in bag_dictionary:	# doesn't have any "parent" bags
			continue
		for entry in bag_dictionary[checking]:
			containing_colours.add(entry)
			still_need_to_check.add(entry)

	return len(containing_colours)
	

def num_bags_this_contains(bag_dictionary, colour):
	sum_bags = 0
	if colour not in bag_dictionary:
		return 0

	for entry in bag_dictionary[colour]:
		# entry has (colour, num of bags)
		num_bags = entry[1]
		colour_bag = entry[0]
		sum_bags += num_bags * (1 + num_bags_this_contains(bag_dictionary, colour_bag) )

	return sum_bags

if __name__ == "__main__":

	bag_dictionary = {}
	# bag dictionary 1 will contain parents
	
	bag_dictionary_2 = {}
	# bag dictionary 2 will contain children and num of those children

	input = open("input/day07.txt").read().split('\n')
	for line in input:
		if "no other bags" in line or line == '':
			continue
		contains_index = line.find(' bags contain ')
		type_bag = line[:contains_index]
		contents = line[contains_index+len(' bags contain '):-1].split(', ')
		bag_contents = []
		for entry in contents:
			space_index = entry.find(' ')
			num_subbag = int(entry[:space_index])
			if num_subbag == 1:
				type_subbag = entry[space_index+1:-4]
			else:
				type_subbag = entry[space_index+1:-5]
			
			# for part a
			if type_subbag not in bag_dictionary:
				bag_dictionary[type_subbag] = []
			bag_dictionary[type_subbag].append(type_bag)

			# for part b
			bag_contents.append((type_subbag,num_subbag))
			bag_dictionary_2[type_bag] = bag_contents

	
	print("Solution to part a:", num_bags_containing_this_colour(bag_dictionary, 'shiny gold'))
	print("Solution to part b:", num_bags_this_contains(bag_dictionary_2, 'shiny gold'))
	