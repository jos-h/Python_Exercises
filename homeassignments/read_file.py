

def read_file():
    with open("/home/sudouser/Command_Line_demo/abc.txt") as file_handle:
        for line in reversed(file_handle.readlines()):
            print(line)
def main():
    read_file()

if __name__ == '__main__':
    main()