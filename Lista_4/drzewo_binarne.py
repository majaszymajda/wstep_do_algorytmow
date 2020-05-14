import binarytree


def drzewo_binarne_1():

    class Node:

        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.data)

    class NodeS:
        # wezel binarny do stosu
        def __init__(self, data):
            self.data = data
            self.next = None

    class Stack:
        def __init__(self):
            self.head = None

        def push(self, data):
            if self.head is None:
                self.head = NodeS(data)
            else:
                new_node = NodeS(data)
                new_node.next = self.head
                self.head = new_node

        def pop(self):
            if self.head is None:
                return None
            else:
                popped = self.head.data
                self.head = self.head.next
                return popped

        def isEmpty(self):
            return self.head == None

    def traverse_preorder(top):
        # funkcja przechodzenia przez drzewo rekurencyjnie
        if top is None:
            return
        print(top)
        traverse_preorder(top.left)
        traverse_preorder(top.right)

    def traverse_stack(top):
        if top is None:
            return
        stack = Stack()
        stack.push(top)
        while not stack.isEmpty():
            node = stack.pop()
            print(node)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # tworzenie drzewa

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # sprawdzenie drzewa

    traverse_stack(root)


def drzewo_binarne_2():

    class Node:
        # wezel binarny dla kolejki

        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.data)

    class NodeQ:

        def __init__(self, data):
            self.data = data
            self.next = None

    # kolejka

    class Queue:

        def __init__(self):
            self.front = self.rear = None

        def isEmpty(self):
            return self.front == None

        # Method to add an item to the queue
        def enQueue(self, item):
            temp = NodeQ(item)

            if self.rear == None:
                self.front = self.rear = temp
                return
            self.rear.next = temp
            self.rear = temp

        def deQueue(self):

            if self.isEmpty():
                return

            temp = self.front
            self.front = temp.next

            if (self.front == None):
                self.rear = None

            return temp.data

    def traverse_preorder(top):
        if top is None:
            return
        print(top)
        traverse_preorder(top.left)
        traverse_preorder(top.right)

    def traverse_queue(top):
        if top is None:
            return
        queue = Queue()
        queue.enQueue(top)
        while not queue.isEmpty():
            node = queue.deQueue()
            print(node)
            if node.left:
                queue.enQueue(node.left)
            if node.right:
                queue.enQueue(node.right)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # traverse_preorder(root) #sprawdzam, czy drzewo działa

    traverse_queue(root)


def drzewo_binarne():

    class Node:
        # wezel binarny

        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.data)

    def traverse_preorder(top):
        if top is None:
            return
        # print(top)
        traverse_preorder(top.left)
        traverse_preorder(top.right)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    traverse_preorder(root)  # sprawdzenie drzewa

    def wypisanie_drzewa(root):
        root = binarytree.Node(1)
        root.left = binarytree.Node(2)
        root.right = binarytree.Node(3)
        root.left.left = binarytree.Node(4)
        root.left.right = binarytree.Node(5)
        root.right.left = binarytree.Node(6)
        root.right.right = binarytree.Node(7)
        print(root)

    wypisanie_drzewa(root)


print("drzewo binarne przeszukane w glab z pomoca stosu")
drzewo_binarne_1()
print("drzewo binarne przeszukane w szesz za pomoca kolejki")
drzewo_binarne_2()
print("drzewo binarne ")
drzewo_binarne()
