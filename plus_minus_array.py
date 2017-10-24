#!/usr/bin/python3


def calculate_fraction(positive_cnt, negative_cnt, zeros_cnt, size):

	return (positive_cnt / size), (negative_cnt / size), (zeros_cnt / size)


def plus_minus(int_arr):

	positive_cnt = 0
	negative_cnt = 0
	zeros_cnt = 0

	for element in int_arr:
		if element < 0:
			negative_cnt += 1
		if element == 0:
			zeros_cnt += 1
		if element > 0:
			positive_cnt += 1

	positive_fraction,\
	negative_fraction,\
	zeros_fraction = calculate_fraction(positive_cnt, negative_cnt, zeros_cnt, len(int_arr))

	return positive_fraction, negative_fraction, zeros_fraction


def main():

	arr_elem = int(input("how many elements in array?"))
	int_arr = [6,-4,2,0,-3,0] #[int(elem) for elem in input("enter elements in list").strip().split(' ')]

	# for ele in range(arr_elem):
	# 	int_arr.append(eval(input("enter elements in list")))
	#
	#
	# p_f, n_f, z_f = plus_minus(int_arr)
	#
	# print("{:.6f}".format(p_f))
	# print("{:.6f}".format(n_f))
	# print("{:.6f}".format(z_f))

	print("*********************")

	print("OR")

	n = len(int_arr)
	print(format(len([x for x in int_arr if x > 0]) / n,".6f"))
	print(format(len([x for x in int_arr if x < 0]) / n, ".6f"))
	print(format(len([x for x in int_arr if x == 0]) / n, ".6f"))

if __name__ == '__main__':
	main()