#! /usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored

class Card(object):

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		self.card = self.value + self.suit

	def template(self, mult=13):
		if self.card[0] != '1' and len(self.card) <= 2:
			self.card = ' ' + self.card
		top_line =				'⎧' + '‾' * mult + '⎫\n'
		left_side_mark_line =	'⎪ ' + self.card + ' ' * 9 + '⎪\n'
		empty_line =			('⎪' + ' ' * mult + '⎪\n') * 3
		centr_mark_line =		'⎪'+ ' ' * 5 + self.card + ' ' * 5 + '⎪\n'
		right_side_mark_line =	'⎪' + ' ' * 9 + self.card + ' ⎪\n'
		botton_line =			'⎩' + '_' * mult + '⎭\n'
		template = (top_line +
					left_side_mark_line +
					empty_line +
					centr_mark_line +
					empty_line +
					right_side_mark_line +
					botton_line)
		return template

	def show(self):
		print self.card


class CardSet(Card):

	def __init__(self, args):
		self.args = args

	def send_cards(self):
		output_str = ''
		for card in self.args:
			output_card = card[0] + card[1] + ' '
			output_str += str(output_card)
		return output_str

	def receive_cards(self, input_str):
		self.input_str = input_str[:-1]
		output = list(self.input_str.split(' '))
		name = lambda x: x[0] if x[0] != '1' else x[:2]
		suit = lambda x: x[1:] if x[0] != '1' else x[2:]
		output_list = [[name(x), suit(x)] for x in output]
		return output_list

	def __add__(self, card):
		self.args.append(card)
		return CardSet(self.args)

	def __sub__(self, card):
		self.args.remove(card)
		return CardSet(self.args)

	def show(self, card_per_line=7):
		def preparer(template_list):
			template_buffer = []
			for i in range(len(template_list[0])):
				template = [x[i] for x in template_list]
				template_buffer.append(' '.join(template))
			return template_buffer

		print_template = []
		template_list = [list(Card(x[0], x[1]).template().split('\n'))
							for x in self.args]
		if len(template_list) > 8:
			print_template += preparer(template_list[:card_per_line])
			print_template += preparer(template_list[card_per_line:])
		else:
			print_template += preparer(template_list)
		
		for cards in print_template:
			print cards

if __name__ == '__main__':
	names = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	suits = ['♠', '♣', colored('♦', 'red'), colored('♥', 'red')]
	cards_with_suits = [[y, z] for z in suits for y in names]

	z = CardSet(cards_with_suits[:2])
	# print cards_with_suits[0]
	rec = z.send_cards()
	foo = CardSet(rec)
	foo.receive_cards(rec)
	g = z + cards_with_suits[5] 
	g.show()
	h = g + cards_with_suits[9]
	h.show()
	bar = h - cards_with_suits[9]
	bar.show()
	# k = Card('8', '♠')
	# k.show()
	# print k.template()