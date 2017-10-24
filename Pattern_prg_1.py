"""
		  *
		* * *
	  * * * * *
		* * *
		  *
"""


def pattern(rows):

	i = 0
	k = 0
	space = rows - 1
	stars = 1

	for i in range(1,rows*2 + 1):
		for j in range(1,space + 1):
			print(" ",end="")

		for k in range(1,stars*2):
			print("*",end="")
		print("")

		if i < rows:
			space -= 1
			stars += 1
		else:
			space += 1
			stars -= 1


def main():
	rows = eval(input("Enter number of rows"))
	pattern(rows)


if __name__ == '__main__':
	main()
