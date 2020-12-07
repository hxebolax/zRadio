from .lib import mpv

class MPVClass:
	def __init__(self):
		self.is_initiated = False

	def inicio(self):
		if not self.is_initiated:
			self.is_initiated = True
			self.player = mpv.MPV(ytdl=True, video=False)

	def volumen(self, valor):
		if not self.is_initiated:
			return
		self.player.volume = valor

	def mute(self, valor):
		if not self.is_initiated:
			return
		self.player.mute = valor

	def stop(self):
		if not self.is_initiated:
			return
		self.player.command('stop')
		self.is_initiated = False

	def play(self, valor):
		if not self.is_initiated:
			return
		self.player.play(valor)
