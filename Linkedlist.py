class Node:
	def __init__(self):
		self.data = None
		self.next = None


class Linkedlist:
	def __init__(self):
		self.head = None

	def gethead(self):
		return self.head

	def newNode(self, data):
		nw = Node()
		nw.data = data
		nw.next = self.head
		self.head = nw
		return nw

	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next


def main():
	llist = Linkedlist()
	nodes_to_create = eval(input("Enter how many nodes to create"))
	for i in range(nodes_to_create):
		nw = llist.newNode(input("Enter the data"))

	llist.display()


if __name__ == '__main__':
	main()
