# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import socket
from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import urlopen

class InternetChecker(object):
	def __init__(self):
		pass

	def test_internet(self, url):
		try:
			data = urlopen(url, timeout=5)
		except: # URLError:
			return False

		host = data.fp.raw._sock.getpeername()
		url = 'http://' + (host[0] if len(host) == 2 else
				socket.gethostbyname(urlparse(data.geturl()).hostname))
		return True
