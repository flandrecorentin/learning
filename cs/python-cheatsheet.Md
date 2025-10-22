# List

````python
lst = [12, 34, 56]
lst.append(78)          # Add to end
lst.extend([911, 1213]) # Extend with iterable
lst.sort()              # In-place sort
sorted_lst = sorted(lst) # New sorted list
lst.pop(2)              # Remove by index
sublist = lst[1:-1]     # Slice [start:end:step]
reversed_lst = lst[::-1] # Reverse
squares = [x**2 for x in lst if x % 2 == 0] # List comprehension
````

# Tuple

````python
point = (3, 5, 7)
x, y, z = point         # Unpack
point.count(5)          # Count occurrences
point.index(7)          # Find index
````


# Dictionary

````python
person = {"name": "Alice", "age": 30}
person.get("name")      # Safe access (returns None if missing)
person.get("job", "President") # Default value
person.update({"job": "Engineer"}) # Add/Update multiple
person.pop("city")      # Remove key
for key, value in person.items(): # Iterate
    print(key, value)

````

# Set

````python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.add(7)            # Add element
set_a.remove(3)         # Remove (raises KeyError if missing)
set_a.discard(3)        # Remove (no error if missing)
set_a.union(set_b)      # Union
set_a & set_b           # Intersection
set_a - set_b           # Difference
````

# String

````python
text = "  hello, world!  "
clean_text = text.strip()       # Remove whitespace
split = clean_text.split(", ")  # Split into list
joined = "--".join(split)       # Join with delimiter
new_text = clean_text.replace("world", "python") # Replace
sub_text = new_text[:3] + "--" + new_text[7:]    # Slice + concat
chartoint = ord(text[0]) - ord('a')
````

# Collections

````python
from collections import deque, defaultdict, Counter

# Deque (double-ended queue)
queue = deque()
queue.append("first")   # Push / Add to right
queue.popleft()         # Pop / Remove from left
queue[0]                # Peek / Check left
len(queue) == 0         # isEmpty 

# We can manage stack with []
stack = []
stack.append("first")    # Push / Add to right
stack.pop()              # Pop / Remove from right
stack[-1]                # Peek / Check right
len(stack) == 0          # isEmpty

# DefaultDict
dd = defaultdict(int)   # Default value for missing keys
dd["key"] += 1

# Counter
counts = Counter("hello") # {'h':1, 'e':1, 'l':2, 'o':1}
````

# File/Error handling

````python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    raise Excetion("Custom exception")
except Exception as e:
    print(f"Unexpected: {e}")
finally:
    print("Always runs")
````

# Functional programming helping

````python
nums = [3, 1, 2]
sorted_nums = sorted(nums)                     # [1, 2, 3]
mapped = list(map(lambda n: n * 2, nums))      # [6, 2, 4]
filtered = list(filter(lambda n: n % 2, nums)) # [3, 1] (odd numbers)
zipped = list(zip([1, 2], ["a", "b"]))         # [(1, 'a'), (2, 'b')]
````

# OOP

````python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

# Decorators
# Use __variable_name to insinuate private
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
````

# Date/Time / request

````python
from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)  # Add 7 days
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # Format
parsed = datetime.strptime("2024-01-15", "%Y-%m-%d")  # Parse


import requests

# GET
response = requests.get("https://api.github.com/users/octocat", headers={"User-Agent": "MyApp"})
data = response.json()

# POST
post_data = {"name": "John", "email": "john@example.com"}
response = requests.post("https://httpbin.org/post", json=post_data)
````

# Appendix 

````python
import math
import random

math.sqrt(16)      # 4.0
random.randint(1, 10)  # Random int between 1 and 10
maxi = max(list) # or max(int1, int2)
mini = min(list) # or mini(int1, int2)
absolue = abs(-13)


import re

text = "Hello 123 world 456"
match = re.search(r'\d+', text)   # First match
numbers = re.findall(r'\d+', text) # All matches
new_text = re.sub(r'\d+', 'X', text) # Replace all matches
````
