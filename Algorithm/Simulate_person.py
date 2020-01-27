import random
import turtle

class Live():
	def __init__(self,year=0,day=0,hour=0,mintue=0,second=0):
		self.hour = hour
		self.mintue = mintue
		self.second = second
		self._year = year
		self.day = day

	@property
	def get_year(self):
		return self._year
	

	def live(self):
		isrun = True
		while isrun:
			self.second += 1
			if self.second == 60:
				self.second = 0
				self.mintue += 1
				if self.mintue == 60:
					self.mintue = 0
					self.hour += 1
					if self.hour == 24:
						self.hour = 0
						self.day += 1
						if self.day == 365:
							self.day = 0
							self._year += 1

			if self._year >= 100:
				x = random.randint(1,10)
				if x >= 1:
					isrun = False
			elif self._year in range(90,100):
				x = random.randint(1,10)
				if x >= 3:
					isrun = False
			elif self._year in range(80,90):
				x = random.randint(1,10)
				if x >= 5:
					isrun = False
			elif self._year in range(70,80):
				x = random.randint(1,10)
				if x >= 7:
					isrun = False
			elif self._year in range(60,70):
				x = random.randint(1,10)
				if x >= 9:
					isrun = False
			else:
				x = random.randint(1,10000000000)
				if x == 1:
					isrun = False

			if not isrun:
				print('Die in the age at:', self._year)
			


class Person(Live):
	def __init__(self,name='xxx',height=0,weight=0,year=0,day=0,hour=0,mintue=0,second=0):
		super().__init__(year,day,hour,mintue,second)
		self._name = name
		self._height = height
		self._weight = weight

	@property 
	def get_name(self):
		return self._name
	@property
	def get_height(self):
		return self._height
	@property
	def get_weight(self):
		return self._weight
	@property
	def get_age(self):
		return self._year
	@name.setter
	def set_name(self,name):
		self._name = name
	@height.setter
	def set_height(self,height):
		self._height = height
	@weight.setter
	def set_weight(self,weight):
		self._weight = weight

class Student(Person):
	def __init__(self,GPA=0,name='xxx',height=0,weight=0,year=0,day=0,hour=0,mintue=0,second=0):
		super().__init__(name,height,weight,year,day,hour,mintue,second)
		self._GPA = GPA

	@property
	def get_GPA(self):
		return self._GPA
	
	def set_GPA(self,GPA):
		self._GPA = GPA


class ZhiqiZhang(Student):
	def __init__(self,GPA=0,name='xxx',height=0,weight=0,year=0,day=0,hour=0,mintue=0,second=0):
		super().__init__(GPA,name,height,weight,year,day,hour,mintue,second)

	def live(self):
		isrun = True
		while isrun:
			self.second += 1
			if self.second == 60:
				self.second = 0
				self.mintue += 1
				if self.mintue == 60:
					self.mintue = 0
					self.hour += 1
					if self.hour == 4:
						print('4:00,ZhiqiZhang goes to bed')
					elif self.hour == 10:
						print('10:00,ZhiqiZhang gets up')
					elif self.hour == 12:
						print('12:00,ZhiqiZhang eats lunch')
					elif self.hour == 13:
						print('13:00ZhiqiZhang starts looking i5')
					elif self.hour == 17:
						print('17:00,ZhiqiZhang stops watching')
					elif self.hour == 18:
						print('18:00,ZhiqiZhang has dinner')
					elif self.hour == 19:
						print('19:00,ZhiqiZhang begins playing \'Ninja must die\'')
					elif self.hour == 24:
						self.hour = 0
						self.day += 1
						if self.day == 365:
							self.day = 0
							self._year += 1
					else:
						pass

			if self._year >= 100:
				x = random.randint(1,10)
				if x >= 1:
					isrun = False
			elif self._year in range(90,100):
				x = random.randint(1,10)
				if x >= 3:
					isrun = False
			elif self._year in range(80,90):
				x = random.randint(1,10)
				if x >= 5:
					isrun = False
			elif self._year in range(70,80):
				x = random.randint(1,10)
				if x >= 7:
					isrun = False
			elif self._year in range(60,70):
				x = random.randint(1,10)
				if x >= 9:
					isrun = False
			else:
				x = random.randint(1,10000000000)
				if x == 1000:
					isrun = False

			'''if isrun:
				print('%02d:%02d:%02d:%02d:%02d' % (self._year,self.day,self.hour, self.mintue, self.second))'''

			if not isrun:
				print('Die at the age:', self._year)

	def show_face(self):
		turtle.showturtle()
		turtle.penup()
		turtle.goto(0,-300)
		turtle.pendown()
		turtle.begin_fill()
		turtle.color('burlywood1')
		turtle.circle(300)
		turtle.end_fill()
		turtle.penup()
		turtle.left(30)
		turtle.goto(0,-200)
		turtle.pendown()
		turtle.color('red')
		turtle.forward(150)
		turtle.goto(0,-200)
		turtle.left(120)
		turtle.forward(150)
		turtle.penup()
		turtle.goto(0,-20)
		turtle.down()
		turtle.left(30)
		turtle.begin_fill()
		turtle.color('LightPink1')
		turtle.circle(50, steps = 3)
		turtle.end_fill()
		turtle.penup()
		turtle.goto(120,140)
		turtle.pendown()
		turtle.color('blue')
		turtle.circle(50)
		turtle.penup()
		turtle.goto(120,95)
		turtle.begin_fill()
		turtle.color('black')
		turtle.circle(5)
		turtle.end_fill()
		turtle.penup()
		turtle.goto(-120,140)
		turtle.down()
		turtle.color('blue')
		turtle.circle(50)
		turtle.penup()
		turtle.goto(-120,95)
		turtle.pendown()
		turtle.begin_fill()
		turtle.color('black')
		turtle.circle(5)
		turtle.end_fill()
		turtle.penup()
		turtle.goto(-150,150*(3**0.5))
		turtle.pendown()
		turtle.backward(300)
		turtle.done()

def main():
    zzq = ZhiqiZhang(4.0,'张志奇',186,90,18,0,9,59,0)
    zzq.show_face()
    zzq.live()
    
if __name__ == '__main__':
    main()
