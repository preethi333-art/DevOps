Here is a **clean, neat, structured, beginner‑friendly cheat sheet** for **IF, ELSE, ELIF, nested IF, indentation, and decision making in Python** — exactly matching your video flow and adding whatever is missing for complete clarity.  
Use this as your ultimate **decision‑making reference** in Python.

***

# ✅ Python Decision‑Making Cheat Sheet

*(IF, ELSE, ELIF, Nested IF, Indentation — neat & clear)*

***

## 1️⃣ Why Do We Need IF?

Computers don’t “think” — we make them think by giving **conditions**.

In real life:

*   If it rains → take umbrella
*   If score > 35 → pass
*   If age < 18 → not eligible

In Python, we use:

    if  CONDITION:
        STATEMENT

***

## 2️⃣ IF Statement

### Syntax

    if condition:
        statement(s)

### Example

```python
if True:
    print("I am right")
```

Output:

    I am right

If condition is **False**, the block does NOT run.

***

## 3️⃣ Indentation (VERY IMPORTANT)

Indentation = tells Python **which statements belong to IF**.

Rules:

*   Default indentation = **4 spaces** (or 1 tab)
*   All statements inside the same IF must have **same indentation**

Correct:

```python
if x > 10:
    print("Big")
    print("Number")
```

Incorrect:

```python
if x > 10:
    print("Big")
   print("Number")   # ❌ wrong indentation
```

***

## 4️⃣ IF with Expressions

We rarely use `True` or `False` directly.

Example: Even or Odd

```python
x = 8
r = x % 2

if r == 0:
    print("Even")
```

***

## 5️⃣ IF–ELSE (Choose 1 out of 2)

### Syntax

    if condition:
        statements
    else:
        statements

### Example

```python
x = 9
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

***

## 6️⃣ Nested IF (IF inside IF)

Used when conditions depend on previous results.

```python
x = 8

if x % 2 == 0:
    print("Even")
    if x > 5:
        print("Great")
    else:
        print("Not so great")
```

***

## 7️⃣ IF–ELIF–ELSE (Multiple Conditions)

Use when you have **many exclusive options**.

### Syntax

    if condition1:
        block1
    elif condition2:
        block2
    elif condition3:
        block3
    else:
        default_block

### Example

```python
x = 3

if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
else:
    print("Wrong input")
```

Behavior:

*   Checks top to bottom
*   Executes the **first matching** condition
*   Skips the rest

***

## 8️⃣ Common Mistakes to Avoid

❌ Writing multiple IFs when conditions are related  
✔ Use IF–ELIF–ELSE instead

❌ Wrong indentation  
✔ Keep all statements aligned correctly

❌ Using `=` instead of `==`  
✔ `=` is assignment  
✔ `==` is comparison

Example mistake:

```python
if x = 5:   # ❌ invalid
```

Correct:

```python
if x == 5:  # ✔ valid
```

***

## 9️⃣ When to Use What?

| Situation                          | Use            |
| ---------------------------------- | -------------- |
| Only one condition                 | `if`           |
| Two possible paths                 | `if–else`      |
| Many paths, only one should match  | `if–elif–else` |
| Condition inside another condition | Nested `if`    |

***

## 🔟 Real‑World Style Example

```python
age = 20

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

***

## ⭐ Bonus: Truthy & Falsy Values in IF

Python treats some values as **False automatically**:

*   `0`
*   `""` (empty string)
*   `[]` (empty list)
*   `None`
*   `False`

Example:

```python
if "":
    print("Runs")         # Does not run
else:
    print("Empty")        # Runs
```

***

## 📌 Ultra‑Short Summary

*   IF → check condition
*   ELSE → default action
*   ELIF → multiple checks
*   Nested IF → conditions inside conditions
*   Indentation → defines blocks
*   Use `==` for comparison
*   Python evaluates truth values automatically

***

If you want, I can also prepare:
✅ a printable **PDF version**  
✅ flowchart diagrams for IF/ELSE  
❇️ practice problems with solutions  
🎯 mini‑projects using conditions (calculator, login system, grade checker)

Just tell me!
