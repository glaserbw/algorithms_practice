# Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

def diff(a1, a2):
	a3 = a1 + a2
	a3.sort()
	difference = a3[-1] - a3[0]
	for i in range(len(a3)-1):
		temp = a3[i+1] - a3[i]
		if temp < difference:
			if a3[i] in a1 and a3[i+1] in a1:
				difference = difference
			elif a3[i] in a2 and a3[i+1] in a2:
				difference = difference
			else:
				difference = temp
	print(difference)
a1 = [1, 3, 15, 11, 2]
a2 = [23, 127, 235, 19, 8]

a3 =  [10, 5, 40]
a4 = [50, 90, 80]

diff(a1,a2)
diff(a3,a4)
