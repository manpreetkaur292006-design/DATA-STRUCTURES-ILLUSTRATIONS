
# QUEUE USING SLL (O(1) OPERATIONS)

# IMPLEMENTING QUEUE WITH HEAD + TAIL POINTERS AND CONNECT TO BFS USAGE.

# QUEUE USING SLL :  Queue implemented on SLL with front (dequeue) and rear (enqueue) pointers. 
#                    FIFO order. Enqueue at tail O(1), dequeue at head O(1)

# ANSWER :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Dequeue from front
        self.rear = None   # Enqueue at rear (TAIL POINTER)
        self.size = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        
        # Underflow safe
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # O(1) with tail pointer!
            self.rear = new_node
        
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        if self.front is None:
            print("UNDERFLOW: Empty queue")
            return None
        
        removed = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None  # Last element removed
        
        self.size -= 1
        print(f"Dequeued: {removed}")
        return removed
    
    def front_element(self):
        return self.front.data if self.front else None
    
    def print_queue(self):
        if not self.front:
            print("Queue: Empty")
            return
        
        temp = self.front
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(f"Queue: {' → '.join(result)} (size={self.size})")

# Lab Demo
print("=== Queue using SLL (O(1) operations) ===\n")

q = Queue()

# Test sequence
print("1. Enqueue operations:")
q.enqueue(10); q.print_queue()
q.enqueue(20); q.print_queue()
q.enqueue(30); q.print_queue()

print("\n2. Dequeue + Front:")
print(f"Front: {q.front_element()}")
q.dequeue(); q.print_queue()

print("\n3. Underflow test:")
q.dequeue(); q.dequeue(); q.dequeue()  # Empty now
q.dequeue()  # UNDERFLOW

print("\n4. BFS-like usage:")
q.enqueue('A'); q.enqueue('B'); q.enqueue('C')
q.print_queue()
