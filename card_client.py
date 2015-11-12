#! usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import string
import sys


def prompt():
	sys.stdout.write('%s> ' % name)
	sys.stdout.flush()


if __name__ == '__main__':

	Host = ''
	Port = 8888

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((Host, Port))
	except:
		print 'Unable to connect'
		sys.exit()

	print 'Connected to remote host. Enter your name.'
	name = raw_input('> ')
	s.send(name)
	print 'Start bidding'
	prompt()

	while 1:
		socket_list = [sys.stdin, s]

		r_s, w_s, err_s = select.select(socket_list, [], [])

		for sock in r_s:
			if sock == s:
				data = sock.recv(4096)
				if not data:
					print '\nDisconnected from chat server'
					sys.exit()
				else:
					sys.stdout.write(data)
					prompt()
			else:
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()