#!/bin/python3
def diagonal(mat, row):
	# Main Diagonal Sum
	i_index, pd_sum = 0, 0
	for i in range(row):
		pd_sum += mat[i_index]
		i_index += row + 1

	# Secondary Diagonal Sum
	i_index, sd_sum = row - 1, 0
	for i in range(row):
		sd_sum += mat[i_index]
		i_index += row - 1

	print(abs(pd_sum - sd_sum))


def main():
	mat = []
	row = int(input())

	for i in range(row):
		mat.extend(list(map(int, input().split())))  # keep extending the array

	diagonal(mat, row)


if __name__ == '__main__':
	main()
