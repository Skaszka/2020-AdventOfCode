#!/usr/bin/python3

def return_invalid_values(rules, ticket):
	invalid_numbers = []
	
	for entry in ticket:
		valid = False
		for rule in rules:
			if (rule[1] <= entry <= rule[2]) or (rule[3] <= entry <= rule[4]):
				valid = True
				break
		if valid == False:
			invalid_numbers.append(entry)
		
	return invalid_numbers

def return_possible_rules(rules, valid_tickets, index):
	possible_rules = []
	
	for rule in rules:
		valid = True
		for ticket in valid_tickets:
			if not (rule[1] <= ticket[index] <= rule[2]) and not (rule[3] <= ticket[index] <= rule[4]):
				valid = False
				break
		if valid == True:
			possible_rules.append(rule[0])
	
	return possible_rules



def return_finalized_rules(possible_rules):
	finalized_rules = {}
	
	while(possible_rules):
		keys = [key for key in possible_rules]
		for key in keys:
			if len(possible_rules[key]) == 1:
				popped_rule = possible_rules.pop(key)
				finalized_rules[ popped_rule[0] ] = key
				
				for entry in possible_rules:
					if popped_rule[0] in possible_rules[entry]:
						possible_rules[entry].remove(popped_rule[0])
		
	return finalized_rules



if __name__ == "__main__":
	
	input = open("input/day16.txt").read().split("\n\n")
	
	rules = []
	temp_rules = input[0].split("\n")
	#print(temp_rules)
	
	for entry in temp_rules:
		temp_rule = entry.split(":")
		rule_name = temp_rule[0]
		entry = temp_rule[1]
		temp_rule = entry.split(" ")
		numbers_1 = temp_rule[1].split("-")
		numbers_2 = temp_rule[3].split("-")
		rule = [rule_name, int(numbers_1[0]), int(numbers_1[1]), int(numbers_2[0]), int(numbers_2[1])]
		rules.append(rule)
	#print(rules)	
	
	
	your_ticket = [ int(entry) for entry in input[1].split("\n")[1].split(",") ]
	#print(your_ticket)
	
	nearby_tickets = []
	temp_nearby_tickets = [ ticket.split(",") for ticket in input[2].split("\n")[1:-1] ]
	for entry in temp_nearby_tickets:
		nearby_tickets.append( [int(i) for i in entry] )
	#print(nearby_tickets)
	
	invalid_numbers = []
	valid_tickets = []
	
	for ticket in nearby_tickets:
		inval_nums = return_invalid_values(rules, ticket)
		if inval_nums == []:
			valid_tickets.append(ticket)
		else:
			invalid_numbers.extend( inval_nums )
	
	#print(valid_tickets)
	
	possible_rules = {}
	
	for index in range(len(your_ticket)):
		possible_rules[index] = return_possible_rules(rules, valid_tickets, index) 
		
	#print(possible_rules)
	
	finalized_rules = return_finalized_rules(possible_rules)
	#print(finalized_rules)
	
	list_values = []
	for rule in finalized_rules:
		if "departure" in rule:
			list_values.append( your_ticket[ finalized_rules[rule] ] )
	
	product = 1
	for value in list_values:
		product *= value
	
		
	print("Solution to part a is:", sum(invalid_numbers))
	
	print("Solution to part b is:", product)
	