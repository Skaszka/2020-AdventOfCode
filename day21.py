#!/usr/bin/python3


if __name__ == "__main__":
	
	input = open("input/day21.txt").read().split("\n")[:-1]
	
	allergen_dict = {}
	test = []
	
	# it took me forever to understand but the idea is that if an allergen is listed
	# one of the ingredients IS that allergen
	# so if an allergen is listed and an ingredient is not, that ingredient CANNOT have that allergen
	
	for line in input:
		allergens = []
		try:
			index_contains = line.index(" (contains ")
			ingredients = line[:index_contains].split(" ")
			allergens = line[index_contains+11:-1].split(", ")
			#print(line[index_contains+11:-1])
			#print(allergens)
		except:
			ingredients = line.split(" ")
		
		for allergen in allergens:
			if allergen not in allergen_dict:
				allergen_dict[allergen] = ingredients.copy()
			else:
				temp = [x for x in allergen_dict[allergen] if x in ingredients.copy()]
				allergen_dict[allergen] = temp
				
	print(allergen_dict)
	
	temp_allergen_set = set()
	
	for allergen in allergen_dict:
		for entry in allergen_dict[allergen]:
			temp_allergen_set.add(entry)
	
	sum = 0
	for line in input:
		index_contains = line.index(" (contains ")
		ingredients = line[:index_contains].split(" ")
		for ingredient in ingredients:
			if ingredient not in temp_allergen_set:
				sum += 1	
	
	print("Solution to part a is:", sum)
	
	final_allergen_dict = {}	
	
	while(allergen_dict):
		keys = [key for key in allergen_dict]
		temp_val = ""
		for key in keys:
			if len(allergen_dict[key]) == 1:
				temp_val = allergen_dict.pop(key)[0]
				final_allergen_dict[key] = temp_val
				break
		for allergen in allergen_dict:
			if temp_val in allergen_dict[allergen]:
				allergen_dict[allergen].remove(temp_val)
			
	#print(final_allergen_dict)
	keys = [key for key in final_allergen_dict]
	keys.sort()
	
	print("Solution to part b is:", ",".join([final_allergen_dict[key] for key in keys]))
	