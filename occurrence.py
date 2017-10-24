#!/usr/bin/python3


class WordOccurr(object):

	def __int__(self):
		print("in constructor")

	def __del__(self):
		print("destructor")

	def calculateoccurrword(self, file_path):

		word = "include"
		occurrence = 0
		offset_list = []
		try:
			with open(file_path, "rt") as file_handle:
				line = file_handle.readline()
				print(line)
				if word in line:
					occurrence += 1
					offset = file_handle.tell()
					offset_list.append(offset)

		except FileNotFoundError as e:
			print(e.errno)
		finally:
			print('in final')
		#return occurrence, offset_list


def main():
	obj = WordOccurr()
	v, f = obj.calculateoccurrword(r"/home/sudouser/PycharmProjects/Practice_Programs/demo.txt")

	print("occurrence is {} and offset is {}".format(v,f))

if __name__ == '__main__':
	main()