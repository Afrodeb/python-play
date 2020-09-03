1.	# Program to check if a number is prime or not
2.	
3.	num = 407
4.	
5.	# To take input from the user
6.	#num = int(input("Enter a number: "))
7.	
8.	# prime numbers are greater than 1
9.	if num > 1:
10.	   # check for factors
11.	   for i in range(2,num):
12.	       if (num % i) == 0:
13.	           print(num,"is not a prime number")
14.	           print(i,"times",num//i,"is",num)
15.	           break
16.	   else:
17.	       print(num,"is a prime number")
18.	       
19.	# if input number is less than
20.	# or equal to 1, it is not prime
21.	else:
22.	   print(num,"is not a prime number")
