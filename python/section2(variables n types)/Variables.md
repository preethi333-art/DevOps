Here is a **clean, compact Python Variables & Strings CHEAT SHEET** — perfect for quick revision 👌  
(I’ve kept it crisp, exam‑friendly, and beginner‑oriented.)

***

# 🐍 Python Variables & Strings — Cheat Sheet

## 1️⃣ Variables

### Definition

A **variable** is a container used to store data.

### Syntax

```python
variable_name = value
```

### Examples

```python
x = 2
y = 3
name = "YouTube"
```

✅ Python automatically detects the data type  
✅ No need to declare type explicitly

***

## 2️⃣ Rules for Variable Names

✅ Must start with a letter or `_`  
✅ Can contain letters, numbers, `_`  
❌ Cannot start with a number  
❌ Cannot use keywords (`if`, `for`, `while`, etc.)

✅ Valid:

```python
x, my_name, _count
```

❌ Invalid:

```python
2x, my-name, for
```

***

## 3️⃣ Assignment vs Output

Assignment:

```python
x = 5
```

🔹 No output (just stores value)

Print value:

```python
x
```

Output:

    5

***

## 4️⃣ Changing Variable Values

```python
x = 2
x = 9
```

✅ Latest value replaces the old one  
👉 Variables can **change** → hence called *variables*

***

## 5️⃣ Using Variables in Operations

```python
x = 2
y = 3
x + y
```

Output:

    5

***

## 6️⃣ Using Previous Output (`_`)

```python
x + 10     # 19
_ + y
```

Output:

    22

✅ `_` stores the **last output**

***

## 7️⃣ Variable Types (Automatic)

| Value     | Type  |
| --------- | ----- |
| `10`      | int   |
| `3.5`     | float |
| `"hello"` | str   |

Python handles type detection automatically ✅

***

## 8️⃣ Undefined Variables

```python
abc
```

❌ Error:

    NameError: name 'abc' is not defined

✅ Variables must be defined before use

***

## 9️⃣ Strings

### Creating a String

```python
name = "YouTube"
```

### Print String

```python
name
```

Output:

    YouTube

***

## 🔟 String Concatenation

```python
name + " Rocks"
```

Output:

    YouTube Rocks

⚠️ Strings must be joined using `+`

***

## 1️⃣1️⃣ String Indexing

Index starts from **0**

```python
name = "YouTube"
```

| Index | Character |
| ----- | --------- |
| 0     | Y         |
| 1     | o         |
| 2     | u         |
| 3     | T         |
| 4     | u         |
| 5     | b         |
| 6     | e         |

### Examples

```python
name[0]   # Y
name[6]   # e
```

❌ Out of range:

```python
name[8]
```

***

## 1️⃣2️⃣ Negative Indexing

Access from the **end**

```python
name[-1]   # e
name[-2]   # b
name[-7]   # Y
```

***

## 1️⃣3️⃣ String Slicing

### Syntax

```python
string[start : end]
```

📌 End index is **NOT included**

### Examples

```python
name[0:2]   # Yo
name[1:4]   # ouT
name[1:]    # ouTube
name[:4]    # YouT
```

✅ No error even if end exceeds length:

```python
name[3:10]  # Tube
```

***

## 1️⃣4️⃣ String Immutability

❌ Cannot change characters directly:

```python
name[0] = 'M'
```

✅ Create new string instead:

```python
"my" + name[3:]
```

Output:

    myTube

📌 **Strings are immutable**

***

## 1️⃣5️⃣ Length of String

```python
my_name = "Navin Reddy"
len(my_name)
```

Output:

    11

✅ `len()` is a built‑in function

***

## ✅ Quick Summary

✔ Variables store data  
✔ Value can change  
✔ Python auto‑detects type  
✔ Strings support indexing & slicing  
✔ Strings are immutable  
✔ Use `len()` for length

***

If you want next:
✅ **Printable PDF cheat sheet**  
✅ **Interview / exam questions**  
✅ **Practice programs**  
✅ **Next cheat sheet: Lists & Tuples**

Just tell me 👍

