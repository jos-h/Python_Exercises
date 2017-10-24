#!/usr/bin/python3

def copy_all_file(input_file, output_file):
    with open(output_file, "w") as file_write:
        print("output file open")
        with open(input_file, "r") as file_read:
            print("input file open")
            for line in file_read:
                file_write.write(line)
        file_read.close()
    file_write.close()	


def copy_n_lines(input_file, output_file, line_number):
    
    i = 0;
    with open(output_file, "w") as file_write:
        print("copy n lines write")
        with open(input_file, "r") as file_read:
            print("read n lines")
            #while i < line_number:
            for line in file_read:
                if i < line_number:
                    print("line=>",line)
                    file_write.write(line)
                else:
                    break
                i += 1
        file_read.close()
    file_write.close()


def copy_input_output_file(input_file, output_file, line_number):
    
    if line_number == -1:
        copy_all_file(input_file, output_file)
    elif line_number < -1:
        print("Plz specify positive number of lines")
    elif line_number >= 1:
        copy_n_lines(input_file, output_file, line_number)
    elif line_number == 0:
        print("Nothing to copy")


def accept():
    ch = 'y'
    
    PATH = "D:\\macrocodesrequired\\python\\"
    input_file = input(str(("accept file name from user")))
    input_file = PATH + input_file
    output_file = input(str(("accept file name from user")))
    output_file = PATH + output_file
    
    while ch == 'y':
        line_number = int(input("Accept the number of lines"))
        copy_input_output_file(input_file, output_file, line_number)
        ch = str(input("Accept the choice"))


def main():
    accept()


if __name__ == '__main__':
    main()