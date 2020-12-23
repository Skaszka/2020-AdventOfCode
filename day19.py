#!/usr/bin/python3

def interpret_rule(rules, rule_key):
	rule = rules[rule_key]
	final_possible_messages = []
	possible_messages = [""]
	
	
	#print(rule)
	
	if rule[0] == '"':
		return( [ rule[1:-1] ] )
	else:
		tokens = rule.split(" ")
		#print(tokens)
		for token in tokens:
			if token != "|":
				returned_msg = interpret_rule(rules, token)
				temp_messages = []
				for new_suffix in returned_msg:
					for prefix in possible_messages:
						temp_messages.append(prefix + new_suffix)
				possible_messages = temp_messages
			else:
				final_possible_messages.extend(possible_messages)
				possible_messages = [""]
	
	final_possible_messages.extend(possible_messages)
	return final_possible_messages

def test_against_rule(rules, rule_key, message):
	return
	

if __name__ == "__main__":
	
	input = open("input/day19.txt").read().split("\n\n")
	rules = {}
	for entry in input[0].split("\n"):
		colon_index = entry.find(":")
		key = entry[:colon_index]
		value = entry[colon_index+2:]
		rules[key] = value
	messages = input[1].split("\n")[:-1]
	
	#print(rules)
	#print(messages)

	sum = 0
	
	# definitely not the most efficient way to do it, but eh
	temp_set = set(interpret_rule(rules, "0"))
	for entry in messages:
		if entry in temp_set:
			sum += 1	
	
	print("Solution to part a is:", sum)
	
	#print(rules["0"])
	# rules 0 = 8 11
	
	rules["8"] = "42 | 42 8"
	rules["11"] = "42 31 | 42 11 31"
	
	set_42 = set(interpret_rule(rules, "42"))
	set_31 = set(interpret_rule(rules, "31"))
	#print(set_42)	# all entries here are the same length: 8
	#print()
	#print(set_31)	# all entries here are the same length: 8
	
	# since rules 0 is 8 11
	# and rule 8 is 42 | 42 8 - aka, 42 repeating
	# and rule 11 is 42 31 | 42 11 31 - aka, 42 repeating followed by 31 repeating ( expand in option 2)
	# minimum valid entry is "42 42 31"
	
	# all we need to do, for every entry in messages, slice into substrings of len 8
	# first two substrings must be in 42
	# last substring must be in 31
	# all in between must be in 42 or 31, but once there is a 31, no more 42s
	
	#... wait, also, for every 31, must be another 42
	# so there must be AT LEAST one more 42 than 31 total
	
	element = set_42.pop()
	length_substring = len(element)
	set_42.add(element)
	sum = 0
	j = 0
	
	
	for message in messages:
		#print(j,end="\r")
		temp_message = [ message[i:i+length_substring] for i in range(0, len(message), length_substring) ]
		#print(temp_message)
		
		if temp_message[0] not in set_42 or temp_message[1] not in set_42 or temp_message[-1] not in set_31:
			continue
		
		match = True
		num_42s = 0
		num_31s = 0
		i = 1	# skipping the first 42 match
		while(i<len(temp_message)):
			if temp_message[i] not in set_42:
				break
			i+=1
			num_42s += 1
		if (i>=len(temp_message)):
			match = False
		while(i<len(temp_message)):
			if temp_message[i] not in set_31:
				match = False
				break
			i+=1
			num_31s += 1
			
		if match and num_42s >= num_31s:
			sum += 1
	
	
	#for message in messages:
	#	test_against
	
	print("Solution to part b is:", sum)
	