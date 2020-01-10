class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.p = None

    def create_new_node(self, i):
        return Node(i)

    def add_nodes(self, start, end):
        for i in range(start, end):
            nw = self.create_new_node(i)
            if self.head is None:
                self.head = self.p = nw
            else:
                self.p.next = nw
                self.p = nw

    def display(self):
        temp = self.head
        s = ''
        while temp:
            s += str(temp.value)
            temp = temp.next
        print("->".join(s))
        return s

    @staticmethod
    def add_two_numbers_linked_list(ll, ll_1):
        first_operand = int("".join(ll.display().split("->")))
        second_operand = int("".join(ll_1.display().split("->")))
        return first_operand + second_operand

    def reverse_list(self):
        next_ptr = prev = None
        current = self.head
        while current:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
        self.head = prev


def main():
    ll = LinkedList()
    ll.add_nodes(0, 5)
    ll.display()

    # ll_1 = LinkedList()
    # ll_1.add_nodes(5, 10)
    # ll_1.display()
    ll.reverse_list()
    ll.display()
    # print(f'{LinkedList.add_two_numbers_linked_list(ll, ll_1)}')


if __name__ == '__main__':
    main()
