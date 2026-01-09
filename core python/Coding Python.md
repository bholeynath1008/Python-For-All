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

### Advanced Level (Questions 14-20)

#### 14. String - Longest Substring Without Repeating
**Question:** Write a function to find the length of the longest substring without repeating characters (use a sliding window with a set).  
**Example:** `"abcabcbb"` should return `3` (for "abc").

**Notes:**  
Sliding window technique: Use left/right pointers and a set for O(1) duplicate checks. Shrink window on repeats.  
Edge cases: Empty string (return 0), all unique chars (return len(s)), all repeats (return 1).  
Space: O(min(n, charset size)), e.g., 26 for lowercase letters.  
Interview tip: Explain "two pointers" and why set > dict for simple existence.

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
Brute force: Nested loops O(n^2), but hash optimizes to O(n).  
Edge cases: No solution (return []), duplicates (first occurrence).  
Interview tip: Discuss trade-offs if indices must be unique or multiple pairs.

**Solution:**
```python
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

**Explanation:** Dict stores seen numbers and indices. For each num, check if `target - num` was seen (O(1) lookup). Single pass, O(n) time/space. Assumes exactly one solution.

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
