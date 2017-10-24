def words(s):
	str_ = ""
	str_len = len(s) - 1
	temp = ''
	for ch in range(str_len, -1, -1):

		if s[ch] == " ":
			str_ = reverse_words(s, ch + 1)
			temp = temp + str_ + ' '

	return temp


def reverse_words(s, ch):
	i = 1
	temp_str = ""
	cnt = ch
	while i != ch:
		var = s[cnt]
		temp_str += var
		cnt += 1
		i += 1
	else:
		if i == 1 and ch == 1:
			temp_str += s[ch]

	print("====>",temp_str)
	return temp_str


def main():
	s = ' i am kunal'
	print("reverse string is {0}".format(words(s)))

if __name__ == '__main__':
	main()