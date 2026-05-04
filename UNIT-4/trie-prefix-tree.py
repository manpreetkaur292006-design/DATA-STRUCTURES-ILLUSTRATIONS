class TrieNode:
    def __init__(self):
        self.children = {}          
        self.is_end_of_word = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print(f"Inserted: '{word}'")
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

words = ["cat", "car", "card", "care", "dog", "do", "dot"]

trie = Trie()
print("=== Inserting Words ===")
for word in words:
    trie.insert(word)

test_words = ["car", "care", "dog", "cats"]
print("\n=== Exact Search (search()) ===")
for word in test_words:
    result = trie.search(word)
    print(f"search('{word}') → {result}")

test_prefixes = ["ca", "do", "car", "xyz"]
print("\n=== Prefix Match (startsWith()) ===")
for prefix in test_prefixes:
    result = trie.starts_with(prefix)
    print(f"startsWith('{prefix}') → {result}")