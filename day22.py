#!/usr/bin/python3

COMBAT_GAME_CALLED = 1


def measure_score(cards):
	sum = 0
	i = 1
	
	while i <= len(cards):
		sum += ( i * cards[-i] )
		i += 1
	
	return sum



def play_recursive_combat_game(player_1_cards, player_2_cards):
	global COMBAT_GAME_CALLED
	#print("game", COMBAT_GAME_CALLED)
	previous_rounds_p1 = []
	previous_rounds_p2 = []
	COMBAT_GAME_CALLED += 1
	
	print(COMBAT_GAME_CALLED,end="\r") # at least with my input it takes 15311 recursive games total
	
	while ( len(player_1_cards) > 0 and len(player_2_cards) > 0):
				

		for i in range(len(previous_rounds_p1)):
			if player_1_cards == previous_rounds_p1[i] and player_2_cards == previous_rounds_p2[i]:
				#print("DUPLICATE ROUND")
				return 1
		previous_rounds_p1.append(player_1_cards.copy())
		previous_rounds_p2.append(player_2_cards.copy())
		
		p1_card = player_1_cards.pop(0)
		p2_card = player_2_cards.pop(0)
		
		
		
		
	# if both players have at least as many cards in their own decks as the number on the card they just dealt,
	# the winner of the round is determined by recursing into a sub-game of Recursive Combat
		
		if len(player_1_cards) >= p1_card and len(player_2_cards) >= p2_card:
			round_victor = play_recursive_combat_game(player_1_cards.copy()[:p1_card], player_2_cards.copy()[:p2_card])
		else:
			if p1_card > p2_card:
				#print("Winner of round is 1")
				round_victor = 1
			elif p2_card > p1_card:
				#print("Winner of round is 2")
				round_victor = 2

		if round_victor == 1:
			player_1_cards.append(p1_card)
			player_1_cards.append(p2_card)
		elif round_victor == 2:
			player_2_cards.append(p2_card)
			player_2_cards.append(p1_card)
		else:
			print("???")
			exit()
			
					
		if len(player_1_cards) == 0 or len(player_2_cards) == 0:
			break
	
	if len(player_1_cards) == 0:
		winner = 2
	else:
		winner = 1
		
		
	
	#print(player_2_cards)
	
	return winner

	

if __name__ == "__main__":
	
	data = open("input/day22.txt").read()[:-1].split("\n\n")
	player_1_cards = [int(card) for card in data[0].split("\n")[1:] ]
	player_2_cards = [int(card) for card in data[1].split("\n")[1:] ]
	
	#print(player_1_cards, player_2_cards)
	
	while ( len(player_1_cards) > 0 and len(player_2_cards) > 0):
		p1_card = player_1_cards.pop(0)
		p2_card = player_2_cards.pop(0)
		
		if p1_card > p2_card:
			player_1_cards.extend([p1_card, p2_card])
		else:
			player_2_cards.extend([p2_card, p1_card])
			
	
	winning_score = 0
	if len(player_1_cards) == 0:
		winning_score = measure_score(player_2_cards)
	else:
		winning_score = measure_score(player_1_cards)
	
	print("Solution to part a is:", winning_score)
	
	
	
	player_1_cards = [int(card) for card in data[0].split("\n")[1:] ]
	player_2_cards = [int(card) for card in data[1].split("\n")[1:] ]
	
	winner = play_recursive_combat_game(player_1_cards, player_2_cards)
	
	if winner == 1:
		winning_score = measure_score(player_1_cards)
	else:
		winning_score = measure_score(player_2_cards)
		
	
	#print()
	
	print("Solution to part b is:", winning_score)
	