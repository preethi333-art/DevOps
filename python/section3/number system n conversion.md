Here’s a **clean, neat, and exam‑/interview‑ready cheat sheet** for **Number Systems & Binary Formats in Python**, based exactly on the concepts explained in your video — no extra noise, just clarity ✅

***

# ✅ Number Systems & Binary Formats — Python Cheat Sheet

***

## 1️⃣ Common Number Systems

| System          | Base | Digits Used | Where It’s Used           |
| --------------- | ---- | ----------- | ------------------------- |
| **Decimal**     | 10   | `0–9`       | Daily life, math          |
| **Binary**      | 2    | `0, 1`      | Computers, memory         |
| **Octal**       | 8    | `0–7`       | Low‑level systems         |
| **Hexadecimal** | 16   | `0–9, A–F`  | MAC address, IPv6, colors |

***

## 2️⃣ Python Built‑In Functions (Decimal → Other Systems)

### Decimal → Binary

```python
bin(25)
```

✅ Output:

```python
'0b11001'
```

***

### Decimal → Octal

```python
oct(25)
```

✅ Output:

```python
'0o31'
```

***

### Decimal → Hexadecimal

```python
hex(25)
```

✅ Output:

```python
'0x19'
```

***

## 3️⃣ Meaning of Prefixes

| Prefix | Number System |
| ------ | ------------- |
| `0b`   | Binary        |
| `0o`   | Octal         |
| `0x`   | Hexadecimal   |

✅ These prefixes tell Python **how to interpret the number**

***

## 4️⃣ Convert Other Systems Back to Decimal

### Binary → Decimal

```python
0b101
```

✅ Output:

```python
5
```

***

### Octal → Decimal

```python
0o31
```

✅ Output:

```python
25
```

***

### Hexadecimal → Decimal

```python
0xA
```

✅ Output:

```python
10
```

```python
0xF
```

✅ Output:

```python
15
```

***

## 5️⃣ Manual Conversion: Decimal → Binary (Concept)

### Example: Convert **25 (Decimal)** to Binary

1.  Divide by 2 repeatedly
2.  Note **remainders**
3.  Read remainders **bottom → top**

| Division | Quotient | Remainder |
| -------- | -------- | --------- |
| 25 ÷ 2   | 12       | 1         |
| 12 ÷ 2   | 6        | 0         |
| 6 ÷ 2    | 3        | 0         |
| 3 ÷ 2    | 1        | 1         |
| 1 ÷ 2    | 0        | 1         |

✅ Binary = **11001**

***

## 6️⃣ Manual Conversion: Binary → Decimal

### Example: `11001`

Write powers of 2 (right → left):

    1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 1×2⁰

<!---->

    = 16 + 8 + 0 + 0 + 1
    = 25

✅ Decimal value = **25**

***

## 7️⃣ Power Rule (Binary → Decimal)

| Position      | Power |
| ------------- | ----- |
| Rightmost bit | 2⁰    |
| Next          | 2¹    |
| Next          | 2²    |
| …             | …     |

✅ Ignore **0 bits**, calculate only **1 bits**

***

## 8️⃣ Why This Topic Is Important

✔ Foundation for **bitwise operators**  
✔ Used in **networking** (MAC, IPv6)  
✔ Required for **low‑level programming**  
✔ Important for **interviews & exams**

***

## 9️⃣ Homework / Practice

### Decimal → Binary

Convert manually:

*   **21**
*   **31**
*   **52**
*   **65**

***

### Binary → Decimal

Convert manually:

    0b110011010

***

## 🔑 Quick Summary

*   Computers work in **binary**
*   Python makes conversion **easy**
*   Prefixes (`0b`, `0o`, `0x`) are **mandatory**
*   Manual conversion is needed for **bitwise logic**

***

If you want, I can also:
✅ create **one‑page printable PDF notes**  
✅ give **bitwise operator preview**  
✅ add **interview questions + answers**

Just tell me 🚀
