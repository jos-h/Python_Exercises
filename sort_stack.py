# [34, 3, 31, 98, 92, 23]


def sort_stack(s):
    tmp_stack = list()
    while not is_empty(s):
        temp_element = s.pop()
        while not is_empty(tmp_stack) and top(tmp_stack) > temp_element:
            push_element(s, pop_element(tmp_stack))
        if is_empty(tmp_stack) or top(tmp_stack) <= temp_element:
            push_element(tmp_stack, temp_element)
    print("***********************************")
    print(f"Sorted stack is{tmp_stack}")
    print("***********************************")


def push_element(s, var):
    s.append(var)


def pop_element(s):
    return s.pop()


def top(s):
    stack_len = len(s) - 1
    return s[stack_len]


def is_empty(s):
    return len(s) == 0


def main():
    s = [34, 3, 31, 98, 92, 23]
    sort_stack(s)


if __name__ == '__main__':
    main()
