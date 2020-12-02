#!/usr/bin/python3

input = open("input/day01.txt")

expense_report = []

for line in input:
	expense_report.append(int(line))

expense_report.sort()
expense_report_b = expense_report.copy()

low = 0
high = 0

while expense_report:
	low = expense_report.pop(0)
	if low*2>2020:
		print("Error: hit over 2020")
		exit()
	for entry in expense_report:
		if low+entry==2020:
			high = entry
			break
	if high!=0:
		break
			
print("Solution to part a:",low*high)

# For part 2, since expense_report_b is sorted...
# For any collection where low*3 is > 2020, there can't be a success.
# Also, for any collection where low + mid*2 is > 2020, there can't be a success
# (And ofc, low + mid + high can't be > 2020)

for i in range(len(expense_report_b)):
	if expense_report_b[i]*3 > 2020:
		print("Error: hit over 2020")
		exit()
	for j in range(len(expense_report_b[i:])):
		if expense_report_b[i] + expense_report_b[j]*2 > 2020:
			break
		for k in range(len(expense_report_b[j:])):
			if expense_report_b[i] + expense_report_b[j] + expense_report_b[k] > 2020:
				break
			elif expense_report_b[i] + expense_report_b[j] + expense_report_b[k] == 2020:
				print("Solution to part b:",expense_report_b[i]*expense_report_b[j]*expense_report_b[k])
				exit()
				
			
