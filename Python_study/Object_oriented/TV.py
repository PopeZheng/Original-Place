class TV(object):
	def __init__(self,channel=1,volumeLevel=10,on=False):
		self._channel = channel
		self._volumeLevel = volumeLevel
		self._on = on

	def turn_on(self):
		self._on = True
	def turn_off(self):
		self._on = False

	@property
	def get_channel(self):
		return self._channel
	@channel.setter
	def set_channel(self,channel):
		self._channel = channel

	@property
	def get_volume(self):
		return self._volume
	@volume.setter
	def set_volume(self,volume):
		self._volume = volume

	def channel_up(self):
		if self._on:
			self._channel += 1
		else:
			print('sb')

	def channel_dowm(self):
		if self._on:
			self._channel -= 1
		else:
			print('sb')


	
