#! /usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import random

from termcolor import colored


def broadcast_data(sock, message):
	for socket in ConnectionList:
		if socket != s and socket != sock:
			try:
				socket.send(message)
			except:
				socket.close()
				ConnectionList.remove(socket)

def prepare_card_set():
	card_value = [11, 12, 13, 14, 15, 16, 17, 18, 
				21, 22, 23, 24, 25, 26, 27, 28, 
				31, 32, 33, 34, 35, 36, 37, 38,
				41, 42, 43, 44, 45, 46, 47, 48]

	cards = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	card_suit = ['♠', '♣', colored('♦', 'red'), colored('♥', 'red')]

	cards_with_suits = [y + z for z in card_suit for y in cards]
	card_set = {x: t[card_set.index(x)] 
				for x in card_set for k in cards_with_suits}


if __name__ == '__main__':

	PlayersNames = {}
	ConnectionList = []
	CardSet = [1, 2, 3, 4, 5, 6, 7, 8]
	Recv_Buffer = 4096
	Port = 8888

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', Port))
	s.listen(10)

	ConnectionList.append(s)

	print 'Card server started on port: ' + str(Port)


	while 1:
		r_s, w_s, err_s = select.select(ConnectionList, [], [])
		
		for sock in r_s:
			if sock == s:
				sockfd, addr = s.accept()
				ConnectionList.append(sockfd)
				print 'Player (%s, %s) connected' % addr

			elif sock not in PlayersNames:
				name = sock.recv(Recv_Buffer)
				PlayersNames[sock] = name

			else:
				PlayersCards = {x:CardSet for x in PlayersNames}
				broadcast_data(sock, '\rOn the game ' + str(PlayersNames.values()) + '\n')
				broadcast_data(sock, '\rPlayer cards ' + str(PlayersCards[sock]) + '\n')
				try:
					data = sock.recv(Recv_Buffer)
					if data:
						broadcast_data(sock, '\r' + '<' + str(PlayersNames[sock]) + '> ' + data)
				except:
					broadcast_data(sock, '\nPlayer %s (%s, %s) is offline\n' % (PlayersNames[sock], addr[0], addr[1]))
					print 'Player (%s, %s) is offline' % addr
					sock.close()
					ConnectionList.remove(sock)
					del PlayersNames[sock]
					continue
	s.close()