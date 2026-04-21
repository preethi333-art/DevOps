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

