def string_anagram(src_str, dest_str):
	str_dict = {}

	if not len(src_str) == len(dest_str):
		print("Enter strings of equal length")
		exit(1)
	else:
		for char in src_str:
			if str_dict:
				str_dict[char] = str_dict.get(char, 0) + 1
			else:
				str_dict[char] = str_dict.get(char, 0) + 1

		for char in dest_str:
			if str_dict:
				str_dict[char] = int(str_dict.get(char)) + 1
		print(str_dict)

		for value in str_dict.values():
			if value <= 1:
				return False
		else:
			return True


def main():
	src_str, dest_str = input("Accept the two strings").split()

	# src_str, dest_str = "abccd", "acbcd"

	val = string_anagram(src_str, dest_str)

	if val:
		print("{} is anagram of {}".format(dest_str, src_str))
	else:
		print("{} is not anagram of {}".format(dest_str, src_str))


if __name__ == '__main__':
	main()
