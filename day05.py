#!/usr/bin/python3

input = open("input/day05.txt")

def find_seat(seat_record):
	# [0] is current position, [1] is next change
	row = [0,64]	# to make the math easier; will subtract one at the end
	col = [0,4]
	
	for char in seat_record[:7]:
		if char=='F':
			pass
		elif char=='B':
			row[0] += row[1]
		row[1] /= 2
			
	for char in seat_record[7:]:
		if char=='L':
			pass
		elif char=='R':
			col[0] += col[1]
		col[1] /= 2
			
	return (row[0],col[0])

def get_seat_id(row, column):
	return int(row*8 + column)
	
if __name__ == "__main__":
	max_seat_id = 0
	
	seats = []
	
	for line in input:
		row, column = find_seat(line[:-1])
		seat_id = get_seat_id(row, column)
		seats.append(seat_id)
		if seat_id > max_seat_id:
			max_seat_id = seat_id
			
	print("Solution to part a:", max_seat_id )
	seats.sort()
	
	for i in range(len(seats)):
		if seats[i]+1 != seats[i+1]:
			print("Solution to part b:", seats[i]+1 )
			break