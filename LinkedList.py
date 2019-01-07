class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        print(f"\n*** New node created with data = {self.data} and next pointer = {self.next}")


class LinkedList:
    def __init__(self):
        '''
        Empty singly linked list with head pointer node created here. The head pointer node is a "special node" containing no data that
        points to the "head" of the linked list.
        '''
        print(f"\n*** Creating new linked list having head pointer node with data= None and next pointer = None")
        self.head_pointer_node = Node(data=None)
        print(f"*** New linked list created")

    def append(self, data):
        print(f"\n*** Appending Node with data \"{data}\" to empty list")
        new_node = Node(data)
        current_node = self.head_pointer_node

        if self.head_pointer_node.next is None:
            self.head_pointer_node.next = new_node
            new_node.next = None
            print(f"*** New node with data \"{new_node.data}\" appended")
        else:
            print(f"*** Current list is not empty")
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = None
            print(f"*** New node with data \"{new_node.data}\" appended to non empty list\n")

    def prepend(self, data):
        print(f"*** Adding node with data \"{data}\" to beginning of list")
        new_node = Node(data)

        if self.head_pointer_node.next is not None:
            new_node.next = self.head_pointer_node.next
            self.head_pointer_node.next = new_node
            print(f"*** New node with data \"{new_node.data}\" prepended\n")
        else:
            print(f"*** List is empty. Adding new node to list")
            self.append(data)

    def display_elements(self):
        elements_with_data = []

        current_node = self.head_pointer_node.next
        index = 0

        while current_node:

            print(f"Node {index} Data: {current_node.data}")
            if current_node.next:
                print(f"Node {index} Pointer Reference: {current_node.next.data}")
            else:
                print(f"Node {index} Pointer Reference: {current_node.next}")

            elements_with_data.append(current_node.data)

            current_node = current_node.next
            index += 1
            print("\n")

        return print(f"Elements in linked list: {elements_with_data}")

    def list_length(self):
        counter = 0
        current_node = self.head_pointer_node
        while current_node.next is not None:
            current_node = current_node.next
            counter += 1

        print(f"List length is {counter}")
        return counter


def some_test_function():
    test_linked_list = LinkedList()

    print(f"\n>>> Head node data for new linked list is {test_linked_list.head_pointer_node.data} ")
    print(f">>> Head node for new linked list is pointing to {test_linked_list.head_pointer_node.next} ")

    test_linked_list.prepend(data="A")
    test_linked_list.prepend(data="B")
    test_linked_list.prepend(data="C")

    test_linked_list.prepend(1)

    print(f"\n>>> Head node data for new linked list is {test_linked_list.head_pointer_node.data} ")
    print(f">>> Head node for new linked list is now pointing to {test_linked_list.head_pointer_node.next.data} ")

    test_linked_list.display_elements()
    test_linked_list.list_length()


if __name__ == "__main__":
    some_test_function()
