
# SINGLY LINKED LIST (CORE OPERATIONS)

# IMPLEMENTING DYNAMIC INSERTION AND DELETION WITHOUT SHIFTING

# SINGLY LINKED LIST : Linear data structure of nodes where each node contains data 
#                      + next pointer to the next node. One-way traversal from head to tail (last node's next = null).
 
# ANSWER : 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if not self.head:
            print("List: Empty")
            return
        
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print("List: " + " → ".join(result))
    
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at beginning")
    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at end")
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at end")
    
    def delete_by_value(self, key):
        if not self.head:
            print("Empty list")
            return False
        
        # Case 1: Delete head
        if self.head.data == key:
            self.head = self.head.next
            print(f"Deleted head: {key}")
            return True
        
        # Case 2: Delete middle/tail
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                print(f"Deleted: {key}")
                return True
            temp = temp.next
        
        print(f"{key} not found")
        return False

# Lab Demo - All operations + edge cases
sll = SinglyLinkedList()

print("=== Singly Linked List Demo ===\n")

# 1. Insert at beginning
print("1. Insert begin:")
sll.insert_begin(30)
sll.insert_begin(20)
sll.insert_begin(10)
sll.traverse()

# 2. Insert at end
print("\n2. Insert end:")
sll.insert_end(40)
sll.insert_end(50)
sll.traverse()

# 3. Delete cases
print("\n3. Delete HEAD (10):")
sll.delete_by_value(10)
sll.traverse()

print("\n4. Delete MIDDLE (30):")
sll.delete_by_value(30)
sll.traverse()

print("\n5. Delete TAIL (50):")
sll.delete_by_value(50)
sll.traverse()

print("\n6. Delete NON-EXISTENT (99):")
sll.delete_by_value(99)
sll.traverse()
