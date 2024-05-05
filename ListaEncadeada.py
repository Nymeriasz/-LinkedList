class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
        
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        if self.is_empty():
            print("Lista vazia")
            return 
            
        print("Elementos: ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        return None
        
linked_list = LinkedList()

linked_list.insert(15)
linked_list.insert(24)
linked_list.insert(25)
linked_list.print_list()