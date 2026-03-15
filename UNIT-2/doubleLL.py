
# DOUBLY LINKED LIST (EXTENDED OPERATIONS)

# LEARNING BIDIRECTIONAL LINKS AND CORRECT POINTER UPDATES

# DOUBLY LINKED LIST : A doubly linked list is a type of linked list where each 
#                      node contains a reference to both the next and the previous node. This 
#                      allows for efficient traversal in both directions.

# ANSWER : 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        
        temp = self.head
        forward = []
        backward = []
        
        # Forward traversal
        while temp:
            forward.append(str(temp.data))
            temp = temp.next
        
        # Backward traversal (verify prev pointers)
        temp = self.get_last()
        while temp:
            backward.append(str(temp.data))
            temp = temp.prev
        
        print("Forward:  " + " <-> ".join(forward))
        print("Backward: " + " <-> ".join(backward[::-1]))  # Reverse to match forward
        print()
    
    def get_last(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        return temp
    
    def find_target(self, target):
        """Find node with target value"""
        temp = self.head
        while temp:
            if temp.data == target:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, target, x):
        """Insert x after node containing target"""
        target_node = self.find_target(target)
        if not target_node:
            print(f"Target {target} not found")
            return False
        
        new_node = Node(x)
        new_node.next = target_node.next
        new_node.prev = target_node
        
        if target_node.next:
            target_node.next.prev = new_node
        target_node.next = new_node
        
        return True
    
    def delete_at_position(self, pos):
        """Delete node at 0-based position"""
        if not self.head:
            print("Empty list")
            return False
        
        # Find node at position
        temp = self.head
        for i in range(pos):
            if not temp:
                print("Position out of range")
                return False
            temp = temp.next
        
        if not temp:
            print("Position out of range")
            return False
        
        # Update pointers (handles head/tail correctly)
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next  # Deleting head
        
        if temp.next:
            temp.next.prev = temp.prev
            # No need to update tail explicitly (no tail pointer)
        
        print(f"Deleted: {temp.data}")
        return True

# Lab Demo
dll = DoublyLinkedList()

print("=== Doubly Linked List Demo ===\n")

# Build initial list
dll.head = Node(10)
dll.head.next = Node(20)
dll.head.next.prev = dll.head
dll.head.next.next = Node(30)
dll.head.next.next.prev = dll.head.next

print("Initial list:")
dll.print_list()

# Test insert_after
print("1. Insert 15 after 10:")
dll.insert_after(10, 15)
dll.print_list()

print("2. Insert 25 after 20:")
dll.insert_after(20, 25)
dll.print_list()

# Test delete_at_position
print("3. Delete position 1 (15):")
dll.delete_at_position(1)
dll.print_list()

print("4. Delete position 0 (head 10):")
dll.delete_at_position(0)
dll.print_list()

print("5. Delete position 2 (last node):")
dll.delete_at_position(2)
dll.print_list()
