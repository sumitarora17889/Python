import numpy as np

class node(object):
    def __init__(self,value):
        self.val=value
        self.prev=None
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.end=None

    def insert(self,node):
        if self.head is None:
            self.head=node
            self.end=node
        else:
            self.end.next=node
            node.prev=self.end
        print("Node Inserted")

    def traverse(self):
        if self.head is None:
            print("List Empty")
        else:
            print(self.head)
            self.traverse(self.next)

ll=LinkedList()
ll.insert(node(5))
ll.insert(node(7))
ll.traverse()

