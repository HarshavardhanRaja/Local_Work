# why build other data structures instead of using built ds that comes with the language?
    # Each DS solves a particulat problem
    # cost of common operatoions on arrays:
        # accessing the elemens: o(1)
        # inserting: O(n)
        # deleting: O(n)
    # to sum up arrays are good at accessing but not very at inserting/deleting


# If we are trying to solve a problem that involves far more inserts/ delets than accessing then LL can be better tool than array
 

# what is a linked list
"""
LL is a linear DS where each element in list is contained in a seperate object called node.
Node models 2 pices of information: An individual item/value of data we want to store and 
                                    Reference to the next node in the list
    First node is called head
    Last node is called a tail and denotes end of the list. It doesnot points to anything i.e it's reference position is empty 
    List only maintains a reference to the head node
    in some implementations it stores reference to tail as well
    Nodes are also called self referential objects

Two types of LL:
    Singly linked list: where each node stores reference to next node in list
    Doubly linked list: Stores reference to both node before and node after in the list
"""





from typing import Counter


class Node:
    # An object for storing a single node of linked list 
    # models two attributes - data and the link to next node in the list
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: {0}, reference: {1}>".format(self.data, id(self.next_node))


class LinkedList:
    # singly linkedlist 

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        # Returns the number of nodes in the list. O(n)
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        # Adds a new node containing data at the head of the list. O(1)
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node 


    def search(self, key):
        """
        Search for the first node containing data that matches the key 
        Returns the node or none  if not found
        takes O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        insertion takes O(1)
        but finding the node at insertion point takes O(n)
        
        overall O(n)
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position>1 : 
                current = Node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node


    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the Node or None if key doesn't exsit
        Takes O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif  current.data == key:
                found = True
                previous.next_node = current.next_node
            else :
                previous = current
                current = current.next_node
        return current


    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: {0}, {1}]".format(current.data, id(current.next_node)))
            elif current.next_node is None:
                nodes.append("[Tail: {0}, {1}]".format(current.data, current.next_node))
            else:
                nodes.append("[{0}, {1}]".format(current.data, id(current.next_node)))

            current = current.next_node
        return '-> '.join(nodes)


"""
# python -i LinkedLists.py
n1 = Node(10)
print(n1)
n2 = Node(20)
n1.next_node = n2
print(n1.next_node)
"""

l = LinkedList()
l.add(29)
l.add(22)
l.add(45)
l.add(56)
print(l)

