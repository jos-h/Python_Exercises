#!/usr/bin/python3


def main():
	n = int(input().strip())

	for j in range(1, n + 1):
		for i in range(1, n + 1):
			print("*", end='')

		for k in range(0, j):
			print("#", end='')
		print()
		n -= 1

if __name__ == '__main__':
	main()