# -*- coding: utf-8 -*-
"""
Created on Sat Feb 1 21:57:38 2020

@author: Pope  Zheng
"""
class Rational(object):

	def __init__(self,numerator=0,denominator=1):
		divisor = gcd(numerator,denominator)
        #Add int(),otherwise will dispay float
		self._numerator = int(numerator / divisor)
		self._denominator = int(denominator / divisor)
        
        
        #make element is this object can be searched by index[]
	def __getitem__(self,index):
		if index == 0:
			return self._numerator
		if index == 1:
			return self._denominator


	def __add__(self,other):
		n = self._numerator*other[1] + self._denominator*other[0]
		d = self._denominator * other[1]
        #Use construction at first can make this more efficent
		return Rational(n,d)

	def __sub__(self,other):
		n = self._numerator*other[1] - self._denominator*other[0]
		d = self._denominator*other[1]
		return Rational(n,d)

	def __mul__(self,other):
		n = self._numerator * other[0]
		d = self._denominator * other[1]
		return Rational(n,d)

	def __truediv__(self,other):
		n = self._numerator * other[1]
		d = self._denominator * other[0]
		return Rational(n,d)

	def __float__(self):
		return self._numerator / self._denominator

	def __int__(self):
		return int(self._numerator // self._denominator)
    
    #print this
	def __str__(self):
		if self._denominator == 1:
			return str(self._numerator)
		else:
			return str(self._numerator) + '/' + str(self._denominator)

	def __cmp__(self,other):
		result = self.__sub__(other)
        #Add index in this is very important!!!
		if result[0] >0:
			return 1
		elif result[0] == 0:
			return 0
		else:
			return -1
        
    #Alawys use __cmp__() at first
	def __lt__(self,other):
		return self.__cmp__(other) < 0
	def __le__(self,other):
		return self.__cmp__(other) <= 0
	def __eq__(self,other):
		return self.__cmp__(other) == 0
	def __ne__(self,other):
		return self.__cmp__(other) != 0
	def __gt__(self,other):
		return self.__cmp__(other) > 0
	def __ge__(self,other):
		return self.__cmp__(other) >= 0

#If this in the class, it will be ignored
def gcd(x,y):
	x = int(x)
	y = int(y)
	if x >= y:
		x,y = y,x
	for i in range(x,0,-1):
		if x%i == 0 and y%i == 0:
			return i
        
def main():
    x = Rational(1,2)
    y = Rational(1,5)
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(float(x))
    print(int(x))
    print(x > y)
    print(x >= y)
    print(x == y)
    print(x <= y)
    print(x < y)
    print(y[0])
    print(y[1])

if __name__ == '__main__':
    main()