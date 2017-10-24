#!/usr/bin/python3


def push(element, stack_list, stack_elements):

	if isFull(stack_list, stack_elements):
		return False
	else:
		return stack_list.append(element)


def isFull(stack_list, stack_elements):

	if len(stack_list) == stack_elements:
		return True
	else:
		return False


def pop(stack_list):

	if isEmpty(stack_list):
		print('Stack is empty!!')
	else:
		return stack_list.pop(-1)


def isEmpty(stack_list):
	return stack_list == []


def peep(stack_list):

	return stack_list[-1:]


def menu():
	choice = 0
	while choice < 5:
		print("1: Push\n"
			  "2: Pop\n"
			  "3: Peep \n"
			  "4: display\n")
		choice = eval(input("Enter choice"))
		return choice


def display(stack_list):
	print(stack_list)


def main():

	stack_elements = eval(input("Accept the number of elements to insert into stack"))

	stack_list = []

	while True:

		choice = menu()

		if choice == 1:
			element = eval(input("Enter element to push into stack"))
			val = push(element, stack_list, stack_elements)
			if val == False:
				print("Stack full!!! Empty it ")
		elif choice == 2:

			print("the poped element from stack is {}".format(pop(stack_list)))
		elif choice == 3:
			print("the element at the top of stack is {}".format(peep(stack_list)))
		elif choice == 4:
			print("the elements present inside stack are")
			display(stack_list)


if __name__ == '__main__':
	main()