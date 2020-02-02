# -*- coding: utf-8 -*-
"""
Created on Thu Feb 2 21:57:38 2020

@author: Pope  Zheng
"""
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __getitem__(self,index):
		if index == 0:
			return self.x
		if index == 1:
			return self.y

	def __str__(self):
		return '(' + str(self.x) + ',' + str(self.y) + ')'

	def distance(self,other):
		distance = ((self.x - other[0])**2 + (self.y - other[1])**2) ** 0.5
		return distance

	def min_distance(self,point_set):
		distance_list = []
		min_list = []
		min_distance = self.distance(point_set[0])
		for point in point_set:
			d = self.distance(point)
			distance_list.append(d)
			if d < min_distance:
				min_distance = d
		for i in range(len(distance_list)):
			if distance_list[i] == min_distance:
				min_list.append(i)
		return [min_distance,min_list]

def add_point(points,point):
		points.append(point)

def get_points():
	points = []
	point_num = eval(input('Other Points number:'))
	for i in range(point_num):
		x,y = input('point' + str(i+1) + ':').split()
		current_point = Point(float(x),float(y))
		add_point(points,current_point)
	return points

def get_point():
	x,y = input('point0:').split()
	point = Point(float(x),float(y))
	return point

def main():
	point0 = get_point()
	point_set = get_points()
	print(point0.min_distance(point_set))

if __name__ == '__main__':
	main()