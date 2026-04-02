Here is a **clean, compact, easy‑to‑revise CHEAT SHEET** for **Python Lists**, made directly from your lecture content 👇  
(Perfect for beginners, quick revision, and interviews.)

***

# 🐍 Python Lists — Cheat Sheet

***

## 1️⃣ What is a List?

*   A **list** is a collection of multiple values
*   Similar to arrays in C / C++ / Java
*   Can store **different data types**
*   **Ordered** (index-based)
*   **Mutable** (can be modified)

✅ Very flexible compared to arrays in other languages

***

## 2️⃣ Creating a List

### Syntax

```python
list_name = [value1, value2, value3]
```

### Example

```python
nums = [25, 12, 36, 95, 14]
```

Print list:

```python
nums
```

***

## 3️⃣ Accessing Elements (Indexing)

📌 Index starts from **0**

```python
nums[0]   # 25
nums[4]   # 14
```

### Negative Indexing

```python
nums[-1]   # Last element → 14
nums[-5]   # First element → 25
```

***

## 4️⃣ List Slicing

### Syntax

```python
list[start : end]
```

⚠️ End index is **NOT included**

### Examples

```python
nums[2:]      # [36, 95, 14]
nums[1:4]     # [12, 36, 95]
nums[:3]      # [25, 12, 36]
```

✅ Works like string slicing

***

## 5️⃣ List with Strings

```python
names = ["Navin", "Kiran", "John"]
```

Access:

```python
names[0]   # Navin
```

***

## 6️⃣ List with Multiple Data Types

✅ Python allows mixed data types

```python
values = [9.5, "Navin", 25]
```

(float + string + integer)

***

## 7️⃣ List of Lists (Nested Lists)

```python
nums = [25, 12, 36]
names = ["Navin", "Kiran"]

mil = [nums, names]
```

Access:

```python
mil[0]       # nums list
mil[1][0]    # "Navin"
```

***

## 8️⃣ Mutability of List ✅

Lists are **mutable** → values can be changed

```python
nums[1] = 77
```

***

## 9️⃣ Important List Methods

### ➕ Add Elements

**append()** → adds at end

```python
nums.append(45)
```

**insert()** → adds at specific index

```python
nums.insert(2, 77)
```

**extend()** → adds multiple elements

```python
nums.extend([29, 12, 14, 6])
```

⚠️ Must use `[ ]` while extending

***

### ➖ Remove Elements

**remove()** → removes by value

```python
nums.remove(14)
```

**pop(index)** → removes by index

```python
nums.pop(1)
```

**pop()** → removes last element

```python
nums.pop()
```

**del** → removes multiple values

```python
del nums[2:5]
```

***

### 🧹 Clear List

```python
nums.clear()
```

***

## 🔟 Built‑in Functions for Lists

```python
min(nums)     # Minimum value
max(nums)     # Maximum value
sum(nums)     # Sum of elements
len(nums)     # Number of elements
```

***

## 1️⃣1️⃣ Sorting a List

```python
nums.sort()
```

✅ Sorts in ascending order  
⚠️ Modifies the original list

***

## 1️⃣2️⃣ Stack Concept (LIFO)

*   append() → push
*   pop() → pop

```python
nums.append(100)
nums.pop()    # removes last added element
```

✅ Used in stack & data structures

***

## ✅ Key Features Summary

✔ Ordered  
✔ Indexing supported  
✔ Allows duplicates  
✔ Allows mixed data types  
✔ Mutable (editable)  
✔ Many built‑in methods

***

## 🧠 One‑Line Definition

**List = Ordered + Mutable + Collection of values**

***

If you want next:
✅ **PDF / printable cheat sheet**  
✅ **Practice programs**  
✅ **Interview questions**  
✅ **Next topic: Tuple & Set Cheat Sheet**

Just tell me 👍
