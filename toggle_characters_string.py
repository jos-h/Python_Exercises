def toggle_chars(s):
	i = 0
	s_len = len(s) - 1
	new_str = ''
	while i < s_len:
		if s[i].isupper():
			new_str += s[i].lower()
		elif s[i].islower():
			new_str += s[i].upper()
		i += 1
	return new_str


def main():
	s = input()

	print("string is", toggle_chars("DevIce DriVer"))

	
if __name__ == '__main__':
	main()
