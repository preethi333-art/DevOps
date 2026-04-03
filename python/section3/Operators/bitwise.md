Here’s a **clear, neat, beginner‑friendly Bitwise Operators cheat sheet** that explains **what**, **why**, and **how**, matching the flow of your video exactly.  
This is perfect for **notes, revision, and first‑time understanding** ✅

***

# ✅ Python Bitwise Operators — Clean Cheat Sheet

***

## 🔹 What Are Bitwise Operators?

Bitwise operators work **on bits (0s and 1s)** instead of whole numbers.

✅ Used internally by computers  
✅ Important for **low‑level programming, system design, networking**  
✅ Requires understanding of **binary numbers**

***

## 🔢 Binary Reminder

*   Decimal → Binary example

<!---->

    12  →  1100
    13  →  1101

***

## 🧩 List of Bitwise Operators

| Operator    | Name         | Symbol |    |
| ----------- | ------------ | ------ | -- |
| Complement  | NOT          | `~`    |    |
| AND         | Bitwise AND  | `&`    |    |
| OR          | Bitwise OR   | \`     | \` |
| XOR         | Exclusive OR | `^`    |    |
| Left Shift  | Shift left   | `<<`   |    |
| Right Shift | Shift right  | `>>`   |    |

***

## 1️⃣ Bitwise Complement (`~`)

### Meaning

*   Reverses **each bit**
*   `0 → 1`
*   `1 → 0`

### Example

```python
~12
```

✅ Output:

```python
-13
```

### Why `-13`?

Python uses **Two’s Complement** to represent negative numbers.

### Rule

    ~N = -(N + 1)

So:

    ~12 = -(12 + 1) = -13

✅ Common shortcuts:

```python
~0  = -1
~1  = -2
```

***

## 2️⃣ Bitwise AND (`&`)

### Rule

    1 & 1 = 1
    else = 0

### Example

```python
12 & 13
```

### Binary:

    12 → 1100
    13 → 1101
    -------------
         1100  → 12

✅ Output:

```python
12
```

***

## 3️⃣ Bitwise OR (`|`)

### Rule

    If any bit is 1 → result is 1

### Example

```python
12 | 13
```

### Binary:

    1100
    1101
    ----
    1101  → 13

✅ Output:

```python
13
```

***

## 4️⃣ Bitwise XOR (`^`)

### Rule

*   Same bits → `0`
*   Different bits → `1`
*   “Odd number of 1s → 1”

### Example

```python
12 ^ 13
```

### Binary:

    1100
    1101
    ----
    0001 → 1

✅ Output:

```python
1
```

✅ Shortcut:

```text
Same → 0
Different → 1
```

***

## 5️⃣ Left Shift (`<<`)

### Meaning

*   Shifts bits **to the left**
*   Adds zeros on the right
*   Equivalent to multiplying by powers of 2

### Formula

    N << k = N × (2^k)

### Example

```python
10 << 2
```

### Binary:

    10 → 1010
    Shift left by 2 → 101000

✅ Output:

```python
40
```

***

## 6️⃣ Right Shift (`>>`)

### Meaning

*   Shifts bits **to the right**
*   Loses bits
*   Equivalent to dividing by powers of 2

### Formula

    N >> k = N ÷ (2^k)

### Example

```python
10 >> 2
```

### Binary:

    1010 → 10
    Right shift by 2 → 10

✅ Output:

```python
2
```

***

## 🧠 One‑Look Summary

| Operation | Effect                                |            |
| --------- | ------------------------------------- | ---------- |
| `~N`      | Negates number using two’s complement |            |
| `A & B`   | Common 1‑bits only                    |            |
| \`A       | B\`                                   | All 1‑bits |
| `A ^ B`   | Different bits only                   |            |
| `N << k`  | Multiply by `2^k`                     |            |
| `N >> k`  | Divide by `2^k`                       |            |

***

## 🎯 Why Bitwise Operators Matter

✅ Used in **bitwise masks**  
✅ Used in **encryption & compression**  
✅ Core part of **interview questions**  
✅ Required for **low‑level & performance‑critical code**

***

## 📝 Practice (Homework)

Try manually:

*   `~45`
*   `25 & 30`
*   `25 ^ 30`
*   `8 << 3`
*   `64 >> 4`

***

If you want, I can:
✅ convert this into a **1‑page PDF**
✅ create **visual diagrams**
✅ prepare **bitwise interview questions**
✅ link this to **real‑life use cases**

Just say the word 🚀
