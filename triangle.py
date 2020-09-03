1.	# Python Program to find the area of triangle
2.	
3.	a = 5
4.	b = 6
5.	c = 7
6.	
7.	# Uncomment below to take inputs from the user
8.	# a = float(input('Enter first side: '))
9.	# b = float(input('Enter second side: '))
10.	# c = float(input('Enter third side: '))
11.	
12.	# calculate the semi-perimeter
13.	s = (a + b + c) / 2
14.	
15.	# calculate the area
16.	area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
17.	print('The area of the triangle is %0.2f' %area)
