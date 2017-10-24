"""
	**********
	****  ****
	***    ***
	**      **
	*        *
	*        *
	**      **
	***    ***
	****  ****
	**********

"""


def pattern(rows):
	spaces = rows * 2
	stars = rows * 2
	sp = 0
	counter = rows * 2
	for i in range(1, counter + 1):
		if spaces == 10:
			print("*" * stars, end="")
		elif 10 > spaces > 0:
			st = (stars // 2)
			print("*" * st, end="")
			print(" " * sp, end="")
			print("*" * st, end="")
		# elif spaces == 0:
		# 	print("*", end=" " * (sp - 2))
		# 	print("*", end ="")
		if i < rows:
			spaces -= 2
			stars -= 2
			sp += 2
		else:
			spaces += 2
			stars += 2
			sp -= 2
		print()


def main():
	# rows = eval(input("Accept the rows"))
	pattern(5)


if __name__ == '__main__':
	main()
