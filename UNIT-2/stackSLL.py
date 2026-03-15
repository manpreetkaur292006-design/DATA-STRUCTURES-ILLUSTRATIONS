
# STACK USING SLL + PARENTHESES CHECKER

# BUILDING STACK USING LINKED LIST AND APPLY TO BRACKET VALIDATIONS.

# STACK USING SLL : Stack implemented on top of SLL where top pointer = stack top. 
#                   Push/pop at head (O(1)). LIFO order using SLL nodes.

# ANSWER :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        return self.top.data if self.top else None
    
    def is_empty(self):
        return self.top is None

def is_valid_parentheses(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs:  # Closing bracket
            top = stack.pop()
            if top != pairs[char]:
                return False
        else:  # Opening bracket
            stack.push(char)
    
    return stack.is_empty()

# Lab Demo
print("=== Stack using SLL + Parentheses Checker ===\n")

# Test Stack Operations
stack = Stack()
print("Stack Operations:")
stack.push(10); print("Push 10")
stack.push(20); print("Push 20")
stack.push(30); print("Push 30")
print(f"Peek: {stack.peek()}")
print(f"Pop: {stack.pop()}")
print(f"Peek: {stack.peek()}\n")

# Test Parentheses Checker
test_cases = [
    "()", "(())", "({[]})",  # Valid
    ")(", "(()", "([)]",     # Invalid
    "", "abc", "((()))"      # Edge cases
]

print("Parentheses Validation:")
for s in test_cases:
    result = is_valid_parentheses(s)
    print(f"'{s}' → {result}")
