Below are **clean, simple, beginner‑friendly notes** on **Anonymous Functions / Lambda Functions in Python**, along with **use cases** and **interview‑level Q\&A**, exactly matching the lecture style you provided.

***

# Anonymous (Lambda) Functions in Python

***

## 1. What Are Anonymous Functions?

In Python, a **normal function** is created using:

```python
def function_name(parameters):
    return expression
```

But sometimes:

*   You need a function **only once**
*   It contains **only one expression**
*   Giving it a full name is unnecessary

👉 This is where **anonymous functions** come in.

Anonymous functions = **functions without a name**  
In Python, they are created using the **lambda keyword**.

***

## 2. Lambda Function Syntax

    lambda arguments : expression

*   Can have **any number of arguments**
*   Can have **only ONE expression**
*   Expression is **implicitly returned**
*   Usually stored in a variable for reuse

***

## 3. Normal Function vs Lambda Function

### Normal Function

```python
def square(a):
    return a * a

print(square(5))    # 25
```

### Equivalent Lambda Function

```python
f = lambda a: a * a
print(f(5))         # 25
```

👉 Both do the same thing  
👉 Lambda is shorter & cleaner for one‑line logic

***

## 4. Lambda Function with Multiple Arguments

### Normal Function

```python
def add(a, b):
    return a + b
```

### Lambda Version

```python
f = lambda a, b: a + b
print(f(5, 6))   # 11
```

***

## 5. Important Rules of Lambda

*   Must contain **only one expression**
*   Cannot contain:
    *   loops
    *   if‑else (unless in single-line form)
    *   multiple statements
    *   print statements inside
*   Generally used for **simple transformations**

***

## 6. Why Use Lambdas?

Lambdas shine when:

*   You need a function **temporarily**
*   You don't want to waste lines defining a full function
*   You want cleaner, shorter code
*   You use higher‑order functions like:
    *   `map()`
    *   `filter()`
    *   `reduce()`
    *   sorting with `key=`  
        (all these support lambda expressions)

***

## 7. Real‑World Use Cases

### Use Case 1: Sorting Complex Data

```python
students = [("Alice", 25), ("Bob", 20), ("Carl", 23)]
students.sort(key=lambda x: x[1])
print(students)
```

Sorts by age.

***

### Use Case 2: Using map() for transformations

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)
```

***

### Use Case 3: Using filter() to select values

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

***

### Use Case 4: Inline logic (used once)

```python
print((lambda a, b: a * b)(4, 5))   # 20
```

***

## 8. Lambda Functions Are Often Returned by Other Functions

Example:

```python
def make_multiplier(n):
    return lambda a: a * n

double = make_multiplier(2)
print(double(10))     # 20
```

***

# Interview Q\&A (Important)

***

### Q1. What is a lambda function?

**Answer:**  
A lambda function is an **anonymous, one‑line function** created using the `lambda` keyword.

***

### Q2. Why do we use lambda functions?

**Answer:**  
To write short, simple functions in one line, especially when passing them as arguments to other functions like `map`, `filter`, `sorted`.

***

### Q3. Can lambda have multiple statements?

**Answer:**  
❌ No  
Lambda supports **only one expression**, executed and returned automatically.

***

### Q4. Are lambda functions faster?

**Answer:**  
No. They are not faster.  
They are used for **code readability and convenience**.

***

### Q5. Can lambda functions have default arguments?

**Answer:**  
Yes.

```python
f = lambda a, b=10: a + b
print(f(5))   # 15
```

***

### Q6. Can we assign a lambda to a variable?

**Answer:**  
Yes, that's how we generally use them.

```python
f = lambda x: x * 2
```

***

### Q7. What is the difference between normal function and lambda?

| Normal Function           | Lambda Function                   |
| ------------------------- | --------------------------------- |
| Has a name                | Anonymous                         |
| Can have many lines       | Only one expression               |
| Can have loops/conditions | Only single expression            |
| Used widely               | Used mainly for inline operations |

***

### Q8. Are lambda functions objects in Python?

**Answer:**  
Yes, functions (including lambda) are first‑class objects.  
They can be:

*   stored in variables
*   passed to functions
*   returned from functions

***

# One‑Line Summary

> **Lambda functions are short, unnamed, one‑line functions perfect for simple operations and functional programming in Python.**

***

If you want, I can also create:

*   Next chapter: **Lambdas with map, filter, reduce**
*   Practice exercises
*   MCQs
*   Cheat sheet PDF
*   A combined notebook for all chapter notes

Just tell me!
