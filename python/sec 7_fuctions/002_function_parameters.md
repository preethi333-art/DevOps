Below are **neat, clean, well‑structured notes** based on your lecture, followed by **important interview questions with clear answers**.  
These are written for **revision, teaching, and interview preparation**.

***

# Python Functions – Parameter Passing & Mutability

*(Pass by Value vs Pass by Reference – Python Perspective)*

***

## 1. Recap: Why Functions?

*   Functions help break **large projects into smaller tasks**
*   Each task = one function
*   Functions enable:
    *   Code reuse
    *   Modularity
    *   Easier debugging
    *   Clean structure

***

## 2. Passing Parameters to Functions

When calling a function, we **pass data** using parameters (arguments).

### Example

```python
def update(x):
    x = 8
    print(x)

update(10)
```

### Output

    8

✅ Inside the function, `x` is updated to `8`.

***

## 3. What Happens to Original Variables?

### Example

```python
def update(x):
    x = 8
    print(x)

a = 10
update(a)
print(a)
```

### Output

    8
    10

✅ `x` changed  
✅ `a` remains unchanged

🔍 **Why?**

Even though `a` was passed, its value did not change outside the function.

***

## 4. Pass by Value vs Pass by Reference (Conceptual)

### Pass by Value (C, C++)

*   Value is copied
*   Original variable not affected

### Pass by Reference

*   Address is passed
*   Changes affect original variable

***

## 5. What Does Python Use?

👉 **Python uses neither pure pass‑by‑value nor pass‑by‑reference**

✅ Python uses **object reference passing**

***

## 6. Python Internals: Everything is an Object

*   Variables don’t store values
*   Variables **reference objects**
*   Function parameters reference the **same object initially**

### Example Using `id()`

```python
def update(x):
    print(id(x))
    x = 8
    print(id(x))

a = 10
print(id(a))
update(a)
```

### Observation

*   Before modification → same `id`
*   After modification → new `id`

✅ Initially, `a` and `x` point to the **same object**  
✅ After modification, `x` points to **new object**

***

## 7. Why Does This Happen?

### Because:

*   **Integers, Strings, Tuples are IMMUTABLE**
*   Changing value creates a **new object**

***

## 8. Mutable vs Immutable Objects

### Immutable Types

*   `int`
*   `float`
*   `str`
*   `tuple`

🔹 Modification creates a **new object**

***

### Mutable Types

*   `list`
*   `dict`
*   `set`

🔹 Modification happens **in the same object**

***

## 9. Mutable Example with List

```python
def update_list(lst):
    lst[1] = 25
    print(lst)

a = [10, 20, 30]
print(id(a))
update_list(a)
print(a)
```

### Output

    [10, 25, 30]
    [10, 25, 30]

✅ List changes inside function  
✅ Original list also changes  
✅ Same memory (`id`) is used

***

## 10. Key Concept Summary

| Scenario                  | Result                   |
| ------------------------- | ------------------------ |
| Immutable object modified | New object created       |
| Mutable object modified   | Same object updated      |
| Function parameter        | Reference to object      |
| Python calling style      | Call by object reference |

***

## 11. Important Interview‑Ready Statement ✅

> **Python uses “Call by Object Reference”.  
> Mutable objects can be changed inside functions, immutable objects cannot.**

***

# ⭐ Interview Questions & Answers ⭐

***

### Q1. Is Python pass by value or pass by reference?

✅ **Neither. Python uses call by object reference.**

***

### Q2. Why doesn’t integer change outside a function?

✅ Because integers are **immutable**.

***

### Q3. Why does list change outside a function?

✅ Because lists are **mutable**.

***

### Q4. What happens when you modify an immutable object?

✅ A **new object** is created.

***

### Q5. What will `id()` tell you?

✅ Memory location of the object.

***

### Q6. What are mutable data types in Python?

✅ List, Dictionary, Set

***

### Q7. What are immutable data types?

✅ Int, Float, String, Tuple

***

### Q8. Why is Python called pass by object reference?

✅ Variables reference objects; references are copied, not values.

***

### Q9. Can a function modify global variables?

✅ Yes, but explicitly using `global` keyword (not recommended).

***

### Q10. Why is understanding mutability important?

✅ Prevent bugs, understand side effects, write efficient code.

***

## 12. Best Practices (Industry Level)

✅ Avoid modifying mutable objects inside functions unless intended  
✅ Use return instead of direct modification  
✅ Document function behavior  
✅ Write predictable, side‑effect‑free functions when possible

***

## 13. One‑Line Takeaway for Interviews

> **In Python, function arguments are passed as references to objects.  
> Mutability decides whether changes reflect outside the function.**

***

If you want next:

*   ✅ \*\*Types of arguments (positional, keyword, default, \*args, **kwargs)**
*   ✅ **More tricky interview questions**
*   ✅ **Real‑world bug examples**
*   ✅ **MCQs for interviews**

Just tell me 🚀🐍
