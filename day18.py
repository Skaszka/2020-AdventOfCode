#!/usr/bin/python3

def evaluate_statement(statement):
	# if you encounter a paren, then keep going forward, counting up 
	# for each paren and down for each close, until back to 0. 
	# recursively evaluate that substring
	
	evaluated_num = 0
	paren_depth = 0
	current_operator = ""
	
	i = 0
	
	while (i<len(statement)):
		token = statement[i]
		if token == "(":
			paren_depth += 1
			end_index = 0
			for j in range(i+1, len(statement)):
				if statement[j] == "(":
					paren_depth += 1
				elif statement[j] == ")":
					paren_depth -= 1
				if paren_depth == 0:
					
					if current_operator == "*":
						evaluated_num *= evaluate_statement(statement[i+1:j])
					elif current_operator in ["","+"]:
						evaluated_num += evaluate_statement(statement[i+1:j])
					
					i = j
					break
		elif token in ["+","*"]:
			current_operator = token
		else:
			if current_operator == "*":
		   		evaluated_num *= int(token)
			elif current_operator in ["","+"]:
		   		evaluated_num += int(token)
		i+=1

	return(evaluated_num)

def evaluate_statement_v2(statement):
	
	evaluated_num = 1
	paren_depth = 0
	current_operator = ""
	
	temp_num = 0
	first_pass = []
	
	# for +, evaluate immediately
	# for *, stop, push temp num to first pass, push *, then move on
	
	i = 0
	
	while (i<len(statement)):
		token = statement[i]
		if token == "(":
			paren_depth += 1
			end_index = 0
			for j in range(i+1, len(statement)):
				if statement[j] == "(":
					paren_depth += 1
				elif statement[j] == ")":
					paren_depth -= 1
				if paren_depth == 0:
					
					if current_operator == "*":
						first_pass.append(temp_num)
						temp_num = evaluate_statement_v2(statement[i+1:j])
					elif current_operator in ["","+"]:
						temp_num += evaluate_statement_v2(statement[i+1:j])
					
					i = j
					break
		elif token in ["+","*"]:
			current_operator = token
		else:
			if current_operator == "*":
				first_pass.append(temp_num)
				temp_num = int(token)
			elif current_operator in ["","+"]:
		   		temp_num += int(token)
		i+=1
	
	first_pass.append(temp_num)
	#print(first_pass)
	
	for entry in first_pass:
		evaluated_num *= entry
	
	return(evaluated_num)
	
	

if __name__ == "__main__":
	
	input = open("input/day18.txt").read().split("\n")[:-1]
	
	sum = 0
	sum_v2 = 0
	
	for entry in input:
		statement = [char for char in entry if char !=" "]
		sum += evaluate_statement(statement)
		
	print("Solution to part a is:", sum)
	
	for entry in input:
		statement = [char for char in entry if char !=" "]
		sum_v2 += evaluate_statement_v2(statement)
	
	print("Solution to part b is:", sum_v2)
	