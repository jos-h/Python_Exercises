import os
from os import listdir
from os.path import isfile, join, isdir


def main():
	mypath = "/home/sudouser/python"
	onlyfiles = [f for f in listdir(mypath) if os.path.isfile(join(mypath,f))]
	onlydir = [d for d in listdir(mypath) if isdir(mypath)]

	print(onlyfiles)
	print(onlydir,end=' ')


if __name__== '__main__':
    main()