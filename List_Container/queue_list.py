#!/usr/bin/python3


def menu():
    print("1:Nqueue\n"
          "2:Dqueue\n"
          "3:Display"
          "4:Exit\n")
    choice = eval(input("enter choice"))
    return choice


def enqueue(queue_list, element):
    if not isfull(queue_list):
        return queue_list.append(element)
    else:
        dequeue(queue_list)


def dequeue(queue_list):
    if not isempty(queue_list):
        return queue_list.pop(0)


def isempty(queue_list):
    return queue_list == []


def isfull(queue_list):
    if queue_list.__len__() == 20:
        return True
    return False


def display(queue_list):
    return queue_list


def main():
    queue_list = eval(input("Accept the list"))
    print(queue_list.__len__())
    while True:
        choice = menu()
        if choice == 1:
            element = eval(input("Enter elment to insert into queue"))
            enqueue(queue_list,element)
            print(element)
            print(queue_list)
        elif choice == 2:
            print("removed element is {}".format(dequeue(queue_list)))
        elif choice == 3:
            print("Elements in queue are {}".format(display(queue_list)))
        else:
            print("exit")
            return

if __name__ == '__main__':
    main()