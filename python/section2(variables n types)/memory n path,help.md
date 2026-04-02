Here is a **neat, clear, and exam‑ready CHEAT SHEET** covering **Python Variables (Memory Model), `id()`, Constants, `type()`**, and **Python Command Line + Help System**, exactly based on the content you shared.

***

# 🐍 Python Cheat Sheet

## Variables, Memory, ID, Constants, CMD & Help

***

## 1️⃣ Variables & Memory Model

### Variable Creation

```python
num = 5
```

✅ In Python, a variable is **not a box**  
✅ A variable is a **reference (tag)** pointing to an **object in memory**

***

## 2️⃣ Objects & Memory Address (`id()`)

Every value in Python is an **object**.

### Get Memory Address

```python
id(num)
```

✅ `id()` returns the **memory address** of the object  
✅ Same object → same `id`

***

## 3️⃣ Multiple Variables → Same Object

```python
a = 10
b = a
```

Check values:

```python
a   # 10
b   # 10
```

Check addresses:

```python
id(a)
id(b)
```

✅ Both have **same memory address**  
✅ Python does **NOT create duplicate objects**  
✅ Improves **memory efficiency**

***

## 4️⃣ Objects Exist Independently of Variable Names

```python
id(10)
```

✅ Object `10` has its own memory  
✅ Variables `a`, `b`, `k` are just **tags**

```python
k = 10
id(k)   # same id as a and b
```

***

## 5️⃣ Changing Variable Value

```python
a = 9
```

✅ New object is created  
✅ `a` now points to `9`  
✅ `b` still points to `10`

```python
id(a) != id(b)
```

***

## 6️⃣ Multiple References Example

```python
a = 9
k = a
```

✅ `a` and `k` → same object (`9`)  
✅ `b` still → `10`

***

## 7️⃣ Unused Objects & Garbage Collection

```python
b = 8
```

Now:

*   `a`, `k` → `9`
*   `b` → `8`
*   No variable points to `10`

✅ Object `10` becomes **eligible for garbage collection**  
✅ Python removes unused objects automatically

***

## 8️⃣ Variables as Tags (Important Concept)

✅ Variables are **tags / references**  
✅ Objects live in memory independently  
✅ Many variables can refer to **one object**

***

## 9️⃣ Constants in Python

🔴 Python has **NO true constants**

### Convention (Intention Only)

```python
PI = 3.14
```

✅ CAPITAL letters indicate “do not change”  
❌ Python does **not** prevent reassignment

```python
PI = 3.15   # Allowed (but bad practice)
```

***

## 🔟 Checking Variable Type (`type()`)

```python
type(PI)
```

Output:

    <class 'float'>

Examples:

```python
type(10)        # int
type(3.5)       # float
type("Navin")   # str
```

✅ `type()` tells the **data type of object**

***

## 1️⃣1️⃣ Everything Is an Object

✔ Integers  
✔ Strings  
✔ Floats  
✔ Variables

✅ Everything has:

*   Type
*   Identity (`id`)
*   Value

***

# 🖥 Python Command Prompt (CMD)

***

## 1️⃣2️⃣ Running Python in Command Prompt

If this fails:

```bash
python
```

Error:

    'python' is not recognized

✅ Python is installed  
❌ Path is not set

***

## 1️⃣3️⃣ Setting Python Path (Permanent)

### Steps (Windows)

1.  Go to **Environment Variables**
2.  Edit **Path** under *System Variables*
3.  Add:
        C:\Users\<username>\AppData\Local\Programs\Python\PythonXX\
        C:\Users\<username>\AppData\Local\Programs\Python\PythonXX\Scripts\
4.  Restart CMD

✅ Now:

```bash
python
```

Works ✅

***

## 1️⃣4️⃣ Checking Python

```python
2 + 3
```

Output:

    5

```python
print("Hello World")
```

✅ Python is working

***

# 📘 Python Help System

***

## 1️⃣5️⃣ Using `help()`

```python
help()
```

✅ Opens interactive help mode

***

## 1️⃣6️⃣ Exploring Topics

```python
topics
```

Lists available topics & modules

***

## 1️⃣7️⃣ Help on Specific Topic

Inside help:

```python
list
```

OR directly:

```python
help('list')
```

✅ Shows:

*   Methods
*   Syntax
*   Documentation
*   Version info

***

## 1️⃣8️⃣ Exit Help

```python
quit
```

***

## ✅ Quick Summary

### Variables & Memory

✔ Variables are references  
✔ Objects live in memory  
✔ Same value → same object  
✔ `id()` shows address  
✔ Garbage collection removes unused objects

### Constants

✔ No true constants  
✔ Use CAPITAL names as convention

### CMD & Help

✔ Set PATH to use python in CMD  
✔ `help()` replaces books  
✔ Docs + practice = mastery

***

## 🧠 One‑Line Takeaway

**Python variables don’t store values — they reference objects.**

***

If you want next:
✅ **Printable PDF cheat sheet**  
✅ **Data Types Cheat Sheet**  
✅ **Interview Questions (Variables & Memory)**  
✅ **Objects & Garbage Collection explained visually**

Just tell me 👍
