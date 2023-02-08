# Approach would be to add up the digits
# Have a variable to carry over, ideally starting from 0 so we always have some carry over
# If we reach the last node, then we can simply add a new node with the value of that varry over
# have a separate function to loop from a number, via diving it by 10 every time and getting the appropiate digit
import math
from linked import Node, produceSequenceFromArray

def getDigits (number):
	digits = []
	while number >= 1:
		nextDigit = number % 10
		digits.append(nextDigit)
		number /= 10
		number = math.floor(number)
	return digits[::-1]

def addTwoSequences (numb1, numb2):
	
	pointer1 = numb1
	pointer2 = numb2
	sum_ = Node()	
	carry = 0

	while pointer1 != None and pointer2 != None:
		digitAdd = pointer1.data + pointer2.data + carry
		if digitAdd >= 10:
			digits = getDigits(digitAdd)
			sum_.addNode(digits[1])
			carry = digits[0]
			print(f"broken was {digits}")
		else:
			sum_.addNode(digitAdd)
			carry = 0
		
		#print(f"Adding {pointer1.data} and {pointer2.data} with carry {carry} and got {digitAdd}")
		pointer1 = pointer1.next
		pointer2 = pointer2.next 

	while pointer1 != None:
		digitAdd = pointer1.data + carry	
		if digitAdd >= 10:
			digits = getDigits(digitAdd)
			sum_.addNode(digits[1])
			carry = digits[0]
		else:
			sum_.addNode(digitAdd)
			carry = 0
		pointer1 = pointer1.next		
	
	while pointer2 != None:
		digitAdd = pointer2.data + carry	
		if digitAdd >= 10:
			digits = getDigits(digitAdd)
			sum_.addNode(digits[1])
			carry = digits[0]
		else:
			sum_.addNode(digitAdd)
			carry = 0
		pointer2 = pointer2.next		

	if carry > 0:
		sum_.addNode(carry)

	return sum_

number1 = produceSequenceFromArray([9, 1, 1, 1])
number2 = produceSequenceFromArray([9, 1, 1])
summed = addTwoSequences(number1, number2)
summed.printNodes()
