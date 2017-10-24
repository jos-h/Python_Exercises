#!/usr/bin/python3


def push(stack_list, element):
    if isFull(stack_list):
        return stack_list.append(element)
    else:
        pop_list(stack_list)


def isFull(stack_list):
    if stack_list.__len__() == 10:
        return False
    return True


def pop_list(stack_list):
    if not isempty(stack_list):
        return stack_list.pop()


def isempty(stack_list):
    return stack_list == []

def peep(stack_list):
    return stack_list[-1:]


def menu():
    while True:
        print("1:Push\n"
              "2:Pop\n"
              "3:Peep\n"
              "4:display"
              "5:Exit\n")
        choice = eval(input("accept choice"))
        return choice


def main():
    stack_list = eval(input("Accept list to perform stack operations"))

    while True:
        choice = menu()
        if choice == 1:
            element = eval(input("enter element to push"))
            push(stack_list, element)
            print(element)
            print(stack_list)
        elif choice == 2:
            pop_element = pop_list(stack_list)
            print("poped element is{}".format(pop_element))

        elif choice == 3:
            print("top of stack {}".format(peep(stack_list)))
        elif choice == 4:
            print(stack_list)
        else:
            print("exit")
            return


if __name__ == '__main__':
    main()