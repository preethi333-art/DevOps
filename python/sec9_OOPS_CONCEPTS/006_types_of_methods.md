Below are **clean, neat, exam‑ready notes** based on your content, rewritten clearly with **examples, use cases, and interview questions**.

***

# Python Methods – Clean Notes

## 1. What is a Method?

A **method** is a function defined inside a class that represents the **behavior** of an object.

*   **Variables** → store data (state)
*   **Methods** → perform actions (behavior)

Example:

*   Student has **marks** → variables
*   Student can **calculate average** → method

***

## 2. Types of Methods in Python

Python supports **three types of methods** inside a class:

1.  **Instance Method**
2.  **Class Method**
3.  **Static Method**

> ✅ Unlike variables, **class methods and static methods are NOT the same**

***

## 3. Instance Methods

### Definition

*   Works with **instance variables**
*   Uses the keyword **`self`**
*   Called using an **object**

***

### Example

```python
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
```

### Creating Objects

```python
s1 = Student(34, 67, 32)
s2 = Student(87, 32, 12)

print(s1.average())
print(s2.average())
```

✅ `average()` is an **instance method** because:

*   It uses `self`
*   It accesses instance variables (`m1`, `m2`, `m3`)

***

### Types of Instance Methods

#### a) Accessors (Getters)

*   Used to **fetch data**
*   Do NOT modify values

```python
def get_m1(self):
    return self.m1
```

#### b) Mutators (Setters)

*   Used to **modify data**

```python
def set_m1(self, value):
    self.m1 = value
```

✅ **Getters → Access values**  
✅ **Setters → Modify values**

***

## 4. Class Methods

### Definition

*   Works with **class variables**
*   Uses **`cls`**
*   Uses decorator **`@classmethod`**
*   Can be called using **class name**

***

### Example

```python
class Student:
    school = "ABC School"

    @classmethod
    def get_school_name(cls):
        return cls.school
```

### Calling Class Method

```python
print(Student.get_school_name())
```

✅ Class methods:

*   Affect **all objects**
*   Used when data is **shared**

***

### Where Class Methods Are Used

*   Working with shared data
*   Modifying class variables
*   Factory methods
*   Configuration values

***

## 5. Static Methods

### Definition

*   Does **not use** `self` or `cls`
*   Independent of instance & class variables
*   Uses decorator **`@staticmethod`**

***

### Example

```python
class Student:

    @staticmethod
    def info():
        print("This is Student class")
```

### Calling Static Method

```python
Student.info()
```

✅ Static methods:

*   Perform utility or helper tasks
*   Do not access class or instance data

***

### Use Cases of Static Methods

*   Mathematical operations
*   Validation logic
*   Utility functions
*   Helper methods
*   Factorial, prime check, conversions

***

## 6. Comparison Summary

| Method Type | Keyword Used | Works With         | Called Using |
| ----------- | ------------ | ------------------ | ------------ |
| Instance    | `self`       | Instance variables | Object       |
| Class       | `cls`        | Class variables    | Class        |
| Static      | None         | No variables       | Class        |

***

## 7. When to Use Which Method?

✅ **Use Instance Method when**

*   Working with object data
*   Behavior depends on instance

✅ **Use Class Method when**

*   Working with shared data
*   Need to affect all objects

✅ **Use Static Method when**

*   No dependency on class/object data
*   Utility functionality

***

## 8. Interview Questions & Answers

### Q1. What are instance methods?

**Answer:**  
Methods that access instance variables using `self` and are called using an object.

***

### Q2. Why do class methods use `cls` instead of `self`?

**Answer:**  
Because class methods operate on class variables, not instance variables.

***

### Q3. Difference between class method and static method?

**Answer:**  
Class methods access class variables using `cls`.  
Static methods access neither class nor instance variables.

***

### Q4. Can static methods access instance variables?

**Answer:**  
❌ No. Static methods cannot access instance or class variables.

***

### Q5. Why use setters and getters?

**Answer:**  
To maintain data encapsulation and control access to variables.

***

### Q6. Can we call instance methods using class name?

**Answer:**  
❌ No, because instance methods require an object (`self`).

***

## 9. One‑Line Summary

> **Instance methods work with object data, class methods work with shared data, and static methods work independently as utility functions.**

***

Great 👍  
Let’s go **very slow, very clear**, using **pictures in your mind**, **simple code**, and **daily‑life examples**.

***

# Python Methods – Explained like a STORY

## Imagine This 👇

There is a **school**.  
Inside the school, there are **students**.

Each student:

*   has **their own marks**
*   all students share the **same school name**

Some actions:

*   calculate **my average** → only for *this student*
*   show **school name** → same for everyone
*   show **general information** → not related to marks or school

***

# Step 1️⃣ Create a Student Class

```python
class Student:
    school = "ABC School"   # common for all students

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
```

***

# Step 2️⃣ Instance Method (MOST IMPORTANT)

## 📌 What is it?

*   Works with **one student**
*   Uses **self**
*   Uses **student’s own data**

***

### Example: Average Marks

```python
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
```

### Use it

```python
s1 = Student(10, 20, 30)
print(s1.average())
```

### Think like this 🧠

> 🧑 “Calculate **MY** marks”

✅ Needs **self**  
✅ Depends on **this object**

***

# Step 3️⃣ Class Method

## 📌 What is it?

*   Works with **class data**
*   Same for **all students**
*   Uses **cls**
*   Uses `@classmethod`

***

### Example: School Name

```python
    @classmethod
    def get_school(cls):
        return cls.school
```

### Use it

```python
print(Student.get_school())
```

### Think like this 🧠

> 🏫 “Which school do **we all belong to**?”

✅ No object needed  
✅ Uses **class data**

***

# Step 4️⃣ Static Method (EASIEST)

## 📌 What is it?

*   Uses **nothing**
*   No `self`
*   No `cls`
*   Just helper info
*   Uses `@staticmethod`

***

### Example: Info

```python
    @staticmethod
    def info():
        print("This is the Student class")
```

### Use it

```python
Student.info()
```

### Think like this 🧠

> 📄 “Just extra information”

✅ No data needed  
✅ Just a helper

***

# FINAL COMPLETE CODE (SEE TOGETHER)

```python
class Student:
    school = "ABC School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is the Student class")
```

***

# ONE LOOK DIFFERENCE TABLE 👀

| Method   | Uses        | Keyword | Example Use       |
| -------- | ----------- | ------- | ----------------- |
| Instance | object data | `self`  | calculate average |
| Class    | common data | `cls`   | school name       |
| Static   | no data     | none    | info / helper     |

***

# SUPER EASY REMEMBERING TRICK 🔑

Ask **ONE QUESTION ONLY**:

### ❓ What does this method need?

*   👉 Student’s own data → **Instance method**
*   👉 Same data for everyone → **Class method**
*   👉 No data → **Static method**

***

# Interview Friendly Lines ✅

*   Instance method works on **object data**
*   Class method works on **class data**
*   Static method works as **utility/helper**
*   `self` → object
*   `cls` → class

***

💡 If you want next:

*   ✨ Drawing / diagram explanation
*   ✨ Real‑life analogy only (no code)
*   ✨ Practice questions
*   ✨ 5 interview MCQs

Just tell me 👍


EXAMPLE
-------

Good question. Your code is **almost correct**, but there is **one important mistake** and a couple of **conceptual issues**.  
I’ll explain **clearly**, then show the **correct version**, and finally explain **why**.

***

## ✅ Your Code (As Given)

```python
class Student:
    def school(cls):
        print("This is a school: Aditya")

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @staticmethod
    def sample():
        print("This is a sample method")
    
S1 = Student(34, 56, 78)
S2 = Student(45, 67, 89) 

print(Student.school())
print(S1.avg())
print(Student.sample())
```

***

## ❌ Problem 1: `school()` is NOT a class method

### Your method:

```python
def school(cls):
```

This **LOOKS** like a class method because you used `cls`,  
but Python does **not care about the name** `cls`.

➡️ Python only treats it as a **normal instance method**, because:

*   There is **no `@classmethod` decorator**

So internally Python thinks:

```python
Student.school()  # ❌ missing argument
```

### What actually happens?

```text
TypeError: school() missing 1 required positional argument
```

***

## ✅ Correct Way to Write `school()` as a Class Method

```python
class Student:
    @classmethod
    def school(cls):
        print("This is a school: Aditya")
```

✅ Now Python knows:

*   This method belongs to **class**
*   `cls` will automatically receive `Student`

***

## ❌ Problem 2: Using `print(Student.school())`

Your `school()` method **prints** something but does **not return** anything.

So:

```python
print(Student.school())
```

Output will be:

```text
This is a school: Aditya
None
```

Because:

*   `print()` inside method → prints message
*   No `return` → returns `None`

***

## ✅ Better Practice: Either PRINT or RETURN (not both)

### Option 1: Return value (recommended)

```python
@classmethod
def school(cls):
    return "This is a school: Aditya"
```

Then:

```python
print(Student.school())
```

✅ Clean output  
✅ Reusable method

***

## ✅ Problem 3: `sample()` static method is correct ✅

```python
@staticmethod
def sample():
    print("This is a sample method")
```

This is **perfect** because:

*   No `self`
*   No `cls`
*   No class or instance data

Calling:

```python
Student.sample()
```

✅ Correct  
✅ Best practice

***

## ✅ Fully Corrected & CLEAN Version

```python
class Student:

    @classmethod
    def school(cls):
        return "This is a school: Aditya"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @staticmethod
    def sample():
        return "This is a sample method"


S1 = Student(34, 56, 78)
S2 = Student(45, 67, 89)

print(Student.school())
print(S1.avg())
print(Student.sample())
```

***

## 🧠 Summary (VERY IMPORTANT)

### Key Rules to Remember

| Method Type | Must Have | Decorator         | Called Using |
| ----------- | --------- | ----------------- | ------------ |
| Instance    | `self`    | ❌                 | Object       |
| Class       | `cls`     | ✅ `@classmethod`  | Class        |
| Static      | none      | ✅ `@staticmethod` | Class        |

***

## 🔑 Interview‑Perfect Explanation

> **“Using `cls` alone does not make a class method; the `@classmethod` decorator is mandatory.”**

***

If you want next, I can:
✅ Show memory flow (how Python passes `self/cls`)  
✅ Explain why decorators are required  
✅ Give interview trick questions  
✅ Explain error messages line by line

Just tell me 👍

