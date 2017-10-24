#!/usr/bin/python3
import sys
from sys import argv


def command_line_demo():
    print(sys.argv[0])


def command_line_args():
    my_path = "/home/sudouser/Command_Line_demo/"
    input_file = my_path + argv[1]
    output_file = my_path + argv[2]

    lines = int(argv[3])

    operations = argv[4]
    if operations == "copy":
        copy_file(input_file,output_file,lines)
    elif operations == "cmp":
        cmp_files(input_file, output_file,lines)
    elif operations == "diff":
        diff_files(input_file, output_file,lines)
    elif operations == "append":
        append_files(input_file,output_file,lines)


def copy_file(input_file, output_file, lines):
    i = 0
    with open(output_file, "w") as file_write:
        print("output file open")
        with open(input_file, "r") as file_read:
            print("input file open")
            print("inp=>",input_file)
            for line in file_read :
                print("=>",line)
                if i < lines:
                    file_write.write(line)
                    i += 1
                else:
                    break
        file_read.close()
    file_write.close()
    display_cop_file(output_file)


def display_cop_file(output_file):
    print("Display function")
    with open(output_file,"r") as file_read:
        print([line for line in file_read])


def diff_files(input_file, output_file,lines):
    return ''


def append_files(input_file,output_file,lines):
    return ''


def cmp_files(input_file, output_file,lines):
    return ''


def main():
    command_line_demo()
    command_line_args()


if __name__ == '__main__':
    main()