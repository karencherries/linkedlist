# author: karen chan
# date: 11-13-24
# description: a class LinkedList that consists of numerous methods that adds, remove, insert, reverse and, check if a node contains in the
#linked list. All of these methods are written in recursion with its helper method. This class also returns a plain python list.



class Node:
    def __init__(self, data):
        """holds and initializes the stored value and next node of the linked list."""
        self.data = data
        self.next = None

class LinkedList:
    """represents an unordered linked list. Each list object of this class maintains a single reference to the head of the list."""
    def __init__(self):
        """initiates the empty linked list that initially sets the first item of the list to None for denoting
    the end of the linked list. The head of the list contains the first item of the list and hold reference to the next
    node(s)."""
        self._head = None

    def get_head(self):
        """returns the first item of the linked list."""
        return self._head

    def add(self, value):
        """calls its helper method to add a value to the end of the linked list."""
        self.add_base(value, self._head)

    def add_base(self, value, current):
        """servers as a helper method that sets the current node to be the head of the list. With the special case
        where the head is none, it creates and sets the new node as the head. It moves the current to the nodes ahead of
        current, it adds the new node at the end of the list recursively."""
        # special case: if the list is empty:
        if self._head is None:
        # creates a new node with a value and sets it as head of the list.
            self._head = Node(value)
            return
        #base case: if it reaches the end of list:
        if current.next is None:
            #creates and sets the new node at the end
            current.next = Node(value)
            return current.next

        # Recursive call: moves the current to the next node(s)
        return self.add_base(value, current.next)


    def contains(self, value):
        """calls its helper method to check if a value is present in the linked list."""
        return self.contains_node(value, self._head)

    def contains_node(self, value, current):
        """By initially setting the head as the current, it recursively moves the current one node ahead,
        and it returns true if it finds the value in the linked list. If not,
        it returns false."""
        # special case: if empty list and if it reaches the end of the list, return false
        if self._head is None or current is None:
            return False

        #base case: if value is found, return True
        if current.data == value:
            return True

        #recursive call: if not empty list or value is not found, it moves the current one node ahead.
        return self.contains_node(value, current.next)

    def remove(self, value):
        """calls its helper method to remove a value from the linked list."""
        self.rec_remove(value, None, self._head)

    def rec_remove(self, value, previous, current):
        """By initially setting the head to be the current node of the linked list, it recursively removes a value by checking
        whether the node has a previous node. If it does not, the node that is removed is a head. """
        #special case: if it is empty list, just return.
        if self._head is None:
            return
        #base case: if value is found in current, it sets the head as the current.next.
        if current.data == value:
            if previous is None:
                #it sets the current.next as the head.
                self._head = current.next
                return
            if previous is not None:
                #remove a node that is not the head. It sets the former current.next node as previous.next.
                previous.next = current.next
                return
        #recursive call: when the value is not found, it moves the current to the next node(s) ahead
        if current.data != value:
            self.rec_remove(value, current, current.next)


    def insert(self, value, pos):
        """calls its helper method to insert a value at the given position in the linked list."""
        self.rec_insert(value, pos, self._head)

    def rec_insert(self, value, pos, current):
        """ By initially setting the head as the current node of the linked list, it recursively inserts a value at the
        given position in the linked list."""
        #special case: if the list is empty, adds the new node with given value.
        if self._head is None:
            self.add(value)
            return

        #special case: if inserting at pos == 0, insert new node prior to the head.
        if pos == 0:
            temp = self._head
            self._head = Node(value)
            self._head.next = temp
            return
        #if the pos is larger or equal to one:
        if pos >= 1:
            # if no more nodes ahead of current node:
            if current.next is None:
                #it sets the new node as the current.next, which is one node ahead of current.
                current.next = Node(value)
                return
        #if position is equal to one:
        if pos == 1:
            #if there are node(s) ahead of current node
            if current.next is not None:
                #place the new node ahead of formerly current.next.
                temp = current.next
                current.next = Node(value)
                current.next.next = temp
                return
        #if pos is larger or equal to 2:
        if pos >=2:
            #if there are node(s) ahead of current node
            if current.next is not None:
                #recursive call decrement the position by 1 and moves the current to one node ahead
                return self.rec_insert(value, pos-1, current.next)

    def reverse(self):
        """calls its helper method to reverse the linked list."""
        return self.rec_reverse(None, self._head)

    def rec_reverse(self, previous, current):
        """reverses the linked list recursively"""
        #if it reaches to the end of the list
        if current is None:
            #set the previous to head
            self._head = previous
        # otherwise
        if current is not None:
            #  resetting the rest of the nodes after "following" from the cycle: current.next and previous
            following = current.next
            current.next = previous
            #recursively calls the cycle by moving one node ahead, which is previous to current, current to following in the cycle.
            return self.rec_reverse(current, following)


    def to_plain_list(self):
        """calls its helper method to convert the linked list to a python plain list."""
        return self.rec_to_plain_list(self._head)

    def rec_to_plain_list(self, current):
        """recursively converts the linked list to a python plain list by initially setting the head as the current node."""
        result = []
        #special case: empty list, just return
        if self._head is None:
            return
        # base case: if it reaches the end of list, return the result.
        if current is None:
            return result
        # recursive call: concatenate the data of current node with the data of the next current node. It also moves
        #current to the node(s) ahead
        if current is not None:
            return  [current.data] + self.rec_to_plain_list(current.next)

















