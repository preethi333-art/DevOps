Here are **clean, structured notes on Iterators in Python** with **examples, use-cases, and interview Q\&A**.

***

# ✅ **Iterators in Python**

## 🔹 What is an Iterator?

An **iterator** is an object that:

*   Allows you to traverse (iterate) over elements
*   Returns **one value at a time**
*   Maintains its **state (position)**

👉 Used internally in:

*   `for` loops
*   list, tuple, string traversal

***

## 🔹 Basic Example

```python
nums = [7, 8, 9, 5]

it = iter(nums)   # convert list to iterator

print(next(it))   # 7
print(next(it))   # 8
print(next(it))   # 9
```

***

## ✅ Key Concepts

### ✔️ 1. `iter()`

*   Converts an iterable → iterator

```python
it = iter(nums)
```

***

### ✔️ 2. `next()`

*   Fetches next element
*   Maintains state internally

```python
next(it)
```

***

## ✅ Important Behavior

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
```

👉 Iterator **remembers position**, doesn’t restart

***

## ✅ Error Handling

```python
print(next(it))  # 3
print(next(it))  # ❌ StopIteration error
```

👉 When no elements left → **StopIteration**

***

# 🔹 **How `for` Loop Works Internally**

```python
for i in nums:
    print(i)
```

👉 Internally does:

```python
it = iter(nums)

while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break
```

***

# 🔹 **Custom Iterator (User-defined)**

## ✅ Rules to Create Iterator Class

You must implement:

1.  `__iter__()` → returns iterator object
2.  `__next__()` → returns next value

***

## ✅ Example: Top 10 Numbers

```python
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
```

***

## ✅ Using Custom Iterator

```python
values = TopTen()

for i in values:
    print(i)
```

✅ Output:

    1 2 3 4 5 6 7 8 9 10

***

## 🔹 Important Insight

👉 Iterator does **NOT restart automatically**

```python
values = TopTen()

print(next(values))  # 1

for i in values:
    print(i)
```

✅ Output:

    1
    2 3 4 5 6 7 8 9 10

👉 First value is already consumed

***

# 🔹 **Difference: Iterable vs Iterator**

| Feature    | Iterable                    | Iterator                       |
| ---------- | --------------------------- | ------------------------------ |
| Definition | Object that can be iterated | Object that performs iteration |
| Example    | list, tuple, string         | object from `iter()`           |
| Methods    | `__iter__()`                | `__iter__()`, `__next__()`     |

***

# 🔹 **Use Cases**

## ✅ 1. Large Data Processing

*   Avoid loading entire data into memory
*   Example: file reading line-by-line

***

## ✅ 2. Streaming Data

*   Real-time data processing
*   APIs, sensors

***

## ✅ 3. Custom Sequences

*   Generate dynamic values (like Fibonacci)

***

## ✅ 4. Memory Optimization

*   Iterators are **lazy**
*   Generate values only when needed

***

# 🔹 **Iterator vs List**

| Feature     | List              | Iterator             |
| ----------- | ----------------- | -------------------- |
| Storage     | Stores all values | Generates one-by-one |
| Memory      | High              | Low                  |
| Reusability | Yes               | No (single pass)     |

***

# 🎯 **Interview Questions & Answers**

## 🔹 Q1: What is an iterator?

**Answer:**
An object that returns elements one at a time using `__next__()`.

***

## 🔹 Q2: Difference between iterable and iterator?

**Answer:**

*   Iterable → can be looped (`list`)
*   Iterator → performs iteration (`iter(list)`)

***

## 🔹 Q3: What are `__iter__()` and `__next__()`?

**Answer:**

*   `__iter__()` → returns iterator object
*   `__next__()` → returns next value or raises StopIteration

***

## 🔹 Q4: What is StopIteration?

**Answer:**
Exception raised when iterator reaches the end.

***

## 🔹 Q5: Does `for` loop use iterators?

**Answer:**
Yes. Internally, it uses `iter()` and `next()`.

***

## 🔹 Q6: Can iterator be reused?

**Answer:**
❌ No. Once exhausted, it cannot restart.

***

## 🔹 Q7: Why use iterators instead of lists?

**Answer:**

*   Memory efficient
*   Lazy evaluation
*   Suitable for large data

***

## 🔹 Q8: What is lazy evaluation?

**Answer:**
Values are generated only when requested.

***

## 🔹 Q9: Write a custom iterator example

👉 (TopTen example above)

***

## 🔹 Q10: What happens if `__next__()` doesn't raise StopIteration?

**Answer:**
Loop becomes **infinite**

***

# ✅ **Summary**

*   Iterator = object that gives values one-by-one
*   Uses:
    *   `iter()` → get iterator
    *   `next()` → get next value
*   `for` loop works using iterators internally
*   Custom iterator requires:
    *   `__iter__()`
    *   `__next__()`
*   Must raise **StopIteration** to stop loop

***

If you want next:
✅ Generator vs Iterator (very important)  
✅ Practice problems  
✅ MCQs + tricky interview questions  
✅ Visual diagram explanation
