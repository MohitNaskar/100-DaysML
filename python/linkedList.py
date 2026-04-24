class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.insert(1)
llist.printList()
llist.insert(2)
llist.insert(3)
llist.printList()
llist.insert(4)
llist.insert(5)
llist.printList()