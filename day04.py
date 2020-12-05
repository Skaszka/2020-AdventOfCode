def validate_single_entry(passport):

	temp_fields = set()
	qualified = True
	for entry in passport:
		field = entry[0:3]
		contents = entry[4:]
		temp_fields.add(field)

		# part b handling
		if qualified:	#if it's already been invalidated, don't bother
			if field=='byr':
				try:
					if int(contents)>2002 or int(contents)<1920:
						qualified = False
				except ValueError:
					qualified = False
			elif field=='iyr':
				try:
					if int(contents)>2020 or int(contents)<2010:
						qualified = False
				except ValueError:
					qualified = False
			elif field=='eyr':
				try:
					if int(contents)>2030 or int(contents)<2020:
						qualified = False
				except ValueError:
					qualified = False
			elif field=='hgt':
				try:
					hght = int(contents[:-2])
					if contents[-2:]=='in':
						if int(hght)>76 or int(hght)<59:
							qualified = False
					elif contents[-2:]=='cm':
						if int(hght)>193 or int(hght)<150:
							qualified = False
					else:
						qualified = False
				except ValueError:
					qualified = False
			elif field=='hcl':
				if contents[:1]!='#' or len(contents[1:])!=6:
					qualified = False
				else:
					for char in contents[1:]:
						if char not in '0123456789abcdef':
							qualified=False			
			elif field=='ecl':
				if contents not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
					qualified = False
			elif field=='pid':
				if len(contents)!=9:
					qualified = False
				else:
					for char in contents:
						if char not in '0123456789':
							qualified=False

	contains_all_reqs = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}.issubset(temp_fields)
		
	return(contains_all_reqs, qualified)


if __name__ == "__main__":

	input = open("input/day04.txt")
	
	passports = []
	single_pass = []
	
	sum_valid_a = 0
	sum_valid_b = 0

	for line in input:
		if line=='\n':
			single_pass.sort()
			passports.append(single_pass.copy())
			returned = validate_single_entry(single_pass)
			if returned[0]:
				sum_valid_a+=1
			if returned[0] and returned[1]:
				sum_valid_b+=1
			single_pass = []
		else:
			single_pass.extend(line[:-1].split(" "))
	if single_pass != []:		# to catch the very last one
		single_pass.sort()
		passports.append(single_pass.copy())
		returned = validate_single_entry(single_pass)
		if returned[0]:
			sum_valid_a+=1
		if returned[0] and returned[1]:
			sum_valid_b+=1
		
	
	print("Solution to part a:", sum_valid_a )
	print("Solution to part b:", sum_valid_b )	
	# in the end we didn't actually need to store everything in passports... I coded that in just in case for part b
	
