Here is a **NEAT, CLEAR & BEGINNER‑FRIENDLY CHEAT SHEET** for **Python Lists, Tuples, and Sets**, based exactly on the content you shared.

***

# 🐍 Python Collections Cheat Sheet

## List ✅ | Tuple 🔒 | Set ⚡

***

## 1️⃣ List

### What is a List?

*   Collection of multiple values
*   Can store **different data types**
*   **Mutable** → values can be changed

### Creating a List

```python
nums = [21, 36, 14, 25]
```

### Accessing Elements (Indexing)

```python
nums[0]   # 21
nums[2]   # 14
```

### Modifying List Values ✅

```python
nums[1] = 99
```

### Common List Methods

```python
nums.append(50)
nums.remove(14)
nums.pop()
nums.insert(1, 100)
nums.sort()
len(nums)
```

✅ Order is maintained  
✅ Duplicate values allowed

***

## 2️⃣ Tuple

### What is a Tuple?

*   Collection of values **similar to list**
*   **Immutable** → values CANNOT be changed
*   Faster than list (better performance)

### Creating a Tuple

```python
tup = (21, 36, 14, 25)
```

### Accessing Tuple Elements

```python
tup[1]   # 36
```

### Trying to Modify ❌

```python
tup[1] = 30
```

❌ Error:

    TypeError: 'tuple' object does not support item assignment

### Available Tuple Methods

```python
tup.count(21)   # counts occurrences
tup.index(14)   # returns index
```

❌ No append  
❌ No remove  
❌ No replace

✅ Use tuple when values **should not change**

***

## 3️⃣ Set

### What is a Set?

*   Collection of **unique elements**
*   **Unordered** → no fixed sequence
*   Duplicate values are automatically removed
*   Faster element access (uses hashing)

### Creating a Set

```python
s = {21, 14, 25, 5}
```

### Duplicate Values Removed

```python
s = {25, 14, 98, 63, 98}
```

Output:

    {98, 14, 25, 63}

✅ No duplicates  
✅ Order is NOT guaranteed

***

### No Indexing in Set ❌

```python
s[0]
```

❌ Error:

    TypeError: 'set' object is not subscriptable

***

### Modifying a Set ✅

```python
s.add(100)
s.remove(14)
s.discard(25)
```

✅ Values can be added or removed  
❌ Cannot update a specific position (no index)

***

## 4️⃣ Key Differences (Quick Comparison)

| Feature    | List      | Tuple     | Set           |
| ---------- | --------- | --------- | ------------- |
| Brackets   | `[ ]`     | `( )`     | `{ }`         |
| Ordered    | ✅ Yes     | ✅ Yes     | ❌ No          |
| Mutable    | ✅ Yes     | ❌ No      | ✅ Yes         |
| Duplicates | ✅ Allowed | ✅ Allowed | ❌ Not Allowed |
| Indexing   | ✅ Yes     | ✅ Yes     | ❌ No          |
| Speed      | Normal    | Faster    | Fastest       |

***

## 5️⃣ When to Use What?

✅ **List**

*   When data changes frequently
*   When order matters

✅ **Tuple**

*   When data should NOT change
*   For fixed configuration values
*   Faster iteration

✅ **Set**

*   When uniqueness is required
*   When order does not matter
*   For fast searching

***

## ✅ One‑Line Summary

*   **List** → Changeable & ordered
*   **Tuple** → Fixed & ordered
*   **Set** → Unique & unordered

***

If you want next:
✅ **Printable PDF cheat sheet**  
✅ **Interview questions**  
✅ **Coding practice problems**  
✅ **Next topic: Dictionary cheat sheet**

Just tell me 👍
