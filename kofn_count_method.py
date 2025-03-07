#Last editied Mar 5, 2025 by Stateus

import random

#base variables
n = 0
k = 0
while True:
	while True:
		try:
			n = int(input("Size of list N: "))
			break
		except:
			print("Incompatible input, try again. [Not Integer]")
	if n > 0:
		break
	else:
		print("Incompatible input, try again. [Too small]")
while True:
	while True:
		try:
			k = int(input("Size of k: "))
			break
		except:
			print("Incompatible input, try again. [Not Integer]")
	if k < n:
		break
	elif k > 0:
		print("Incompatible input, try again. [Too small]")
	else:
		print("Incompatible input, try again. [Too large]")
nlist = []
printWarningLength = 500		#determines at what length of nlist  the code will warn the user


#list generator
def generateList():
	print("")
	print("Generating...")
	for i in range(n):
		nlist.append(random.randint(0,9))
	print("List Generated")
	showlist = input("Print List? [y/n]: ")
	if showlist.lower() == "y":
	
		#detect if list will overflow
		if len(nlist) > printWarningLength:
			print("Warning - The list exceeds " + str(printWarningLength) + " elements.")
			showlist = input("Print List? [y/n]: ")
			if showlist.lower() == "y":
				print(nlist)
		else:
			print(nlist)






def maxsum(parentList, k):
	counts = [0,0,0,0,0,0,0,0,0,0] #each index is a count of its digit in the parentList
	sum = 0

	for i in parentList:
		counts[i] += 1
	
	for j in range(10):
		counts[9-j]
		if k > 0:
			if counts[9-j] >= k:
				sum += k*(9-j)
				break
			else:
				sum += counts[9-j] * (9-j)
				k -= counts[9-j]

	return sum


generateList()
print("")
print("Sum = " + str(maxsum(nlist, k)))







