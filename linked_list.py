class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        head = self.head
        while head is not None:
            print(head.value)
            head = head.next

    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        self.listprint()


s_linked_list = LinkedList()
node1 = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")

s_linked_list.head = node1
s_linked_list.head.next = node2
node2.next = node3

s_linked_list.listprint()
print('Reverse list:')
s_linked_list.reverse()
