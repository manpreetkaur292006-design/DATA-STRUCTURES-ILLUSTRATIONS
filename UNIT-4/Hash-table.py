class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]  
    
    def hash_key(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_key(key)
        bucket = self.table[index]
        
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        print(f"Inserted ({key}:{value}) → bucket {index}")
    
    def get(self, key):
        index = self.hash_key(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self.hash_key(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                removed = bucket.pop(i)
                print(f"Deleted ({removed[0]}:{removed[1]}) from bucket {index}")
                return True
        print(f"Key {key} not found")
        return False
    
    def display(self):
        print("\n=== Hash Table Buckets ===")
        for i in range(self.size):
            if self.table[i]:
                items_str = ', '.join([f"{k}:{v}" for k, v in self.table[i]])
                print(f"[{i}]: {items_str}")
            else:
                print(f"[{i}]: empty")

pairs = [(10, 'apple'), (7, 'banana'), (14, 'cherry'), (3, 'date'), (17, 'elderberry')]

ht = HashTable(size=7)
print("Table size:", ht.size)

for key, value in pairs:
    ht.insert(key, value)

ht.display()

print("\n=== Get Tests ===")
print("get(7):", ht.get(7))
print("get(14):", ht.get(14))
print("get(99):", ht.get(99))

print("\n=== Delete Tests ===")
ht.delete(7) 
ht.delete(20) 
ht.display()
print("get(7) after delete:", ht.get(7))