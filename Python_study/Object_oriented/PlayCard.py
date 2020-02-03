"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
''' 
0:spade
1:heart
2:club
3:diamond
'''
import random

class Card(object):
	def __init__(self,suite,face):
		self.suite = suite
		self.face = face

	def show_face(self):
		suites = ['spade','heart','club','diamond']
		faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
		return f'{suites[self.suite]} {faces[self.face]}'

	def __str__(self):
		return show_face()

class Poker(object):
	def __init__(self):
		self.index = 0
		self.cards = [Card(suite,face) for suite in range(4) for face in range(1,14)]

	def shuffle(self):
		random.shuffle(self.cards)
		self.index = 0

	def deal(self):
		card = self.cards[self.index]
		self.index += 1
		return card
	@property
	def has_more(self):
		return self.index < len(self.card)

class Player(object):

	def __init__(self,name):
		self.name = name
		self.cards = []
	def get_one(self):
		self.cards.append(card)

	def sort(self,comp = lambda card : (card.suite,card.face)):
		self.cards.sort(key = comp)

def main():
	poker = Poker()
	poker.shuffle()
	players = [Player(name) for name in ['zcy','zzq','zsc','fbm']]
	while poker.has_more():
		for player in players:
			player.get_one(poker.deal())
	for player in players:
		player.sort()
		print(player.name,end = ':')
		print(player.cards)

if __name__ == '__main__':
	main()

	



