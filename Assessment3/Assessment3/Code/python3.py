    	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI

	# Type help() or for example help(str)
	
	
	# <QUESTION 1>

	# Write a function which takes a string of numbers, separated by commas, and returns all the odd numbers as a string, separated by commas.
	
	# If there are no odd numbers then the function should return "null".

	# Inputs will always be given in ascending order, eg "3,4,5". Outputs should also be given in ascending order.

	# <EXAMPLES>

	# one("1,2,3,4,5") → "1,3,5"
	# one("2,4,6,8") → "null"
	# one("23,48,52,57") → "23,57"

	# <HINT>
	# What were the name of the functions we used to get a list from a string, and get a string from a list?
	# Use help(str) on your CLI for more information.

def one(input):
	splitinput =input.split(',')
	nums = []
	for i in splitinput:
		i = int(i)
		if i % 2 != 0:
			nums.append(i)
		else:
			continue
    
	if (len(nums)) >= 1:
		return ','.join([str(i) for i in nums])
	else:
		return "null"



	# <QUESTION 2>

    # Given an Array of Strings, remove any duplicate Strings that occur, then return the Array.
    # Do not ignore case.

    # <EXAMPLES>

	# two(["Dog"]) → ["Dog"]
	# two(["Dog","Cat"]) → ["Dog","Cat"]
	# two(["Dog","Dog","Cat"]) → ["Dog","Cat"]
    # two(["Dog","DoG","Cat"]) → ["Dog","DoG","Cat"]    

	# <HINT>
	# How did we check if an entry was NOT IN a list?

def two(input):
	mylist = list( dict.fromkeys(input) )
	return mylist

	# <QUESTION 3>

    # Write a function which, given a string input, returns a string which contains only the characters with odd indexes.

	# <EXAMPLES>

	# three("Hello") → "el"
	# three("hi") → "i"
	# three("0H1e2l3l4o5w6o7r8l9d") → "Helloworld"

	# <HINT>
	# How do we choose only the odd numbers when using range()?

def three(input):
	return input[1::2]
			

	# <QUESTION 4>

    # given a string - return the number of times "am" appears in the String
	# ignoring case -
	# BUT ONLY WHEN the word "am" appears without being followed or preceded by
	# other letters
	    
    # <EXAMPLES>

	# four("Am I in Amsterdam") → 1
	# four("I am in Amsterdam am I?") → 2
	# four("I have been in Amsterdam") → 0

	# <HINT>
	# What function do we use to get a list from a string? Use help(str) on your CLI for more information.

def four(arg1):
	arg1 = arg1.lower()
	arg1 = arg1.split(' ')
	return arg1.count('am')

	# <QUESTION 5>

    # Write a function which checks the validity of a credit card number.
	# The function will take a string and should return a boolean, True if the card is valid, or False if it is not.

	# A credit card has a valid number if it satisfies the following criteria.
	# - it must start with a 4, 5 or 6.
	# - it must contain exactly 16 digits.
	# - each digit must be 0-9 inclusive.
	# - it may contain hyphens ("-"), to separate groups of 4 digits only, but it cannot contain any other characters.
	# - it must not have 4 or more consecutive repeated digits.

	# <EXAMPLES>

	# five(0123-4567-8901-2345) → False
	# five(401234567890123) → False
	# five(4012 3456 7890 1234) → False
	# five(4444-0123-4567-8901) → False
	# five(4012-3456-7890-1234) → True
	# five(4012345678901234) → True

	# <HINT>
	# How did we check if an entry was NOT IN a list?
	# Think about maybe nesting 'if statements' and/or 'for loops'.

def five(input):
	numlist = ('0,1,2,3,4,5,6,7,8,9,-')
	digit_bool = []
	if (len(input)) == 19 and (input[4::5]) == '---' and (input[0] == '4' or input[0] == '5' or input[0] == '6'):
		digit_bool.append(True)
	else:
		digit_bool.append(False)
	for i in input:
		if i in numlist:
			digit_bool.append(True)
		else:
			digit_bool.append(False)
	split = input.split('-')
	for j in split:
		for char in j:
		    if (j.count(char)) <= 3:
			    digit_bool.append(True)
		    else:
			    digit_bool.append(False)
	return all(digit_bool)





	# <QUESTION 6>

    # Given an email address person@company.com, and a parameter "person" or "company",
	# write a function which returns the corresponding piece of information.
	# Your function should ignore case.

	# <EXAMPLES>

	# six("john@google.com", "person") → john
	# six("jane@Microsoft.com", "company") → microsoft
	# six("Dave@amazon.com", "person") → dave

	# <HINT>
	# How can you split the email address up? Use help(str) on your CLI for more information.

def six(email, parameter):
	email = email.lower()
	split = email.split('@')
	if parameter == 'person':
		return str(split[0])
	elif parameter == 'company':
		company = split[1]
		return str(company[:-4])
	


	# <QUESTION 7>

    # Given a string, return the length of the largest "block" in the string.
	# A block is a run of adjacent chars that are the same, do not ignore case.
	
    # <EXAMPLES>
	
	# seven("hoopplla") → 2
	# seven("abbCCCddDDDeeEEE") → 3
	# seven("") → 0

	# <HINT>
	# Try using nested for loops and keep track of the longest block.
    
def seven(input):
	if input == '':
		return 0
	mylist = []
	for i in input:
		mylist.append(input.count(i))
		nums = sorted(mylist)
	return nums[-1]



	# <QUESTION 8>

    # There is a mathematical function which is defined in the following way:

	# eight(n)=0 if n=0
	# eight(n)=1 if n=1
	# eight(n)=eight(n-1)+eight(n-2) if n>1

	# eg eight(2) = eight(1) + eight(0) = 1 + 0 = 1, so eight(2) = 1

	# Write a Python function which outputs the result of the mathematical function, given an input n.

	# <EXAMPLES>

	# eight(3) → 2
	# eight(8) → 21
	# eight(0) → 0
	# eight(1) → 1

	# <HINT>
	# You can have nested functions in Python.

def eight(n):
	return 0

	# <QUESTION 9>

    # Write a function which solves the following puzzle.
	
	# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
	# The values for 'heads' and 'legs' will be inputs and can be different from 35 and 94.
	# The output should be of the form (chickens,rabbits).
	# If there are no solutions to the puzzle, return "no solutions"

	# <EXAMPLES>

	# nine(35, 94) → (23,12)
	# nine(2, 6) → (1,1)
	# nine(12,63) → "no soltuions"

	# <HINT>
	# How many legs/heads does a chicken have?
	# How many legs/heads does a rabbit have?
	# If we have the right number of legs, do we have the right number of heads?

def nine(heads,legs):
	return "no solutions"

	# <QUESTION 10>

    # Write a function that accepts a comma separated sequence of lower case words as input and returns the words in a comma-separated
	# sequence after sorting them alphabetically.

	# <EXAMPLES>

	# ten('bag,car,dog') → "bag,car,dog"
	# ten('dog,car,bag') → "bag,car,dog"
	# ten('car,bark,bag,dog') → "bag,bark,car,dog"

	# <HINT>
	# What was the function which we used to sort a list in ascending numeric order? It works on strings too.
	# Use help(list) on your CLI for more information.

def ten(input):
	mylist = input.split(',')
	return ','.join(sorted(mylist))


