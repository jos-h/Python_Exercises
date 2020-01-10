class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinaryTreeImplementation:

    def __init__(self):
        self.root = self.p = None

    def create_node(self, value):
        new_node = Node(value)
        return new_node

    def insert_node(self, value):
        new_node = self.create_node(value)
        if not self.root:
            self.root = self.p = new_node
        elif value < self.root.data:
            self.root.left = new_node
            # self.p = new_node
        elif value > self.root.data:
            self.root.right = new_node
            # self.p = new_node

    # def display(self):
    #     while self.root:
    #         print(self.root.data)


def main():
    obj = BinaryTreeImplementation()

    obj.insert_node(8)
    obj.insert_node(6)
    obj.insert_node(9)
    obj.display()
    # obj.insert_node(8)


if __name__ == '__main__':
    main()
