Here’s a **neat, clean, and beginner‑friendly Python Operators Cheat Sheet**, based exactly on what you covered in the video 👇  
You can use this for **quick revision** or **notes**.

***

# ✅ Python Operators – Quick Cheat Sheet

***

## 1️⃣ Arithmetic Operators

Used to perform basic mathematical operations.

| Operator | Meaning             | Example  | Output |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `2 + 3`  | `5`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `3 * 4`  | `12`   |
| `/`      | Division            | `10 / 2` | `5.0`  |
| `%`      | Modulus (remainder) | `10 % 3` | `1`    |

```python
x = 2
y = 3

x + y   # 5
x - y   # -1
x * y   # 6
x / y   # 0.666...
x % y   # 2
```

***

## 2️⃣ Assignment Operators

Used to assign and update values.

### Basic Assignment

```python
x = 8
```

### Shorthand Assignment

| Operator | Meaning           | Example  | Same As     |
| -------- | ----------------- | -------- | ----------- |
| `+=`     | Add & assign      | `x += 2` | `x = x + 2` |
| `-=`     | Subtract & assign | `x -= 2` | `x = x - 2` |
| `*=`     | Multiply & assign | `x *= 3` | `x = x * 3` |
| `/=`     | Divide & assign   | `x /= 2` | `x = x / 2` |

```python
x = 4
x += 2   # 6
x *= 3   # 18
```

### Multiple Assignment (One Line)

```python
a, b = 5, 6
```

***

## 3️⃣ Unary Operators

Operate on **one operand**.

### Negation (`-`)

```python
n = 7
n = -n
print(n)   # -7
```

***

## 4️⃣ Relational (Comparison) Operators

Used to **compare values**. Output is always `True` or `False`.

| Operator | Meaning               | Example  | Output |
| -------- | --------------------- | -------- | ------ |
| `<`      | Less than             | `5 < 6`  | `True` |
| `>`      | Greater than          | `6 > 5`  | `True` |
| `==`     | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 6` | `True` |
| `<=`     | Less than or equal    | `5 <= 5` | `True` |
| `>=`     | Greater than or equal | `6 >= 5` | `True` |

```python
a = 5
b = 6

a < b    # True
a == b   # False
a != b   # True
```

***

## 5️⃣ Logical Operators

Used to **combine conditions**.

| Operator | Meaning                                    |
| -------- | ------------------------------------------ |
| `and`    | True if **both** conditions are true       |
| `or`     | True if **at least one** condition is true |
| `not`    | Reverses the result                        |

### AND (`and`)

```python
a = 5
b = 4

a < 8 and b < 5   # True
a < 8 and b < 2   # False
```

✅ Both conditions must be `True`

***

### OR (`or`)

```python
a < 8 or b < 2   # True
```

✅ At least **one condition** must be `True`

***

### NOT (`not`)

```python
x = True
not x   # False
```

✅ Reverses the result

***

## 🔁 Truth Table (Quick Reference)

### AND

| A     | B     | A and B |
| ----- | ----- | ------- |
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

### OR

| A     | B     | A or B |
| ----- | ----- | ------ |
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

***

## 🚀 Key Takeaways

*   Arithmetic → Math operations
*   Assignment → Storing & updating values
*   Unary → Single value operation
*   Relational → Comparisons (`True / False`)
*   Logical → Combine conditions (`and`, `or`, `not`)

These operators are **building blocks** for:

*   `if` conditions
*   loops
*   real-world Python programs

***

If you want, I can also:
✅ turn this into **PDF notes**  
✅ add **real interview questions**  
✅ create **practice problems**

Just tell me 😄
