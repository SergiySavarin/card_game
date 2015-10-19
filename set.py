#! /usr/bin/env python

import random
import os
from termcolor import colored

def computer_choice1(inpt, player2):
	card_buffer1 = []
	card_buffer2 = []
	if inpt > 100:
		for i in player2:
			if i > 100:
				card_buffer1.append(i)
			else:
				card_buffer2.append(i)
		card_buffer1.sort()
		card_buffer2.sort()
		if len(card_buffer1) == 0:
			return card_buffer2[0]
		else:
			return card_buffer1[0]
	elif 19 > inpt > 10:
		for i in player2:
			if 19 > i > 10:
				card_buffer1.append(i)
			else:
				card_buffer2.append(i)
		card_buffer1.sort()
		card_buffer2.sort()
		if len(card_buffer1) == 0:
			return card_buffer2[0]
		else:
			return card_buffer1[-1]
	elif 29 > inpt > 20:
		for i in player2:
			if 29 > i > 20:
				card_buffer1.append(i)
			else:
				card_buffer2.append(i)
		card_buffer1.sort()
		card_buffer2.sort()
		if len(card_buffer1) == 0:
			return card_buffer2[0]
		else:
			return card_buffer1[-1]
	elif 39 > inpt > 30:
		for i in player2:
			if 39 > i > 30:
				card_buffer1.append(i)
			else:
				card_buffer2.append(i)
		card_buffer1.sort()
		card_buffer2.sort()
		if len(card_buffer1) == 0:
			return card_buffer2[0]
		else:
			return card_buffer1[-1]
	elif 49 > inpt > 40:
		for i in player2:
			if 49 > i > 40:
				card_buffer1.append(i)
			else:
				card_buffer2.append(i)
		card_buffer1.sort()
		card_buffer2.sort()
		if len(card_buffer1) == 0:
			return card_buffer2[0]
		else:
			return card_buffer1[-1]

def computer_choice2(player2):
	card_buffer = []
	for i in player2:
		if i > 100:
			card_buffer.append(i)
		else:
			card_buffer.append(i)
	card_buffer.sort()
	return card_buffer[-1]

def tip():
	print '/-TIP----------------------------------------------\ ', '\n',\
		  '| First Number:   | Second Number: | Third Number: |', '\n',\
		  '|^^^^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^|', '\n',\
		  '| *', colored('4', 'red'), '-', colored('Hearts;', 'red'), '  | * 8 - Ace;     | *', colored('0', 'blue'), '-', colored('Trump;', 'blue'), ' |', '\n',\
		  '| *', colored('3', 'red'), '-', colored('Diamonds;', 'red'), '| * 7 - King;    |               |', '\n',\
		  '| * 2 - Clubs;    | * 6 - Queen;   |               |', '\n',\
		  '| * 1 - Spades;   | * 5 - Jack;    |               |', '\n',\
		  '|                 | * 4 - 10;      |               |', '\n',\
		  '|                 | * 3 - 9;       |               |', '\n',\
		  '|                 | * 2 - 8;       |               |', '\n',\
		  '|                 | * 1 - 7;       |               |', '\n',\
		  '\--------------------------------------------------/'

def card_shower(player):
	k = 0
	for i in player:
		if 49 > i > 30:
			k += 1
			print colored('|%d|' % i, 'red'),
			if k == 9:
				print
		elif 500 > i > 100:
			k += 1
			print colored('|%d|' % i, 'blue'),
			if k == 9:
				print
		else:
			k += 1
			print '|%d|' % i,
			if k == 9:
				print
	print

card_set = [11, 12, 13, 14, 15, 16, 17, 18, 
			21, 22, 23, 24, 25, 26, 27, 28, 
			31, 32, 33, 34, 35, 36, 37, 38,
			41, 42, 43, 44, 45, 46, 47, 48]

game = True

while game == True:

	choice = random.randint(1, 2)

	if choice == 1:

		random.shuffle(card_set)

		trump = random.sample(card_set, 1)
		trump = str(trump[0])

		# print trump, int(trump[0]) * 10, '\n'

		t = int(trump[0]) * 10

		game_set = []

		for i in card_set:
			if 9 > (i - t) > 0:
				game_set.append(i * 10)
			else:
				game_set.append(i)

		widow1 = random.sample(game_set, 2)

		for i in widow1:
			if i in game_set:
				game_set.remove(i)

		widow2 = random.sample(game_set, 2)

		for i in widow2:
			if i in game_set:
				game_set.remove(i)

		player1 = []
		player2 = []
		score_p1 = []
		score_p2 = []

		for i in range(len(game_set)):
			if i == 0 or i % 2 == 0:
				player1.append(game_set[i])
			else:
				player2.append(game_set[i])
		os.system('clear')
		tip()
		print 'You start the game!'
		print 'Your cards: '
		card_shower(player1)
		print 'Widow 1 and 2: '
		card_shower(widow1)
		card_shower(widow2)		
		player_1 = player1 + widow1 + widow2
		for i in range(0,2):
			while True:
				# import pdb;pdb.set_trace()
				check = True
				try: 
					inpt = int(raw_input('Choice cards to give your friend: '))
				except ValueError: 
					check = False
					continue
				if check and (int(inpt) in player_1):
					break
				else:
					continue
			player_1.remove(inpt)
			player2.append(inpt)
		player1 = player_1
		# print player1, player2
		os.system('clear')
		print 'Let`s start the game!'
		for i in range(8):
			# print i
			tip()
			print 'Your cards: '
			card_shower(player1)
			print 'Your scores: '
			card_shower(score_p1)
			print 'Computer scores: '
			card_shower(score_p2)

			while True:
				inpt1 = input('Choice the card: ')
				if (inpt1 in player1) and isinstance(inpt1, int):
					break
				else:
					continue
			player1.remove(inpt1)
			inpt2 = computer_choice1(inpt1, player2)
			print 'Computer choice: ', inpt2
			player2.remove(inpt2)

			if inpt1 > inpt2:
				score_p1.append(inpt1)
				score_p1.append(inpt2)
			else:
				score_p2.append(inpt1)
				score_p2.append(inpt2)

			os.system('clear')
			tip()
			print 'Your cards: '
			card_shower(player1)
			print 'Your scores: '
			card_shower(score_p1)
			print 'Computer scores: '
			card_shower(score_p2)

			inpt2 = computer_choice2(player2)
			print 'Computer choice: ', inpt2
			player2.remove(inpt2)

			while True:
				inpt1 = input('Choice the card: ')
				if (inpt1 in player1) and isinstance(inpt1, int):
					break
				else:
					continue
			player1.remove(inpt1)

			if inpt1 > inpt2:
				score_p1.append(inpt1)
				score_p1.append(inpt2)
			else:
				score_p2.append(inpt1)
				score_p2.append(inpt2)

			os.system('clear')
		if len(score_p1) > len(score_p2):
			while True:
				inpt = raw_input('Congratulations! You Win! Play one more? Y/N ').lower()
				if inpt == 'y' or inpt == 'n':
					break
				else:
					continue
			if inpt == 'y':
				game = True
			else:
				game = False
		else:
			while True:
				inpt = raw_input('You lose! Play one more? Y/N ').lower()
				if inpt == 'y' or inpt == 'n':
					break
				else:
					continue
			if inpt == 'y':
				game = True
			else:
				game = False

	else:

		random.shuffle(card_set)

		trump = random.sample(card_set, 1)
		trump = str(trump[0])

		# print trump, int(trump[0]) * 10, '\n'

		t = int(trump[0]) * 10

		game_set = []

		for i in card_set:
			if 9 > (i - t) > 0:
				game_set.append(i * 10)
			else:
				game_set.append(i)

		widow1 = random.sample(game_set, 2)

		for i in widow1:
			if i in game_set:
				game_set.remove(i)

		widow2 = random.sample(game_set, 2)

		for i in widow2:
			if i in game_set:
				game_set.remove(i)

		player1 = []
		player2 = []
		score_p1 = []
		score_p2 = []

		for i in range(len(game_set)):
			if i == 0 or i % 2 == 0:
				player1.append(game_set[i])
			else:
				player2.append(game_set[i])

		os.system('clear')
		# tip()
		# print 'You start the game!'
		# print 'Your cards: ', player1
		# print 'Widow 1 and 2: ', widow1, widow2
		player_2 = player2 + widow1 + widow2
		for i in range(0,2):
			player_2.sort()
			player_2.remove(player_2[0])
			player1.append(player_2[0])
		player2 = player_2
		# print player1, player2
		os.system('clear')
		print 'Let`s start the game!'
		for i in range(8):
			# print i
			tip()
			print 'Your cards: '
			card_shower(player1)
			print 'Your scores: '
			card_shower(score_p1)
			print 'Computer scores: '
			card_shower(score_p2)

			while True:
				inpt1 = input('Choice the card: ')
				if (inpt1 in player1) and isinstance(inpt1, int):
					break
				else:
					continue
			player1.remove(inpt1)
			inpt2 = computer_choice1(inpt1, player2)
			print 'Computer choice: ', inpt2
			player2.remove(inpt2)

			if inpt1 > inpt2:
				score_p1.append(inpt1)
				score_p1.append(inpt2)
			else:
				score_p2.append(inpt1)
				score_p2.append(inpt2)

			os.system('clear')
			tip()
			print 'Your cards: '
			card_shower(player1)
			print 'Your scores: '
			card_shower(score_p1)
			print 'Computer scores: '
			card_shower(score_p2)

			inpt2 = computer_choice2(player2)
			print 'Computer choice: ', inpt2
			player2.remove(inpt2)

			while True:
				inpt1 = input('Choice the card: ')
				if (inpt1 in player1) and isinstance(inpt1, int):
					break
				else:
					continue
			player1.remove(inpt1)

			if inpt1 > inpt2:
				score_p1.append(inpt1)
				score_p1.append(inpt2)
			else:
				score_p2.append(inpt1)
				score_p2.append(inpt2)

			os.system('clear')
		if len(score_p1) > len(score_p2):
			while True:
				inpt = raw_input('Congratulations! You Win! Play one more? Y/N ').lower()
				if inpt == 'y' or inpt == 'n':
					break
				else:
					continue
			if inpt == 'y':
				game = True
			else:
				game = False
		else:
			while True:
				inpt = raw_input('You lose! Play one more? Y/N ').lower()
				if inpt == 'y' or inpt == 'n':
					break
				else:
					continue
			if inpt == 'y':
				game = True
			else:
				game = False
