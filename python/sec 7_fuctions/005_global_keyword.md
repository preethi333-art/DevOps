Below are **clean, neat, exam‑ready Python notes** based exactly on your explanation, with **clear examples, real‑world use cases, and interview Q\&A**.  
I’ve simplified the flow so it’s **easy to revise and teach**.

***

# Python Scope – Global & Local Variables

***

## 1. What is Scope in Python?

👉 **Scope** defines **where a variable can be accessed** in a program.

In Python, the most common scopes are:

*   **Global scope**
*   **Local scope**

***

## 2. Global Variable

### Definition

A variable declared **outside** any function is called a **global variable**.

✅ It can be accessed **anywhere** in the file.

### Example

```python
a = 10   # Global variable

def show():
    print(a)

show()
print(a)
```

### Output

    10
    10

✅ Global variables are accessible **inside and outside functions**

***

## 3. Local Variable

### Definition

A variable declared **inside a function** is called a **local variable**.

✅ It can be accessed **only inside that function**

### Example

```python
def show():
    b = 8   # Local variable
    print(b)

show()
print(b)   # Error
```

### Error

    NameError: name 'b' is not defined

❌ Local variables **cannot be accessed outside the function**

***

## 4. Same Variable Name: Global vs Local

Python allows the **same variable name** in different scopes.

```python
a = 10   # Global

def show():
    a = 15   # Local
    print("In function:", a)

show()
print("Outside:", a)
```

### Output

    In function: 15
    Outside: 10

### Important Rule ✅

> **Local variable gets priority inside the function**

***

## 5. Accessing Global Variable Inside a Function

✅ You can **read** a global variable inside a function **without any keyword**

```python
a = 10

def show():
    print(a)

show()
```

Output:

    10

***

## 6. The Problem: Modifying a Global Variable

```python
a = 10

def show():
    a = 15
    print(a)

show()
print(a)
```

### Output

    15
    10

❓ Why didn’t the global variable change?

### Reason

👉 Python treats `a = 15` as **creating a new local variable**, not modifying the global one.

***

## 7. Using `global` Keyword ✅

### Purpose

Tell Python:

> “This variable refers to the **global one**, not local”

### Example

```python
a = 10

def show():
    global a
    a = 15
    print("In function:", a)

show()
print("Outside:", a)
```

### Output

    In function: 15
    Outside: 15

✅ Global variable is modified successfully

***

## 8. Limitation of `global`

Once you use:

```python
global a
```

❌ You **cannot create a local variable** with the same name inside that function.

```python
def show():
    global a
    a = 15
    a = 9   # Still global
```

👉 Both assignments affect the **same global variable**

***

## 9. Need Both Local & Global Together? → Use `globals()` ✅

### What is `globals()`?

*   A built-in function
*   Returns a **dictionary of all global variables**

***

### Example: Local & Global in Same Function

```python
a = 10

def show():
    a = 9        # Local variable
    globals()['a'] = 15   # Modify global variable

    print("Local a:", a)

show()
print("Global a:", a)
```

### Output

    Local a: 9
    Global a: 15

✅ Local and global both coexist  
✅ Clean and controlled

***

## 10. Understanding with `id()` (Memory Address)

```python
a = 10

def show():
    x = globals()['a']
    print(id(a))
    print(id(x))

show()
```

✅ Same `id` → Same memory location  
✅ Confirms we accessed the global variable

***

## 11. Real-World Use Cases 🌍

### ✅ Use Case 1: Application Configuration

```python
DEBUG = True

def disable_debug():
    global DEBUG
    DEBUG = False
```

Used in:

*   Web applications
*   Feature flags

***

### ✅ Use Case 2: Counter / State Management

```python
count = 0

def increment():
    global count
    count += 1
```

Used in:

*   Tracking users
*   Logging hits

***

### ✅ Use Case 3: Global Constants (Read-only)

```python
PI = 3.14

def area(r):
    return PI * r * r
```

✅ Safe usage of global variable

***

## 12. Best Practices ✅

✅ Avoid excessive global variables  
✅ Prefer returning values from functions  
✅ Use `global` only when necessary  
✅ Use `globals()` cautiously  
✅ Global variables are harder to debug

***

## 13. Interview Questions & Answers ✅

### Q1. What is scope in Python?

**Answer:**  
Scope defines the region where a variable can be accessed.

***

### Q2. Difference between global and local variables?

| Global                    | Local                           |
| ------------------------- | ------------------------------- |
| Defined outside function  | Defined inside function         |
| Accessible everywhere     | Accessible only inside function |
| Lifetime = entire program | Lifetime = function execution   |

***

### Q3. Can we access global variables inside a function?

✅ Yes, directly for reading.

***

### Q4. Why does assigning to a global variable inside a function create a local variable?

**Answer:**  
Python assumes assignment means local unless explicitly told using `global`.

***

### Q5. What does the `global` keyword do?

**Answer:**  
It tells Python that the variable refers to the global scope.

***

### Q6. Can we have global and local variable with same name in one function?

❌ Not using `global`  
✅ Yes using `globals()`

***

### Q7. What does `globals()` return?

**Answer:**  
A dictionary containing all global variables and their values.

***

## 14. One-Line Summary ✅

> **Local variables live inside functions, global variables live across the program, and `global`/`globals()` control how they interact.**

***

If you want, I can also:

*   Convert this into **PDF notes**
*   Create **diagram-based explanation**
*   Provide **hands-on practice problems**
*   Add **tricky interview questions**

Just tell me 👍
