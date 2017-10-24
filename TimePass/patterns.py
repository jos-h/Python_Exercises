# cook your dish here
def pattern():
	rows = int(20)
	spaces = rows - 1
	stars = 1

	for i in range(1, rows * 2):
		for sp in range(spaces):
			print(end=" ")
		for k in range(1, stars * 2):
			print("*", end="")
		print()
		if i < rows:
			spaces -= 1
			stars += 1
		else:
			spaces += 1
			stars -= 1


def main():
	pattern()


if __name__ == '__main__':
	main()
