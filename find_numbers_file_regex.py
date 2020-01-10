import re


def get_numbers_from_file(FILE_PATH):
    with open(FILE_PATH, "r") as fp:
        words = fp.read()
    compile_pattern = re.compile("\\d+")
    l = compile_pattern.findall(words)
    print(l)


def main():
    FILE_PATH = "D://Pycharm_Projects//codes//sample.txt"
    get_numbers_from_file(FILE_PATH)


if __name__ == '__main__':
    main()
