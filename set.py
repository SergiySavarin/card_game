#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

from termcolor import colored


def computer_choice_helper(player2, card_buffer1, card_buffer2, high_val, low_val):

	for i in player2:
		if high_val > i > low_val:
			card_buffer1.append(i)
		else:
			card_buffer2.append(i)
	card_buffer1.sort()
	card_buffer2.sort()
	if len(card_buffer1) == 0:
		return card_buffer2[0]
	else:
		return card_buffer1[-1]

def computer_choice1(inpt, player2):
	card_buffer1 = []
	card_buffer2 = []
	if player1[inpt] > 100:
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
	elif 19 > player1[inpt] > 10:
		return computer_choice_helper(player2, card_buffer1, card_buffer2, 19, 10)
	elif 29 > player1[inpt] > 20:
		return computer_choice_helper(player2, card_buffer1, card_buffer2, 29, 20)
	elif 39 > player1[inpt] > 30:
		return computer_choice_helper(player2, card_buffer1, card_buffer2, 39, 30)
	elif 49 > player1[inpt] > 40:
		return computer_choice_helper(player2, card_buffer1, card_buffer2, 49, 40)


def computer_choice2(player2):
	card_buffer = []
	for i in player2:
		if i > 100:
			card_buffer.append(i)
		else:
			card_buffer.append(i)
	card_buffer.sort()
	return card_buffer[-1]


def card_template(card, index):
	if card[0] == '1':
		card = card + ' '
	elif len(card) == 23:
		card = card + ' '
	else:
		card = ' ' + card + ' '
	if int(index) < 10:
		index = index + ' '
	template = '⎧‾‾‾‾‾‾‾‾‾‾‾‾‾⎫\n' \
				'⎪ ' + card + '        ⎪\n' \
				'⎪             ⎪\n' \
				'⎪             ⎪\n' \
				'⎪             ⎪\n' \
				'⎪     ' + card + '    ⎪\n' \
				'⎪             ⎪\n' \
				'⎪             ⎪\n' \
				'⎪             ⎪\n' \
				'⎪         ' + card + '⎪\n' \
				'⎩_____________⎭\n' \
				'       ' + index + '      \n' \

	return template


def print_card_template(player):
	lines = []
	for card in player:
		ind = str(player.index(card) + 1)
		s = str(card)
		if s[0] == '3' or s[0] == '4':
			card = colored(cards[int(s[1]) - 1], 'red') + card_suit[int(s[0]) - 1]
		else:
			card = cards[int(s[1]) - 1] + card_suit[int(s[0]) - 1]
		lines.append(card_template(card, ind))
		if len(lines) == 8:
			for index in range(len(card_template(card, ind).split('\n')) - 1):
				line_line = ''
				for line in lines:
					line_line += line.split('\n')[index]
				print line_line
			lines = []
	if len(lines) != 0:
		for index in range(len(card_template(card, ind).split('\n')) - 1):
			line_line = ''
			for line in lines:
				line_line += line.split('\n')[index]
			print line_line
		lines = []


def input_func_choice():
	while True:
		check = True
		try: 
			inpt = int(raw_input('Choice card, which you give to your friend: ')) - 1
		except ValueError: 
			check = False
			continue
		if check and (int(inpt) in range(len(player_1))):
			break
		else:
			continue
	return inpt


def input_func():
	while True:
		check = True
		try: 
			inpt = int(raw_input('Choice your card: ')) - 1
		except ValueError: 
			check = False
			continue
		if check and (int(inpt) in range(len(player1))):
			break
		else:
			continue
	return inpt

def score_counter(score):
	result = 0
	for i in score:
		if i < 100:
			result += i
		else:
			i = i / 10
			result += i
	return result


def score_adder(player1, player2, inpt1, inpt2, score_p1, score_p2):
	if player1[inpt1] > inpt2[0]:
		score_p1.append(player1[inpt1])
		score_p1.append(inpt2[0])
		del player1[inpt1]
		player2.remove(inpt2[0])
		return player1, player2, score_p1, score_p2
	else:
		score_p2.append(player1[inpt1])
		score_p2.append(inpt2[0])
		del player1[inpt1]
		player2.remove(inpt2[0])
		return player1, player2, score_p1, score_p2


def game_result(score_p1, score_p2):
	if score_p1 > score_p2:
		while True:
			inpt = raw_input('Congratulations! You Win! Play one more? Y/N ').lower()
			if inpt == 'y' or inpt == 'n':
				break
			else:
				continue
		if inpt == 'y':
			return True
		else:
			return False
	else:
		while True:
			inpt = raw_input('You lose! Play one more? Y/N ').lower()
			if inpt == 'y' or inpt == 'n':
				break
			else:
				continue
		if inpt == 'y':
			return True
		else:
			return False


def prerape_cards_and_widows():

	random.shuffle(card_set)

	trump = random.sample(card_set, 1)
	trump = str(trump[0])

	game_trump = card_suit[int(trump[0]) - 1]

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

	return game_set, game_trump, widow1, widow2

def giving_cards(game_set):

	player1 = []
	player2 = []

	for i in range(len(game_set)):
		if i == 0 or i % 2 == 0:
			player1.append(game_set[i])
		else:
			player2.append(game_set[i])

	return player1, player2


def auto_giving_cards(player2, widow1, widow2):

	player_2 = player2 + widow1 + widow2

	for i in range(0,2):
		player_2.sort()
		player_2.remove(player_2[0])
		player1.append(player_2[0])
	
	player2 = player_2

	return player2


card_set = [11, 12, 13, 14, 15, 16, 17, 18, 
			21, 22, 23, 24, 25, 26, 27, 28, 
			31, 32, 33, 34, 35, 36, 37, 38,
			41, 42, 43, 44, 45, 46, 47, 48]

cards = ["7", "8", "9", "10", "J", "Q", "K", "A"]
card_suit = ['♠', '♣', colored('♦', 'red'), colored('♥', 'red')]

game = True

while game:

	choice = random.randint(1, 2)

	if choice == 1:

		game_set, game_trump, widow1, widow2 = prerape_cards_and_widows()

		score_p1 = []
		score_p2 = []

		player1, player2 = giving_cards(game_set)

		os.system('clear')
		print 'You start the game!'
		print 'Your cards plus two widows: ', 'Trump of the game:', game_trump
		player_1 = player1 + widow1 + widow2
		print_card_template(player_1)

		card_buffer = []
		for i in range(0,2):
			inpt = input_func_choice()
			while player_1[int(inpt)] in card_buffer:
				print 'Choose another card, this was given already.'
				inpt = input_func_choice()
			card_buffer.append(player_1[int(inpt)])
			player2.append(player_1[int(inpt)])

		for card in card_buffer:
			player_1.remove(card)
		player1 = player_1

		os.system('clear')
		print 'Let`s start the game!'

		for i in range(8):
			print 'Your cards: ', 'Trump of the game:', game_trump
			print_card_template(player1)

			inpt1 = input_func()
			
			inpt2 = []
			inpt2.append(computer_choice1(inpt1, player2))
			print 'Computer choice: '
			print_card_template(inpt2)

			player1, player2, score_p1, score_p2 = score_adder(
				player1, player2, inpt1, inpt2, score_p1, score_p2)

			os.system('clear')
			print 'Your cards: ', 'Trump of the game:', game_trump
			print_card_template(player1)

			inpt2 = []
			inpt2.append(computer_choice2(player2))
			print 'Computer choice: '
			print_card_template(inpt2)

			inpt1 = input_func()

			player1, player2, score_p1, score_p2 = score_adder(
				player1, player2, inpt1, inpt2, score_p1, score_p2)

		os.system('clear')
		print 'Your scores: ', score_counter(score_p1)
		print 'Computer scores: ', score_counter(score_p2)

		game = game_result(score_counter(score_p1), score_counter(score_p2))

	else:

		game_set, game_trump, widow1, widow2 = prerape_cards_and_widows()

		score_p1 = []
		score_p2 = []

		player1, player2 = giving_cards(game_set)
		
		os.system('clear')
		player2 = auto_giving_cards(player2, widow1, widow2)

		os.system('clear')
		print 'Let`s start the game!'

		for i in range(8):

			print 'Your cards: ', 'Trump of the game:', game_trump
			print_card_template(player1)

			inpt1 = input_func()

			inpt2 = []
			inpt2.append(computer_choice1(inpt1, player2))
			print 'Computer choice: '
			print_card_template(inpt2)

			player1, player2, score_p1, score_p2 = score_adder(
				player1, player2, inpt1, inpt2, score_p1, score_p2)

			os.system('clear')
			print 'Your cards: ', 'Trump of the game:', game_trump
			print_card_template(player1)

			inpt2 = []
			inpt2.append(computer_choice2(player2))
			print 'Computer choice: '
			print_card_template(inpt2)

			inpt1 = input_func()

			player1, player2, score_p1, score_p2 = score_adder(
				player1, player2, inpt1, inpt2, score_p1, score_p2)

		os.system('clear')
		print 'Your scores: ', score_counter(score_p1)
		print 'Computer scores: ', score_counter(score_p2)

		game = game_result(score_counter(score_p1), score_counter(score_p2))

