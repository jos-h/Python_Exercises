#!/bin/python3
def diagonal(mat, row):
	mat_len = len(mat)
	# Main Diagonal Sum

	primary_diagonal = [mat[i][i] for i in range(row)]

	secondary_diagonal = [mat[i][mat_len - 1 - i] for i in range(row)]

	a = list(zip(primary_diagonal, secondary_diagonal))

	print(abs(sum(a)))


def main():

	mat = []
	row = int(input())

	mat = [[item for item in input().strip()] for i in range(row)]

	diagonal(mat, row)

if __name__ == '__main__':
	main()
