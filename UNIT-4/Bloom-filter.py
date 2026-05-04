class BloomFilter:
    def __init__(self, size=20, hash_count=3):
        self.size = size         
        self.hash_count = hash_count  
        self.bit_array = [0] * size  
        
    def _hash_functions(self, item):
        hashes = []
        for i in range(self.hash_count):
            h = 0
            for char in item:
                h = (h * 31 + ord(char) + i * 17) % self.size
            hashes.append(h)
        return hashes
    
    def insert(self, item):
        for h in self._hash_functions(item):
            self.bit_array[h] = 1
        print(f"Inserted '{item}' → bits {self._hash_functions(item)} set to 1")
    
    def query(self, item):
        for h in self._hash_functions(item):
            if self.bit_array[h] == 0:
                return "DEFINITELY NOT present"
        return "POSSIBLY present (false positive possible)"
    
    def display(self):
        print("Bit array:", ''.join(map(str, self.bit_array)))

items_to_insert = ["cat", "car", "dog"]
test_queries = ["cat", "dog", "bat", "car"]

bf = BloomFilter(size=20, hash_count=3)
print("Bloom Filter: size=20 bits, k=3 hashes\n")

print("=== Insert Phase ===")
for item in items_to_insert:
    bf.insert(item)

bf.display()

print("\n=== Query Phase ===")
for item in test_queries:
    result = bf.query(item)
    print(f"'{item}' → {result}")

print("\n=== False Positive Demo ===")
print("'bat' never inserted but hashes overlap → 'POSSIBLY present'")
print("Real check: bat →", bf.query("bat"))