Below are **clean, well‑structured, beginner‑friendly notes** covering **Recursion in Python** and **Factorial using Recursion**, exactly aligned with the lectures you shared.  
These notes are suitable for **learning, revision, and interviews**.

***

# Recursion in Python

***

## 1. What is Recursion?

👉 **Recursion** means a **function calling itself**.

In simple words:

> A function solves a problem by breaking it into **smaller versions of the same problem**.

***

## 2. Basic Example of Recursion

### Simple Function (Without Recursion)

```python
def greet():
    print("Hello")

greet()
```

Output:

    Hello

***

### Recursive Function Example

```python
def greet():
    print("Hello")
    greet()

greet()
```

### What Happens Here?

1.  `greet()` is called
2.  It prints `"Hello"`
3.  It calls `greet()` again
4.  This repeats continuously

✅ This is recursion  
❌ This is **infinite recursion**

***

## 3. Why Infinite Recursion Is Dangerous?

*   It consumes **stack memory**
*   Program may **crash / hang**
*   Python prevents this by setting a **recursion limit**

***

## 4. Python Recursion Limit

### Default Limit

```python
import sys
print(sys.getrecursionlimit())
```

Output:

    1000

✅ Python allows **maximum 1000 recursive calls** by default.

***

### Increasing Recursion Limit (NOT recommended often)

```python
import sys
sys.setrecursionlimit(2000)
```

⚠️ Use carefully – high limits may crash the system.

***

## 5. Counting Recursive Calls (Using Global Variable)

```python
import sys
sys.setrecursionlimit(2000)

i = 0

def greet():
    global i
    i += 1
    print("Hello", i)
    greet()

greet()
```

✅ Prints `Hello` until recursion limit is reached.

***

## 6. Important Rule: Base Case ✅

👉 **Every recursive function MUST have a base condition**, otherwise it becomes infinite.

**Base case = condition where recursion stops**

***

## 7. Structure of a Recursive Function

```python
def function():
    if base_condition:
        return
    function()   # recursive call
```

✅ Without base case → ❌ error  
✅ With base case → ✅ safe recursion

***

# Factorial Using Recursion

***

## 8. Recap: Factorial

    n! = n × (n-1) × (n-2) × ... × 1

### Examples:

*   `5! = 120`
*   `4! = 24`
*   `1! = 1`
*   `0! = 1`

***

## 9. Mathematical Thinking for Recursive Factorial

Factorial can be defined as:

    fact(n) = n × fact(n - 1)

### Base Case:

    fact(1) = 1
    fact(0) = 1

***

## 10. Factorial Using Recursion – Code

```python
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
```

***

## 11. Calling the Function

```python
result = fact(5)
print(result)
```

### Output

    120

***

## 12. Step‑by‑Step Execution (fact(4))

    fact(4)
    = 4 × fact(3)
    = 4 × (3 × fact(2))
    = 4 × (3 × (2 × fact(1)))
    = 4 × 3 × 2 × 1
    = 24

✅ Function keeps calling itself  
✅ Stops at base case  
✅ Then returns values step‑by‑step

***

## 13. Handling Invalid Inputs

```python
def fact(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
```

***

## 14. Iteration vs Recursion (Comparison)

| Iteration       | Recursion             |
| --------------- | --------------------- |
| Uses loops      | Function calls itself |
| Faster          | Slightly slower       |
| Less memory     | More memory           |
| Easier to debug | Cleaner logic         |

✅ Interviews often ask both

***

## 15. Real‑World Use Cases of Recursion 🌍

✅ Tree traversal  
✅ File system navigation  
✅ Divide & conquer algorithms  
✅ Factorial & Fibonacci  
✅ Backtracking problems

***

## 16. Common Mistakes ❌

❌ Missing base condition  
❌ Modifying recursion limit blindly  
❌ Using global variables unnecessarily  
❌ Infinite recursion

***

## 17. Interview Questions & Answers ✅

### Q1. What is recursion?

**Answer:**  
Recursion is a technique where a function calls itself to solve a problem.

***

### Q2. Why is base condition important?

**Answer:**  
It stops infinite recursion and prevents stack overflow.

***

### Q3. What is recursion limit in Python?

**Answer:**  
1000 (default)

***

### Q4. Factorial of 0?

✅ `1`

***

### Q5. Is recursion always better than looping?

❌ No. Use recursion when logic is naturally recursive.

***

## 18. One‑Line Summary ✅

> **Recursion is a powerful technique where a function calls itself, and factorial is a classic example solved elegantly using recursion.**

***

If you want, I can also:

*   Create **diagrams for recursion call stack**
*   Provide **Fibonacci using recursion**
*   Add **debugging visuals**
*   Turn this into **PDF/cheat sheet**
*   Share **interview coding problems**

Just tell me 👍
