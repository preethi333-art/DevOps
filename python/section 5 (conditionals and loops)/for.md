Here you go — a **clean, neat, structured cheat sheet** for **Python `for` loops**, fully aligned with the flow of your lesson.  
Includes: `for` basics, working with sequences, range(), nested loops, loop + condition, and your homework (perfect squares).

***

# ✅ Python `for` Loop — Clean & Neat Cheat Sheet

***

## 1️⃣ What is a `for` Loop?

A `for` loop is used to **iterate over sequences**, such as:

*   list
*   tuple
*   set
*   string
*   range()

It automatically:

*   picks elements **one by one**
*   stops when sequence ends
*   no need for manual increment

Unlike `while`, **no need for condition or increment**.

***

# 2️⃣ Basic Syntax

    for variable in sequence:
        statement(s)

***

# 3️⃣ Iterating Over a List

```python
x = ["Naveen", 65, 2.5]

for i in x:
    print(i)
```

Output:

    Naveen
    65
    2.5

***

# 4️⃣ Iterating Over a String

```python
for ch in "Naveen":
    print(ch)
```

Iterates character‑by‑character.

***

# 5️⃣ Using `range()`

### (A) Single argument → start=0, end=n-1

```python
for i in range(10):
    print(i)
```

→ Prints 0 to 9

***

### (B) Start & End

```python
for i in range(11, 21):
    print(i)
```

→ Prints 11 to 20

***

### (C) Start, End, Step

```python
for i in range(11, 21, 2):
    print(i)
```

→ 11, 13, 15, 17, 19

***

### (D) Reverse Loop

```python
for i in range(20, 10, -1):
    print(i)
```

→ 20 down to 11

***

# 6️⃣ `for` Loop with `if` Condition

### Skip numbers divisible by 5

```python
for i in range(1, 21):
    if i % 5 != 0:
        print(i)
```

***

# 7️⃣ Nested `for` Loops

Used for:

*   patterns
*   tables
*   combinations

Example:

```python
for i in range(5):
    for j in range(4):
        print("#", end=" ")
    print()
```

***

# 8️⃣ Differences: `while` vs `for`

| Feature              | while | for       |
| -------------------- | ----- | --------- |
| Uses condition       | Yes   | No        |
| Manual increment     | Yes   | No        |
| Works with sequences | Hard  | Very easy |
| Infinite loop risk   | High  | Low       |

Use **for** when you know **how many times** or when looping over a sequence.

***

# 9️⃣ Loop Flow (Simplified)

    for each element in sequence:
        execute block

Done automatically.

***

# 🔟 Homework (Your Task)

**Print all perfect square numbers.**

Perfect squares → 1, 4, 9, 16, 25, 36, …

### Example Solution:

```python
for i in range(1, 101):   # check 1 to 100
    if (i ** 0.5).is_integer():
        print(i)
```

Or using integer math:

```python
for n in range(1, 11):
    print(n * n)
```

***

If you want, I can also prepare:

*   a **pattern printing cheat sheet**
*   **for loop exercises**
*   **flowchart diagrams**
*   **a one‑page PDF** for revision

Just tell me!
