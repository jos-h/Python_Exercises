#!/bin/python3

import sys


def diagonal_diff(a, rows, cols):
	i, j = 0, 0
	left_sum, right_sum = 0, 0
	for i in range(rows):
		for j in range(cols):
			if i == j:
				left_sum += a[i][j]
		right_sum += int(a[i][rows - i - 1])

	return abs(left_sum - right_sum)


def main():
	rows = int(input().strip())
	cols = int(input().strip())
	a = [[0 for row in range(0, rows)] for col in range(0, cols)]
	for a_i in range(rows):
		for a_j in range(cols):
			a[a_i][a_j] = int(input().strip())

	print("Elements of 1st matrix", [row for row in a])

	print("diagonal sum difference is ", diagonal_diff(a, rows, cols))


def main_():

	r = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	right_sum = 0
	left_sum = 0

	for i in range(0,len(r),4):
		right_sum += r[i]

	for i in range(-3,-(len(r)),-2):
		left_sum += r[i]

	print("r",right_sum)
	print(abs(left_sum - right_sum))

if __name__ == '__main__':
	#main()
	main_()
