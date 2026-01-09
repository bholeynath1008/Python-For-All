### Python Data Structures: Notes on List, Set, and Dictionary
#### List
**Overview:**  
A `list` is an ordered, mutable collection of elements, allowing duplicates. It's like a dynamic array, indexed by position (0-based). Ideal for sequences where order matters.

**Key Characteristics:**  
- **Ordered:** Elements maintain insertion order.  
- **Mutable:** Modify in place (add, remove, change).  
- **Allows Duplicates:** Same element can appear multiple times.  
- **Heterogeneous:** Can hold mixed types (e.g., ints, strings).  
- **Time Complexities:**  
  | Operation | Average Case | Worst Case |  
  |-----------|--------------|------------|  
  | Access by index | O(1) | O(1) |  
  | Append | O(1) | O(n) (amortized) |  
  | Insert/Delete at start | O(n) | O(n) |  
  | Insert/Delete at end | O(1) | O(1) |  
  | Search | O(n) | O(n) |  

**Creation and Basic Operations:**  
```python
# Creation
my_list = [1, 2, 2, 'a']  # Or list('abc') → ['a', 'b', 'c']

# Access/Modify
print(my_list[0])  # 1
my_list[1] = 3     # [1, 3, 2, 'a']

# Common Methods
my_list.append(4)                # [1, 3, 2, 'a', 4]
my_list.extend([5, 6])           # [1, 3, 2, 'a', 4, 5, 6]
my_list.insert(1, 'new')         # Insert at index 1
popped = my_list.pop(0)          # Remove and return by index (default: last)
my_list.remove(2)                # Remove first occurrence of value
sorted_list = sorted(my_list)    # New sorted list (original unchanged)
my_list.reverse()                # In-place reverse

# Slicing
subset = my_list[1:4]            # Elements 1 to 3
reversed_slice = my_list[::-1]   # Reverse copy
```

**Use Cases:**  
- Storing ordered data (e.g., shopping cart items).  
- Stacks/queues (with `append`/`pop`).  
- Iterating with indices: `for i, item in enumerate(my_list):`.  
**Pros:** Flexible, readable. **Cons:** Slow for frequent inserts/deletes in middle.

#### Set
**Overview:**  
A `set` is an unordered, mutable collection of unique elements. No indexing—great for membership tests and removing duplicates. Based on hash tables for fast lookups.

**Key Characteristics:**  
- **Unordered:** No guaranteed order (Python 3.7+ insertion order for dicts, but sets are truly unordered).  
- **Mutable:** Add/remove elements, but elements must be hashable (immutable types like ints, strings).  
- **No Duplicates:** Automatically unique.  
- **Heterogeneous:** Mixed hashable types.  
- **Time Complexities:**  
  | Operation | Average Case | Worst Case |  
  |-----------|--------------|------------|  
  | Add | O(1) | O(n) |  
  | Remove | O(1) | O(n) |  
  | Membership (in) | O(1) | O(n) |  
  | Union/Intersection | O(len(smaller)) | O(len(smaller)) |  

**Creation and Basic Operations:**  
```python
# Creation
my_set = {1, 2, 2, 'a'}  # {1, 2, 'a'} (duplicates removed)
empty_set = set()        # {} is a dict, not set!

# Access (no indexing; use 'in')
print(1 in my_set)       # True

# Common Methods
my_set.add(3)            # {1, 2, 'a', 3}
my_set.remove(2)         # Error if not found; use discard() for safe
my_set.discard('a')      # No error if missing
my_set.pop()             # Remove/return arbitrary element
my_set.clear()           # Empty set

# Set Operations (returns new sets)
union = my_set | {3, 4}              # {1, 2, 'a', 3, 4}
intersection = my_set & {2, 3}       # {2}
difference = my_set - {1}            # {'a', 2, 3}
symmetric_diff = my_set ^ {1, 4}     # {2, 3, 4} (unique to each)
is_subset = {1, 2} <= my_set         # True if subset
```

**Use Cases:**  
- Removing duplicates: `unique = list(set(my_list))`.  
- Fast lookups (e.g., user IDs in a system).  
- Mathematical sets (union for merging datasets).  
**Pros:** Fast membership, auto-unique. **Cons:** No order/indexing; can't store lists/tuples as elements.

#### Dictionary (Dict)
**Overview:**  
A `dict` is an unordered (Python 3.7+: insertion-ordered), mutable mapping of unique keys to values. Keys must be hashable; values can be anything. Like a real dictionary: key → definition.

**Key Characteristics:**  
- **Ordered (3.7+):** Maintains insertion order.  
- **Mutable:** Modify keys/values.  
- **Unique Keys:** Duplicates overwrite.  
- **Heterogeneous:** Keys/values mixed types (keys immutable).  
- **Time Complexities:**  
  | Operation | Average Case | Worst Case |  
  |-----------|--------------|------------|  
  | Get/Set | O(1) | O(n) |  
  | Delete | O(1) | O(n) |  
  | Length | O(1) | O(1) |  
  | Iterate | O(n) | O(n) |  

**Creation and Basic Operations:**  
```python
# Creation
my_dict = {'a': 1, 'b': 2, 'a': 3}  # {'a': 3, 'b': 2} (last wins)
from_lists = dict(zip(['a', 'b'], [1, 2]))  # {'a': 1, 'b': 2}

# Access/Modify
print(my_dict['a'])      # 3 (KeyError if missing)
value = my_dict.get('c', 'default')  # 'default' (safe)
my_dict['c'] = 4         # Add/update

# Common Methods
my_dict.pop('b')         # Remove by key, return value (2)
keys = my_dict.keys()    # dict_keys view: {'a', 'c'}
values = my_dict.values()  # dict_values view: [3, 4]
items = my_dict.items()   # dict_items view: [('a', 3), ('c', 4)]
my_dict.update({'d': 5}) # Merge/update from another dict
len(my_dict)             # 2

# Iteration
for key in my_dict:      # Keys
    print(key, my_dict[key])  # a 3, c 4
for k, v in my_dict.items():
    print(k, v)
```

**Use Cases:**  
- Key-value storage (e.g., user: {id: 1, name: 'Alice'}).  
- Counting frequencies: `from collections import Counter`.  
- JSON-like data handling.  
**Pros:** Fast lookups by key, flexible. **Cons:** Keys must be hashable; memory overhead for sparse data.

#### Comparisons: List vs. Set vs. Dict
| Feature | List | Set | Dict |  
|---------|------|-----|------|  
| **Order** | Yes | No (unordered) | Yes (3.7+) |  
| **Duplicates** | Yes | No | Keys: No; Values: Yes |  
| **Indexing/Access** | By index | Membership only | By key |  
| **Best For** | Sequences | Uniques/Lookups | Mappings |  
| **Memory** | Compact for dense | Hash overhead | Hash + pairs |  
| **Iteration** | Ordered | Arbitrary | Ordered (keys) |  

**Tips:**  
- Convert between: `set(list_dict.keys())` for unique keys.  
- For large data: Use `defaultdict` (from `collections`) for auto-default values.  
- Common Pitfall: Mutable elements in sets/dicts (e.g., lists) can't be keys since unhashable.  
Practice: Use `help(list)` in Python REPL for more!

### Beginner Level (Questions 1-7)

#### 1. List - Sum of Elements
**Question:** Write a Python function that takes a list of integers as input and returns the sum of all elements.  
**Example:** `sum_list([1, 2, 3, 4])` should return `10`.

**Notes:**  
This is a straightforward use of the built-in `sum()` function, which is efficient for summing iterables.

**Solution:**
```python
def sum_list(arr):
    return sum(arr)

# Test
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
```

**Explanation:** The built-in `sum()` function iterates over the list and adds up all elements efficiently in O(n) time.

#### 2. String - Palindrome Check
**Question:** Write a function to check if a given string is a palindrome (reads the same forwards and backwards, ignoring case and spaces).  
**Example:** `"A man a plan a canal Panama"` should return `True`.

**Notes:**  
Note: The initial code snippet had a bug: `word[::1] == word[::-1]` where `[::1]` is identical to the original string. Proper cleaning (lowercase, remove spaces) is essential for real palindromes.

**Solution:**
```python
def palindrome_check(word):
    # Clean the string: remove spaces and convert to lowercase
    cleaned = ''.join(word.lower().split())
    # Compare forward and reversed
    return cleaned == cleaned[::-1]

# Test
print(palindrome_check("A man a plan a canal Panama"))  # Output: True
```

**Explanation:** First, clean the string by removing spaces and converting to lowercase using `lower().split()` and `join()`. Then, compare it to its reverse slice `[::-1]`. This handles case-insensitivity and ignores non-alphabetic characters if extended.

#### 3. Dictionary - Create from Lists
**Question:** Write a function that takes two lists (one for keys, one for values) and returns a dictionary pairing them.  
**Example:** `create_dict(['a', 'b'], [1, 2])` should return `{'a': 1, 'b': 2}`.

**Notes:**  
`zip(keys, values)`: This takes the two lists and "zips" them together like a zipper, creating an iterator of tuples: `('a', 1)` and `('b', 2)`.  
`dict(...)`: The dictionary constructor takes those tuples and converts the first item into a key and the second into a value.

**Solution:**
```python
def create_dict(keys, values):
    return dict(zip(keys, values))

# Test
print(create_dict(['a', 'b'], [1, 2]))  # Output: {'a': 1, 'b': 2}
```

**Explanation:** `zip(keys, values)` pairs elements into tuples like `('a', 1)`, `('b', 2)`. `dict()` converts these tuples into key-value pairs. Assumes lists are of equal length; otherwise, extra elements are ignored.

#### 4. Set - Union Operation
**Question:** Write a function to find the union of two sets and return it as a sorted list.  
**Example:** `union_sets({1, 2, 3}, {3, 4, 5})` should return `[1, 2, 3, 4, 5]`.

**Notes:**  
The `'|'` operator performs the union.  
`sorted()` takes the resulting set and returns a sorted list.  
Set Operations Table:  
| Operation | Symbol | Python Method | Result in Example |  
|-----------|--------|---------------|-------------------|  
| Union (All items) | s1 \| s2 | s1.union(s2) | {1, 2, 3, 4, 5, 6} |  
| Intersection (Only overlaps) | s1 & s2 | s1.intersection(s2) | set() (empty) |  
| Difference (Items in s1 not in s2) | s1 - s2 | s1.difference(s2) | {1, 2, 3} |

**Solution:**
```python
def union_sets(set_a, set_b):
    # The '|' operator performs the union
    # sorted() takes the resulting set and returns a sorted list
    return sorted(set_a | set_b)

# Test
print(union_sets({1, 2, 3}, {3, 4, 5}))  # Output: [1, 2, 3, 4, 5]
```

**Explanation:** The `|` operator computes the union (all unique elements from both sets). `sorted()` converts the result to a list in ascending order. Time complexity: O(n log n) due to sorting.

#### 5. List - Reverse In Place
**Question:** Write a function to reverse a list in place (without creating a new list).  
**Example:** Input `[1, 2, 3]` should become `[3, 2, 1]`.

**Notes:**  
While `my_list[::-1]` is great for strings or when you need a new list, it actually creates a copy of the data in memory. To strictly follow the "in place" requirement, `reverse()` or the swapping method are the correct choices.

**Solution:**
```python
def reverse_in_place(my_list):
    my_list.reverse()  # This modifies the original list and returns None
    return my_list

# Test
nums = [1, 2, 3]
reverse_in_place(nums)
print(nums)  # Output: [3, 2, 1]
```

**Explanation:** The `reverse()` method modifies the list in place (O(n) time, O(1) space). Avoid slicing `[::-1]` as it creates a new list, violating the "in place" requirement.

#### 6. String - Vowel Count
**Question:** Write a function to count the number of vowels (a, e, i, o, u) in a string, case-insensitive.  
**Example:** `"Hello World"` should return `3`.

**Notes:**  
`if char in vowels:` This is a very fast membership test in Python.  
Generator expression: The optimized version uses a generator inside `sum()` for conciseness.  
Dictionary Approach Extension: For per-vowel counts, initialize `{v: 0 for v in vowels}` and increment specific keys; filter out zeros with `{k: v for k, v in counts.items() if v > 0}`.

**Solution:**
```python
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    # Convert text to lowercase once to make it case-insensitive
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Test
print(count_vowels("Hello World"))  # Output: 3
```

**Alternative Optimized Version:**
```python
def count_vowels_short(text):
    vowels = "aeiou"
    # This creates a 1 for every vowel found and sums them up
    return sum(1 for char in text.lower() if char in vowels)

# Test
print(count_vowels_short("Hello World"))  # Output: 3
```

**Explanation:** Loop through lowercase characters and check membership in the vowels string (fast O(1) check). The generator version is more Pythonic and concise, still O(n) time.

#### 7. Dictionary - Value Lookup
**Question:** Write a function that takes a dictionary and a key, returning the value if the key exists, else `"Key not found"`.  
**Example:** `lookup({1: 'one'}, 1)` should return `'one'`.

**Notes:**  
`.get()` takes two arguments: the key to find, and the default value to return if it doesn't exist.  
Why use `.get()` instead of `my_dict[key]`? In Python, dictionaries are essentially Hash Tables. When you try to access a key that isn't there using square brackets, the program crashes with a `KeyError`.  
Safety: `.get()` prevents your program from crashing if a key is missing.

**Solution:**
```python
def lookup(my_dict, key):
    # .get() takes two arguments: the key to find, 
    # and the default value to return if it doesn't exist.
    return my_dict.get(key, "Key not found")

# Test cases
my_data = {1: 'one', 2: 'two'}
print(lookup(my_data, 1))    # Output: 'one'
print(lookup(my_data, 5))    # Output: 'Key not found'
```

**Manual Version (for understanding):**
```python
def lookup_manual(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return 'Key Not Found'

# Test
print(lookup_manual(my_data, 2))  # Output: 'two'
```

**Explanation:** `dict.get(key, default)` safely retrieves values without raising `KeyError` on missing keys. The manual `if key in my_dict` is equivalent but more verbose. Both are O(1) time.

### Intermediate Level (Questions 8-13)

#### 8. List - Remove Duplicates
**Question:** Write a function to remove duplicates from a list while preserving the original order (use a set for efficiency).  
**Example:** `remove_duplicates([1, 2, 2, 3, 1])` should return `[1, 2, 3]`.

**Notes:**  
To remove duplicates while preserving the order, we need to keep track of what we have already seen. Using a set is the most efficient way to do this because looking up an item in a set (an "existence check") is incredibly fast.  
The "Seen" Set Pattern: We loop through the list, and for every item, we check if it's in our seen set. If it isn't, we add it to both our result list and our set.  
Efficiency Comparison:  
| Method | Preserves Order? | Speed (Time Complexity) |  
|--------|------------------|-------------------------|  
| list(set(items)) | No | O(n) |  
| Nested Loops | Yes | O(n^2) (Slow) |  
| "Seen" Set | Yes | O(n) (Fast) |  
`dict.fromkeys()`: Creates keys in order; duplicates are automatically ignored (Python 3.7+).

**Solution:**
```python
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Test
print(remove_duplicates([1, 2, 2, 3, 1]))  # Output: [1, 2, 3]
```

**Alternative Pythonic Version (Python 3.7+):**
```python
def remove_duplicates_fast(items):
    # dict.fromkeys creates keys in order; duplicates are automatically ignored
    return list(dict.fromkeys(items))

# Test
print(remove_duplicates_fast([1, 2, 2, 3, 1]))  # Output: [1, 2, 3]
```

**Explanation:** Use a "seen" set for O(1) lookups to track uniques while building the result list (preserves order, O(n) time). `dict.fromkeys()` leverages dict insertion order (stable since Python 3.7) for a concise alternative. Avoid `list(set(items))` as it scrambles order.

#### 9. String - Anagram Check
**Question:** Write a function to check if two strings are anagrams of each other (same characters, same frequencies).  
**Example:** `"listen"` and `"silent"` should return `True`.

**Notes:**  
Method Comparison:  
| Method | Logic | Time Complexity | Best For |  
|--------|-------|-----------------|----------|  
| Sorting | sorted(s1) == sorted(s2) | O(n log n) | Coding interviews (simple to explain) |  
| Counting | Counter(s1) == Counter(s2) | O(n) | High-performance applications |  
Clean strings: Lowercase and remove spaces for robustness.

**Solution:**
```python
from collections import Counter

def is_anagram_fast(str1, str2):
    # Clean the strings
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    
    # Counter creates a frequency dictionary: {'l': 1, 'i': 1, ...}
    return Counter(s1) == Counter(s2)

# Test
print(is_anagram_fast("Heart", "Earth"))  # Output: True
```

**Sorting-Based Version:**
```python
def is_anagram_sort(str1, str2):
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

# Test
print(is_anagram_sort("listen", "silent"))  # Output: True
```

**Explanation:** Clean strings (lowercase, remove spaces). `Counter` builds frequency dicts for O(n) comparison. Sorting is O(n log n) but simpler for interviews. Both ignore length mismatches implicitly via equality check.

#### 10. Dictionary - Frequency Counter
**Question:** Write a function that takes a string and returns a dictionary with character frequencies.  
**Example:** `char_freq("hello")` should return `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`.

**Notes:**  
`Counter` from `collections` is ideal for frequency counting as it auto-increments. Manual version uses conditional increment. Make case-insensitive with `lower()`.

**Solution:**
```python
from collections import Counter

def char_freq(text):
    return dict(Counter(text.lower()))

# Test
print(char_freq("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

**Manual Version:**
```python
def char_freq_manual(text):
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Test
print(char_freq_manual("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

**Explanation:** `Counter` is a dict subclass that auto-increments counts (O(n) time). Manual version uses `if-else` for same logic. Case-insensitive via `lower()`.

#### 11. Set - Symmetric Difference
**Question:** Write a function to find the symmetric difference between two sets (elements in exactly one set).  
**Example:** `sym_diff({1, 2, 3}, {3, 4, 5})` should return `{1, 2, 4, 5}`.

**Notes:**  
Symmetric difference: Elements unique to each set, i.e., `(a - b) | (b - a)`. Use `^` operator for brevity.

**Solution:**
```python
def sym_diff(set_a, set_b):
    # '^' is the symmetric difference operator
    return set_a ^ set_b

# Alternative: (a - b) | (b - a)
def sym_diff_manual(set_a, set_b):
    return (set_a - set_b) | (set_b - set_a)

# Test
print(sym_diff({1, 2, 3}, {3, 4, 5}))  # Output: {1, 2, 4, 5}
```

**Explanation:** `^` computes symmetric difference (union of differences) in O(n) time. Manual version uses `-` for difference and `|` for union, equivalent but more explicit.

#### 12. List - Second Largest
**Question:** Write a function to find the second largest number in a list of integers (handle duplicates and small lists).  
**Example:** `second_largest([3, 1, 4, 1, 5])` should return `4`.

**Notes:**  
Handle edges: Return `None` for lists < 2 elements. Use `set` to dedupe, sort descending. For O(n) optimization, track max/second_max in one pass.

**Solution:**
```python
def second_largest(nums):
    if len(nums) < 2:
        return None  # Or raise an error
    unique_sorted = sorted(set(nums), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None

# Test
print(second_largest([3, 1, 4, 1, 5]))  # Output: 4
print(second_largest([1]))  # Output: None
```

**Explanation:** Convert to set to remove duplicates, sort descending, return index 1. Handles edge cases (len < 2). O(n log n) due to sort; for O(n), use two variables to track max/second_max in one pass.

#### 13. Dictionary - Merge Dicts
**Question:** Write a function to merge two dictionaries, summing values for duplicate keys.  
**Example:** `merge_dicts({'a': 1}, {'a': 2, 'b': 3})` should return `{'a': 3, 'b': 3}`.

**Notes:**  
Use `Counter` for easy summation on overlaps. Manual: Copy first dict, then update/add from second. Assumes numeric values.

**Solution:**
```python
from collections import Counter

def merge_dicts(dict1, dict2):
    combined = Counter(dict1) + Counter(dict2)  # Counters add overlapping values
    return dict(combined)

# Manual Version
def merge_dicts_manual(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

# Test
print(merge_dicts({'a': 1}, {'a': 2, 'b': 3}))  # Output: {'a': 3, 'b': 3}
```

**Explanation:** `Counter` treats dicts as multisets and `+` sums overlaps (O(n) time). Manual version copies first dict and updates/adds from second. Assumes numeric values.

### Advanced Level (Questions 14-20)

#### 14. String - Longest Substring Without Repeating
**Question:** Write a function to find the length of the longest substring without repeating characters (use a sliding window with a set).  
**Example:** `"abcabcbb"` should return `3` (for "abc").

**Notes:**  
Sliding window technique: Use left/right pointers and a set for O(1) duplicate checks. Shrink window on repeats.

**Solution:**
```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

**Explanation:** Sliding window: Expand right pointer, shrink left if duplicate found (using set for O(1) checks). Track max window size. O(n) time, O(min(n, charset)) space.

#### 15. List - Two Sum (Interview Classic)
**Question:** Given a list of integers and a target, return indices of two numbers that add up to the target (use a dict for O(n) time).  
**Example:** `two_sum([2, 7, 11, 15], 9)` should return `[0, 1]`.

**Notes:**  
Hash map for complements: Store num:index, check `target - num` in map. Assumes unique solution.

**Solution:**
```python:disable-run
def two_sum(nums, target):
    seen = {}  # key: num, value: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No solution

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```
### Advanced Level (Continued: Questions 16-20)

#### 16. Dictionary - LRU Cache Implementation
**Question:** Implement an LRU (Least Recently Used) Cache class using a dict and doubly linked list (or OrderedDict for simplicity). Support get and put operations.  
**Example:** Cache with capacity 2; put(1,1), put(2,2), get(1) → 1, put(3,3), get(2) → -1.

**Notes:**  
LRU: Evict least recently used on overflow. OrderedDict simplifies with `move_to_end` and `popitem(last=False)`.  
Full impl: Use dict + DLL (nodes for O(1) add/remove/move). Head/tail dummies for edges.  
Time: O(1) get/put. Space: O(capacity).  
Interview tip: Draw DLL; explain why hash + order needed. Test capacity=0 or full hits.

**Solution:**
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)
print(cache.get(2))  # Output: -1
```

**Explanation:** `OrderedDict` maintains insertion order; `move_to_end` updates recency, `popitem(last=False)` evicts LRU. O(1) for get/put. For full doubly linked list, implement nodes, but OrderedDict simplifies.

#### 17. String - Group Anagrams (Interview Classic)
**Question:** Given a list of strings, group the anagrams together (use a dict with sorted string as key).  
**Example:** `["eat", "tea", "tan", "ate", "nat", "bat"]` should return `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`.

**Notes:**  
Key: Sorted string or tuple(sorted(s)) for hashing. defaultdict(list) for grouping.  
Time: O(n * m log m) where m=avg length (sort per string). Space: O(n*m).  
Alternative: Char count tuple as key (26-letter array) for O(n*m).  
Interview tip: Handle empty strings; return any order of groups.

**Solution:**
```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))  # Sorted tuple as key
        groups[key].append(s)
    return list(groups.values())

# Test
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Explanation:** Sort each string as a key in a defaultdict (anagrams share same sorted key). Append originals to lists. O(n * m log m) time (n strings, m avg length).

#### 18. List - Rotate Array (Interview Classic)
**Question:** Write a function to rotate a list to the right by k steps (in place, O(1) space).  
**Example:** `rotate([1,2,3,4,5], 2)` should become `[4,5,1,2,3]`.

**Notes:**  
Juggling: Reverse full, then prefix/k-suffix. k %= n for large k.  
Alternatives: Temp array O(n) space, or block swaps O(1) space.  
Time: O(n), Space: O(1).  
Interview tip: Mod in place; test k=0, k>n, n=1.

**Solution:**
```python
def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle k > n
    # Reverse full array
    nums.reverse()
    # Reverse first k
    nums[:k] = nums[:k][::-1]
    # Reverse rest
    nums[k:] = nums[k:][::-1]

# Test (modifies in place)
nums = [1, 2, 3, 4, 5]
rotate(nums, 2)
print(nums)  # Output: [4, 5, 1, 2, 3]
```

**Explanation:** Juggling algorithm: Reverse entire, then prefix/suffix. O(n) time, O(1) space. `k %= n` handles large k. Alternative: Use temp array, but violates space.

#### 19. String - Valid Palindrome II (Interview Classic)
**Question:** Given a string, determine if it can be a palindrome by removing at most one character (use two pointers).  
**Example:** `"abca"` should return `True` (remove 'b' to get "aca").

**Notes:**  
Two pointers: On mismatch, try skip left or right (recursive or iterative). Limit to one skip.  
Time: O(n), Space: O(1) iterative.  
Edge cases: Even/odd length, multiple mismatches.  
Interview tip: Discuss recursion depth (O(n) worst, but branches limit to 2).

**Solution:**
```python
def valid_palindrome_ii(s):
    def helper(left, right):
        while left < right:
            if s[left] != s[right]:
                # Try skipping left or right
                return helper(left + 1, right) or helper(left, right - 1)
            left += 1
            right -= 1
        return True
    
    return helper(0, len(s) - 1)

# Test
print(valid_palindrome_ii("abca"))  # Output: True
```

**Explanation:** Two pointers from ends; on mismatch, recurse skipping one side (at most one skip via `or`). O(n) time (linear with branching depth 2). Handles odd/even lengths.

#### 20. List/Dict - FizzBuzz with Memoization (Interview Classic Variation)
**Question:** Write a function to generate the FizzBuzz sequence up to n (use a dict for memoized Fibonacci-like extension if n is large). But focus on: Print numbers 1 to n, replacing multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz". Extend to count frequencies using a dict.  
**Example:** For n=15, output includes "FizzBuzz" at 15.

**Notes:**  
Check order: 15 first, then 3, then 5 to avoid overlap. Dict for counts.  
Memo extension: If fib-integrated, use `@lru_cache` for recursive fib(n) mod checks.  
Time: O(n), Space: O(1) for core, O(n) for list. Interview: Extend to multiples of other nums.

**Solution:**
```python
def fizzbuzz(n):
    freq = {'Fizz': 0, 'Buzz': 0, 'FizzBuzz': 0}
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
            freq['FizzBuzz'] += 1
        elif i % 3 == 0:
            result.append("Fizz")
            freq['Fizz'] += 1
        elif i % 5 == 0:
            result.append("Buzz")
            freq['Buzz'] += 1
        else:
            result.append(str(i))
    print('\n'.join(result))
    return freq

# Test
print(fizzbuzz(15))
# Output: Prints sequence up to 15, and freq dict e.g. {'Fizz': 4, 'Buzz': 2, 'FizzBuzz': 1}
```

**Explanation:** Check divisibility in order (15 first for overlap). Build list for output, track counts in dict. O(n) time. For memoization extension (e.g., if generating Fibonacci FizzBuzz), use `@lru_cache` on a recursive fib function, but core is the loop.
