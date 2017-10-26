# Make a local change
# Make a local change again
# iteration pattern
# This is change [a] from home

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max = n

	return current_max

def average(scores):
	total = 0
	for n in scores:
		total += n
		
	return toal / len(scores)

def averagev2(scores):
	current_min = scores[0]
	current_min_placement = -1
	for n in scores:
		if n <= cureent_min:
			current_min = n
	scores.remove(current_min)
	second_min = scores[0]
	
	for n in scores:
		if n <= second_min:
			second_min = n
	scores.remove(second_min)
	
	sum_averagev2 = 0
	for n in scores:
		sum_averagev2 += n
	return sum_averagev2 /len(scores)
