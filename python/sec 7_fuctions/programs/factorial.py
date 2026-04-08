Below are **clean, neat, beginner‑friendly notes** for the topic **Factorial in Python using Functions**, based exactly on the lecture content you shared.  
These notes are structured for **learning, revision, and interview preparation**.

***

# Factorial of a Number in Python

***

## 1. What is a Factorial?

The **factorial** of a number `n` is the product of all positive integers from `1` to `n`.

### Mathematical Definition

    n! = n × (n−1) × (n−2) × ... × 1

### Examples

| Number | Factorial               |
| ------ | ----------------------- |
| 5      | 5 × 4 × 3 × 2 × 1 = 120 |
| 4      | 4 × 3 × 2 × 1 = 24      |
| 3      | 3 × 2 × 1 = 6           |
| 1      | 1                       |
| 0      | 1                       |

***

## 2. Why Use a Function?

✅ Reusability  
✅ Cleaner code  
✅ Easier testing  
✅ Accepts any large number  
✅ Industry best practice

***

## 3. Problem Statement

*   Take a number
*   Calculate its factorial
*   Print the result
*   Use a **function**
*   Use a **loop** (iterative approach)

***

## 4. Approach (Logic)

1.  Start with value `1` (factorial base)
2.  Loop from `1` to `n`
3.  Multiply each number with the previous result
4.  Return the final value

***

## 5. Factorial Function (Iterative)

### Code Implementation

```python
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
```

***

## 6. Calling the Function

```python
x = 5
result = fact(x)
print(result)
```

### Output

    120

***

## 7. Step‑by‑Step Execution (Example: n = 4)

| i       | f (result) |
| ------- | ---------- |
| Initial | 1          |
| 1       | 1 × 1 = 1  |
| 2       | 1 × 2 = 2  |
| 3       | 2 × 3 = 6  |
| 4       | 6 × 4 = 24 |

✅ Final result = **24**

***

## 8. Why `range(1, n+1)`?

```python
range(1, n+1)
```

*   `range(n)` → ends at `n‑1`
*   Factorial requires loop **up to n**
*   Hence `n + 1`

***

## 9. Dry Run Explanation

*   `f` starts at 1
*   Each loop iteration multiplies `f` with `i`
*   Value accumulates
*   Final value returned

***

## 10. Handling Different Inputs

### Example: Factorial of 4

```python
print(fact(4))
```

✅ Output:

    24

***

## 11. Common Beginner Mistakes ❌

❌ Starting `f = 0`  
❌ Using `range(n)` instead of `range(1, n+1)`  
❌ Forgetting `return`  
❌ Printing inside function instead of returning  
❌ Not handling negative values

***

## 12. Improved Version (Input Validation)

```python
def fact(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1

    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
```

***

## 13. Real‑World Use Cases 🌍

✅ Mathematical calculations  
✅ Probability & permutations  
✅ Competitive programming  
✅ Interview coding questions  
✅ Backend calculations

***

## 14. Interview Questions & Answers ✅

### Q1. What is factorial?

**Answer:**  
Product of all positive integers from 1 to n.

***

### Q2. Factorial of 0?

✅ `0! = 1`

***

### Q3. How do you implement factorial in Python?

Using:

*   Loop (iteration)
*   Recursion (advanced)

***

### Q4. Why initialize factorial value as 1?

Because multiplication identity = 1.

***

### Q5. Time complexity of factorial program?

**Answer:**  
O(n)

***

### Q6. Can factorial be calculated without a loop?

✅ Yes, using recursion.

***

## 15. Assignment (Practice)

✅ Take input from user  
✅ Check if input is negative  
✅ Compute factorial using function  
✅ Print result

***

## 16. One‑Line Summary ✅

> **Factorial is calculated by multiplying numbers from 1 to n, and Python uses loops and functions efficiently to compute it.**

***

If you’d like, I can also:

*   Explain **recursive factorial**
*   Compare **iteration vs recursion**
*   Create **MCQs**
*   Provide **debugging walkthrough**
*   Convert these notes into **PDF**

Just tell me 👍
