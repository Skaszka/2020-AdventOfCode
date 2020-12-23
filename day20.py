#!/usr/bin/python3

from math import sqrt

def find_edge_pieces(tiles):
	edge_dict = {}
	edges = []
	corners = []
	
	for tile in tiles:
		tile_edges = tiles[tile][0]
		for entry in tile_edges:
			if entry in edge_dict:
				edge_dict[entry] += 1
			elif entry[::-1] in edge_dict:
				edge_dict[entry[::-1]] += 1
			else:
				edge_dict[entry] = 1
	
	for tile in tiles:
		sum_for_tile = 0
		tile_edges = tiles[tile][0]
		for entry in tile_edges:
			if entry in edge_dict and edge_dict[entry] == 1:
				sum_for_tile += 1
			elif entry[::-1] in edge_dict and edge_dict[entry[::-1]] == 1:
				sum_for_tile += 1
			elif entry not in edge_dict and entry[::-1] not in edge_dict:
				print("Something went extra wrong.")
		if sum_for_tile == 2:
			corners.append(tile)
		elif sum_for_tile == 1:
			edges.append(tile)
		elif sum_for_tile != 0:
			print("Something went wrong.")
			
	return (corners, edges, edge_dict)

def find_opposite_edge(edges, matching_edge):
	for i in range(4):
		if edges[i] == matching_edge:
			return edges[(i+2)%4]
		elif edges[i] == matching_edge[::-1]:
			return edges[(i+2)%4][::-1]
	print("Something went wrong.")
	return False

def find_right_edge_from_top(edges, matching_edge):
	for i in range(4):
		if edges[i] == matching_edge:
			return edges[(i+1)%4]
		elif edges[i] == matching_edge[::-1]:
			return edges[(i-1)%4]
	print("Something went wrong.")
	return False
	return

def build_first_line(tiles, corner_tiles, edge_tiles, edge_dict, side_len):
	first_line = []
	
	chosen_corner = tiles[corner_tiles[0]]
	first_line.append(corner_tiles[0])
	
	opposite_edge = ""
	
	corners_edges = chosen_corner[0]
	indices = []
	for i in range(4):
		if corners_edges[i] in edge_dict and edge_dict[corners_edges[i]] == 1:
			indices.append(i)
			indices.append(" ")
		elif corners_edges[i][::-1] in edge_dict and edge_dict[corners_edges[i][::-1]] == 1:
			indices.append(i)
			indices.append("r")
			
	
	if indices == [0,' ',3,' ']:
		opposite_edge = find_opposite_edge(corners_edges, corners_edges[3])
		bottom_corner_edge = corners_edges[2]
	else:
		print("Failing for different configuration. I'm cheesing this to save time... rip")
		exit()
			
	#print(opposite_edge)
	
	while( len(first_line) < side_len - 1 ):
		if len(first_line) > 1:
			edge_tiles.remove(first_line[-1])
		
		go_to_next_entry = False
		for edge_tile in edge_tiles:
			tiles_edges = tiles[edge_tile][0]
			for edge in tiles_edges:
				if edge == opposite_edge:
					go_to_next_entry = True
					first_line.append(edge_tile)
					opposite_edge = find_opposite_edge(tiles_edges, edge)
					break
				elif edge[::-1] == opposite_edge:
					go_to_next_entry = True
					first_line.append(edge_tile)
					opposite_edge = find_opposite_edge(tiles_edges, edge[::-1])
					break
			if go_to_next_entry:
				break
	corner_tiles.remove(first_line[0])
	
	for corner_tile in corner_tiles:
		tiles_edges = tiles[corner_tile][0]
		for edge in tiles_edges:
				if edge == opposite_edge:
					first_line.append(corner_tile)
					break
				elif edge[::-1] == opposite_edge:
					first_line.append(corner_tile)
					break
					
	corner_tiles.remove(first_line[-1])
	
	#print(first_line)
	
	return first_line, bottom_corner_edge
		

	
# TODO: FOR THIS TO WORK I need to actually start flipping/rotating in tiles while I'm working with these... ugh
	
	
if __name__ == "__main__":
	
	input = open("input/day20.txt").read().split("\n\n")[:-1]
	
	tiles = {}
	
	for entry in input:
		tile = entry.split("\n")
		tile_num = int(tile[0][5:-1])
		tile_contents = tile[1:]
		tile_edges = []
		tile_edges.append(tile_contents[0])
		right = ""
		left = ""
		for content in tile_contents:
			right += content[-1:]
			left += content[0]
		tile_edges.append(right)
		tile_edges.append(tile_contents[-1][::-1])
		tile_edges.append(left[::-1])
		
		tiles[tile_num] = (tile_edges, tile_contents)
	
	#print(tiles)
	side_len = int(sqrt(len(tiles)))
	#print(side_len)
	
	corner_tiles, edge_tiles, edge_dict = find_edge_pieces(tiles)
	middle_tiles = [tile for tile in tiles if (tile not in corner_tiles and tile not in edge_tiles)]
	#print(middle_tiles)
	
	#print(corner_tiles)
	#print(edge_tiles)
	
	product = 1
	for corner in corner_tiles:
		product *= corner
	
	print("Solution to part a is:", product)
	
	constructed_image = []
	
	first_line, bottom_corner_edge = build_first_line(tiles, corner_tiles, edge_tiles, edge_dict, side_len)
	constructed_image.append(first_line)
	
	print(first_line)
	
	while( len(constructed_image) < side_len - 1):
		print(bottom_corner_edge)
		current_line = []
		opposite_edge = ""
		
		for edge_tile in edge_tiles:
			edge_found = False
			tiles_edges = tiles[edge_tile][0]
			for edge in tiles_edges:
					if edge == bottom_corner_edge:
						current_line.append(edge_tile)
						opposite_edge = find_right_edge_from_top(tiles_edges, edge)
						bottom_corner_edge = find_right_edge_from_top(tiles_edges, opposite_edge)
						edge_found = True
						break
					elif edge[::-1] == bottom_corner_edge:
						current_line.append(edge_tile)
						opposite_edge = find_right_edge_from_top(tiles_edges, edge)
						bottom_corner_edge = find_right_edge_from_top(tiles_edges, opposite_edge)
						edge_found = True
						break
			if edge_found:
				break
		edge_tiles.remove(current_line[0])
		
		while( len(current_line) < side_len - 1):
			if len(current_line) > 1:
				middle_tiles.remove(current_line[-1])
			go_to_next_entry = False
			for middle_tile in middle_tiles:
				#print(middle_tile)
				tiles_edges = tiles[middle_tile][0]
				for edge in tiles_edges:
					if edge == opposite_edge:
						go_to_next_entry = True
						current_line.append(middle_tile)
						opposite_edge = find_opposite_edge(tiles_edges, edge)
						break
					elif edge[::-1] == opposite_edge:
						go_to_next_entry = True
						current_line.append(middle_tile)
						opposite_edge = find_opposite_edge(tiles_edges, edge[::-1])
						break
				if go_to_next_entry:
					break
			
		for edge_tile in edge_tiles:
			tiles_edges = tiles[edge_tile][0]
			for edge in tiles_edges:
					if edge == opposite_edge:
						current_line.append(edge_tile)
						break
					elif edge[::-1] == opposite_edge:
						current_line.append(edge_tile)
						break

		edge_tiles.remove(current_line[-1])
		
		print(current_line)
		constructed_image.append(current_line)
		
	#print(corner_tiles)
	
	for line in constructed_image:
		print(line)
	
	
	print("Solution to part b is:", 0)
	