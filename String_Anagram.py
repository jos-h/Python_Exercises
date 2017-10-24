def string_anagrams(src, dest):
	if not len(src) == len(dest):
		return False
	else:
		src_list = list(src)
		src_list.sort()

		dest_list = list(dest)

		dest_list.sort()

		i = 0

		while i < len(dest):
			if not src_list[i] == dest_list[i]:
				return False
			i += 1
		else:
			return True


def main():
	# src, dest = input("Enter two strings").split()

	src, dest = "dog", "god"

	val = string_anagrams(src, dest)
	if val:
		print("{} is anagram of {}".format(dest, src))
	else:
		print("Strings are not anagram")


if __name__ == '__main__':
	main()
