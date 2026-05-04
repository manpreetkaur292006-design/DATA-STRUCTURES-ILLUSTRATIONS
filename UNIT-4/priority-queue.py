import heapq

class MinHeapPQ:
    def __init__(self):
        self.heap = []
    
    def insert(self, priority):
        heapq.heappush(self.heap, priority)
    
    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None
    
    def extract_min(self):
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        return None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def get_heap_state(self):
        temp_list = []
        # Manual copy - no list comprehension
        for i in range(len(self.heap)):
            temp_list.append(self.heap[i])
        return temp_list

priorities = [5, 2, 8, 1, 9, 3, 4, 6, 7, 0]

pq = MinHeapPQ()

print("Inserting priorities:", priorities)

for priority in priorities:
    pq.insert(priority)

print("\nHeap state after all inserts:", pq.get_heap_state())
print("Peek (minimum priority):", pq.peek())

print("\nExtraction sequence (verifies min-heap correctness):")
extracted_list = []

while pq.is_empty() == False:
    min_priority = pq.extract_min()
    extracted_list.append(min_priority)
    
    print("Extracted:", min_priority, "Remaining heap:", pq.get_heap_state())

print("\nFull extracted order:", extracted_list)
print("Heap empty:", pq.is_empty())