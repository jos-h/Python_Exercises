import sys


def platform_depen():
    assert ("windows" in sys.platform), "On windows only."
    print("do something")


def main():
    try:
        platform_depen()
    except AssertionError as error:
        print(error)
    else:
        try:
            with open("codes/dummy_.txt") as file_handle:
                data = file_handle.read()
        except FileNotFoundError as fnfe:
            print(fnfe)


if __name__ == '__main__':
    main()
