Here is a **clear, concise, beginner‑friendly CHEAT SHEET** for **Python Data Types**, created directly from your lecture content and organized for **quick revision, exams, and interviews** ✅

***

# 🐍 Python Data Types — Cheat Sheet

***

## ✅ Why Data Types Matter

*   Data types define **how data is stored**
*   They decide **what operations are allowed**
*   Wrong data type handling → **bugs & errors**

***

## 📌 Built‑in Python Data Types

Python has **5 major categories** of data types:

1.  **None**
2.  **Numeric**
3.  **Sequence**
4.  **Set**
5.  **Mapping (Dictionary)**

***

## 1️⃣ None Type

### What is `None`?

*   Represents *no value*
*   Similar to `null` in other languages

```python
x = None
```

Check type:

```python
type(x)
```

Output:

    <class 'NoneType'>

✅ Used when variable has **no meaningful value yet**

***

## 2️⃣ Numeric Data Types

### Types under Numeric:

*   `int`
*   `float`
*   `complex`
*   `bool`

***

### 🔢 Integer (`int`)

```python
x = 5
type(x)
```

Output:

    <class 'int'>

***

### 🔢 Float (`float`)

```python
x = 2.5
type(x)
```

Output:

    <class 'float'>

***

### 🔢 Complex (`complex`)

Form:

    a + bj

```python
x = 6 + 9j
type(x)
```

✅ `j` represents √-1

***

### 🔁 Type Conversion (Casting)

```python
a = 5.6
b = int(a)      # 5
```

```python
k = float(b)    # 5.0
```

```python
c = complex(5, 6)   # 5 + 6j
```

✅ Possible conversions:

*   float → int
*   int → float
*   int → complex

***

### ✅ Boolean (`bool`)

Values:

```python
True
False
```

Example:

```python
5 < 6     # True
5 > 6     # False
```

Conversion:

```python
int(True)    # 1
int(False)   # 0
```

✅ Boolean is treated as **numeric**

*   `True` → `1`
*   `False` → `0`

***

## 3️⃣ Sequence Data Types

### Includes:

*   `list`
*   `tuple`
*   `string`
*   `range`

***

### 📋 List

*   Ordered
*   Mutable
*   Allows duplicates

```python
nums = [25, 26, 45, 12]
type(nums)
```

***

### 🔒 Tuple

*   Ordered
*   Immutable

```python
t = (25, 26, 45)
type(t)
```

***

### 🔤 String (`str`)

*   Collection of characters
*   No separate `char` type in Python

```python
name = "Navin"
type(name)
```

```python
ch = 'A'
type(ch)   # still string
```

✅ Single character = string

***

### 🔄 Range

Used for iteration

```python
r = range(10)
```

Convert to list:

```python
list(range(10))
```

Output:

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

With step:

```python
list(range(2, 11, 2))
```

Output:

    [2, 4, 6, 8, 10]

***

## 4️⃣ Set Data Type

*   Unordered
*   No duplicate values

```python
s = {25, 26, 25, 45}
type(s)
```

Output:

    {25, 26, 45}

✅ Uses **curly brackets**
✅ Fast lookup

***

## 5️⃣ Mapping Data Type (Dictionary)

### What is Dictionary?

*   Stored as **key : value**
*   Keys must be **unique**
*   Access by key (not index)

```python
d = {
    "Navin": "Samsung",
    "Rahul": "iPhone",
    "Kiran": "OnePlus"
}
```

Type:

```python
type(d)
```

***

### Access Value

```python
d["Rahul"]
```

OR

```python
d.get("Kiran")
```

***

### Dictionary Methods

```python
d.keys()
d.values()
d.items()
```

***

## ✅ Data Types Summary Table (Text)

*   **NoneType** → None
*   **Numeric** → int, float, complex, bool
*   **Sequence** → list, tuple, string, range
*   **Set** → set
*   **Mapping** → dictionary

***

## 🧠 One‑Line Takeaway

**Data types control how your data behaves, moves, and computes in Python.**

***

If you want next:
✅ **PDF printable cheat sheet**
✅ **Practice programs**
✅ **Interview questions**
✅ **Next topic: Operators Cheat Sheet**

Just tell me 👍
