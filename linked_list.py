class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def add_to_front(self, value):
        new_node = Node(value)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node


    def add_to_end(self, value):
        new_node = Node(value)

        new_node.prev = self.tail

        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    def display(self):
        result = []
        actual = self.head

        while actual:
            result.append(actual.value)
            actual = actual.next

        return result

    def remove_from_front(self):
        if self.head is None:
            return None

        removed_value = self.head.value

        self.head = self.head.next 

        if self.head is None:
            self.tail = None
        else:
            self.head.tail = None

        return removed_value

    def remove_from_end(self):
        if self.tail is None:
            return None

        removed_value = self.tail.value 

        self.tail = self.tail.prev 

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return removed_value

dll = DoublyLinkedList()

dll.add_to_front(3)
dll.add_to_front(2)
dll.add_to_front(1)
dll.add_to_end(4)
dll.add_to_end(5)
dll.add_to_end(7)

print(dll.display())

print(dll.remove_from_front())
print(dll.remove_from_front())
print(dll.remove_from_front())
print(dll.remove_from_front())
print(dll.remove_from_front())
print(dll.remove_from_front())
print(dll.remove_from_front())


print(dll.display())

