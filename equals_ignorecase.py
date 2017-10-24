#!/usr/bin/python3


class CompareCaseSensitivity(object):

	def __init__(self):

		self.first_str = ''
		self.second_str = ''

	def __del__(self):
		print("str memory released")

	def comparestring(self, first_str, second_str):
		print("---")
		if first_str.lower() == second_str.lower():
			return 0
		else:
			return [abs(ord(first_str[0]) - ord(second_str[0]))]


def main():

	first_str = str(input("Accept string from user to compare"))
	second_str = str(input("Accept string from user to compare"))
	obj = CompareCaseSensitivity()
	s = obj.comparestring(first_str, second_str)

	if s == 0:
		print("strings are equal")
	else:
		print("diff between mismatch char is",s)

if __name__ == '__main__':
	main()