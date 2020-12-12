#!/usr/bin/python3

def run_instruction(instruction, instruction_pointer, accumulator):
	instruction = instruction.split(" ")

	if "nop" == instruction[0]:
		instruction_pointer += 1
	elif "acc" == instruction[0]:
		accumulator += int(instruction[1])
		instruction_pointer += 1
	elif "jmp" == instruction[0]:
		instruction_pointer += int(instruction[1])
	else:
		print("Something went wrong.\nInstruction was", instruction[0])
		exit()

	#print("Ran", instruction, "... acc =", accumulator)
	return (instruction_pointer, accumulator)

def flip_instruction(instructions, i):
	if "nop" in instructions[i][0]:
		instructions[i][0] = instructions[i][0].replace("nop", "jmp")
	elif "jmp" in instructions[i][0]:
		instructions[i][0] = instructions[i][0].replace("jmp", "nop")
	else:
		print("Something went wrong.\nTried to flip", instructions[i][0])
		exit()

if __name__ == "__main__":

	instructions = []
	flippable = set()

	input = open("input/day08.txt").read().split('\n')
	i = 0
	for line in input:
		instructions.append([line, 0])
		if "nop" in line or "jmp" in line:
			flippable.add(i)
		i += 1

	instruction_pointer = 0
	accumulator = 0

	while(True):
		try:
			if instructions[instruction_pointer][1] != 0:	# we've seen this instruction before
				break
			else:
				instructions[instruction_pointer][1] = 1
				instruction_pointer, accumulator = run_instruction(instructions[instruction_pointer][0], instruction_pointer, accumulator)
		except:
			print("Failed to run instruction at", instruction_pointer)
			exit()
			
	print("Solution to part a:", accumulator)

	for i in flippable:		# this loop attempts to change an instruction

		for instruction in instructions:	# reset "already ran this instruction" markers
			instruction[1] = 0

		flip_instruction(instructions, i)

		instruction_pointer = 0
		accumulator = 0

		while(True):		# while this actually runs the resulting code
			try:
				if instruction_pointer >= len(instructions):		# we've changed the broken instruction successfully!
					break
				if instructions[instruction_pointer][1] != 0:	# we've seen this instruction before - this one was the wrong one to change
					break
				else:
					instructions[instruction_pointer][1] = 1
					instruction_pointer, accumulator = run_instruction(instructions[instruction_pointer][0], instruction_pointer, accumulator)
			except:
				print("Failed to run instruction at", instruction_pointer)
				exit()

		if instruction_pointer >= len(instructions):	# need another exit for this outer loop
			break

		flip_instruction(instructions, i)	# change this back

	print("Solution to part b:", accumulator)
	#1548 is too high
	