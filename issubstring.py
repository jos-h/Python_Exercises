def issubstring(s, s1):
    return s.find(s1)


def main():
    s = 'geeksforgeeks'
    s1 = 'forr'
    print(issubstring(s, s1))

if __name__ == '__main__':
    main()