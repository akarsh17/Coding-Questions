#!/usr/bin/env python3
''' A contest closes in n days hh hours, mm minutes and ss seconds.
Given two values of n,how many palindrome of format
nhhmmss would we find in the indicated interval'''

rnge = list(map(int,input("Enter n1 and n2 (followed by space) : ").split()))
n1= rnge[0]
n2=rnge[1]
count1=0

# prints palindrome between min and max 
def cnt_Palindrome(minimum: int, maximum: int) -> None:
	global count1
	for s in range(minimum, (maximum + 1)):
		s = str(s)
		if (s == s[::-1]) :
			# print(s, end = " ")
			count1 = count1+1
	# print()

# Driver Code 
n3 = 0
temp =0
for n1 in range(n1 ,n2+1):
	if(n1==0):
		temp = n1
		# n1=n1+1
		n3=str(n1+1)+'235959'
		n1=str(n1+1)+'000000'
		# n1 = int(n1)
		# n3 = int(n3)
	#	print(n1, n3)
		# print()
		cnt_Palindrome(int(n1),int(n3))
		n1 = temp
	
	else:
		temp = n1	
		n3=str(n1)+'235959'
		n1=str(n1)+'000000'
		# n1 = int(n1)
		# n3 = int(n3)
	#	print(n1, n3)
		# print()
		# print(n3)
		cnt_Palindrome(int(n1),int(n3))
		n1 = temp

print(count1)
