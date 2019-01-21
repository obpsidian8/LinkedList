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
        print("\nDisplaying contents of linked list")
        elements_with_data = []

        current_node = self.head_pointer_node.next
        index = 0

        while current_node:

            print(f"***Node {index} Data: {current_node.data}")
            if current_node.next:
                print(f"***Node {index} Pointer: {current_node.next.data}")
            else:
                print(f"***Node {index} Pointer: {current_node.next}")

            elements_with_data.append(current_node.data)

            current_node = current_node.next
            index += 1

        return print(f"***Elements in linked list: {elements_with_data}")

    def list_length(self):
        counter = 0
        current_node = self.head_pointer_node
        while current_node.next is not None:
            current_node = current_node.next
            counter += 1

        print(f"***List length is {counter}")
        return counter

    def swap_nodes(self, key1, key2):
        current_node1 = self.head_pointer_node
        previous_node1 = None
        node_to_swap_1 = None
        node_to_swap_1_previous = None

        while current_node1:
            previous_node1 = current_node1
            current_node1 = current_node1.next

            if current_node1 is not None and current_node1.data == key1:
                print(f"Found key {key1}")
                node_to_swap_1 = current_node1
                node_to_swap_1_previous = previous_node1

                break

        current_node2 = self.head_pointer_node
        previous_node2 = None
        node_to_swap_2 = None
        node_to_swap_2_previous = None

        while current_node2:
            previous_node2 = current_node2
            current_node2 = current_node2.next

            if current_node2 is not None and current_node2.data == key2:
                print(f"Found key {key2}")
                node_to_swap_2 = current_node2
                node_to_swap_2_previous = previous_node2

                break

        if node_to_swap_1 is None or node_to_swap_2 is None:
            print(f"One of two of the keys supplied missing from the list")

        elif key1 == key2:
            print(f"Keys are the same. Nothing to change")

        else:

            print(f"Proceeding to swap nodes {key1} and {key2}")

            node_to_swap_1_previous.next = node_to_swap_2
            node_to_swap_2_previous.next = node_to_swap_1

            temp1 = node_to_swap_1.next
            temp2 = node_to_swap_2.next
            
            node_to_swap_1.next = temp2
            node_to_swap_2.next = temp1

    def reverse_list(self):
        print(f"\nReversing List")
        current_node = self.head_pointer_node
        previous_node = None
        temp_next = current_node.next

        while current_node:

            previous_node = current_node
            current_node = temp_next

            if current_node is None:
                print(f"\nReached end of list")
                return

            temp_next = current_node.next

            if temp_next == None:
                self.head_pointer_node.next = current_node

            if previous_node == self.head_pointer_node:
                current_node.next = None
            else:
                current_node.next = previous_node






def some_test_function():
    test_linked_list = LinkedList()

    print(f"\n>>> Head node data for new linked list is {test_linked_list.head_pointer_node.data} ")
    print(f">>> Head node for new linked list is pointing to {test_linked_list.head_pointer_node.next} ")

    test_linked_list.append(data="A")
    test_linked_list.append(data="B")
    test_linked_list.append(data="C")
    test_linked_list.append(data="D")

    test_linked_list.prepend(1)

    print(f"\n>>> Head node data for new linked list is {test_linked_list.head_pointer_node.data} ")
    print(f">>> Head node for new linked list is now pointing to {test_linked_list.head_pointer_node.next.data} ")

    test_linked_list.display_elements()
    test_linked_list.list_length()

    # test_linked_list.swap_nodes("D", 1)
    # test_linked_list.swap_nodes("A", "B")
    # test_linked_list.swap_nodes("B", "A")

    test_linked_list.display_elements()
    test_linked_list.reverse_list()
    test_linked_list.display_elements()


if __name__ == "__main__":
    some_test_function()
