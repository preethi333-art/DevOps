Here are **clean, structured notes** on **Method Overloading & Method Overriding in Python (Polymorphism)** with examples, use-cases, and interview Q\&A.

***

# ✅ **Polymorphism in Python**

Polymorphism means **one name, multiple behaviors**.

Types:

1.  **Operator Overloading** ✅ (already covered)
2.  **Method Overloading** ⚠️ (not directly supported in Python)
3.  **Method Overriding** ✅ (fully supported)

***

# 🔹 **1. Method Overloading**

## ✅ Definition

Method overloading means:

*   Same method name
*   Different number/type of arguments

👉 Supported in languages like:

*   Java
*   C#
*   C++

👉 **NOT directly supported in Python**

***

## 🔸 Problem in Python

You **cannot define multiple methods with the same name**:

```python
class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):   # ❌ This overrides the previous method
        return a + b + c
```

👉 Only the **last definition survives**

***

## ✅ How Python Achieves It (Workarounds)

### ✔️ Approach 1: Default Arguments

```python
class Test:
    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        elif a != None:
            return a
        else:
            return 0

t = Test()
print(t.add(5))        # 5
print(t.add(5, 9))     # 14
print(t.add(5, 9, 6))  # 20
```

***

### ✔️ Approach 2: Variable Length Arguments ⭐ (Best Practice)

```python
class Test:
    def add(self, *args):
        return sum(args)

t = Test()
print(t.add(5))           # 5
print(t.add(5, 9))        # 14
print(t.add(5, 9, 6))     # 20
```

***

## ✅ Use Cases

*   Flexible API design
*   Mathematical operations
*   Utility/helper functions
*   Library functions (e.g. `print()`, `sum()`)

***

## ✅ Key Points

*   Python does **not support true method overloading**
*   Achieved via:
    *   Default parameters
    *   `*args`, `**kwargs`
*   Only **one method name exists internally**

***

# 🔹 **2. Method Overriding**

## ✅ Definition

Method overriding means:

*   Same method name
*   Same parameters
*   Different implementation
*   Across **parent and child classes**

***

## ✅ Basic Example

```python
class A:
    def show(self):
        print("In A show")

class B(A):   # Inherits A
    def show(self):   # Overrides A.show()
        print("In B show")

b = B()
b.show()
```

✅ Output:

    In B show

***

## ✅ How It Works

1.  Python looks in **child class first**
2.  If found → executes it
3.  Else → checks **parent class**

***

## ✅ Real-Life Analogy (from your video)

*   Parent (A) has Nokia phone
*   Child (B) initially uses parent's phone
*   Later child gets their own phone → overrides

👉 Same in code:

*   If child has method → use it
*   Else → use parent's method

***

## ✅ Calling Parent Method (Important)

```python
class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        super().show()   # Call parent version
        print("In B show")

b = B()
b.show()
```

✅ Output:

    In A show
    In B show

***

## ✅ Use Cases

*   Customizing inherited behavior
*   Extending functionality
*   Framework development
*   GUI apps, APIs, libraries

***

## ✅ Key Points

*   Requires **inheritance**
*   Uses same method signature
*   Child implementation **overrides parent**
*   `super()` can access parent behavior

***

# ⚡ **Difference: Overloading vs Overriding**

| Feature        | Overloading                 | Overriding             |
| -------------- | --------------------------- | ---------------------- |
| Definition     | Same method, different args | Same method, same args |
| Python Support | ❌ (workarounds)             | ✅                      |
| Location       | Same class                  | Parent & child classes |
| Purpose        | Flexibility                 | Specialization         |
| Inheritance    | Not required                | Required               |

***

# 🎯 **Interview Questions & Answers**

## 🔹 Q1: Does Python support method overloading?

**Answer:**
No, Python does not support traditional method overloading.  
It is achieved using:

*   Default arguments
*   Variable arguments (`*args`)

***

## 🔹 Q2: What is method overriding?

**Answer:**
It is redefining a method in a child class with the same name and parameters as in the parent class.

***

## 🔹 Q3: What is the difference between overloading and overriding?

**Answer:**

*   Overloading → same name, different parameters
*   Overriding → same name, same parameters in inheritance

***

## 🔹 Q4: How does Python decide which method to call?

**Answer:**
Uses **Method Resolution Order (MRO)**:

*   Searches child class first
*   Then parent class

***

## 🔹 Q5: What is `super()`?

**Answer:**
Used to call the parent class method inside child class.

***

## 🔹 Q6: Can we override constructors (`__init__`)?

👉 Yes

```python
class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")
```

***

## 🔹 Q7: What happens if child does not override method?

👉 Parent method is used automatically.

***

## 🔹 Q8: Can method overriding change return type?

👉 Yes (Python is dynamic)

***

## 🔹 Q9: What is MRO?

👉 Order in which Python searches classes:

```python
print(B.__mro__)
```

***

## 🔹 Q10: Why is overriding important?

👉 Helps:

*   Customize parent behavior
*   Implement polymorphism
*   Write reusable code

***

# ✅ **Summary**

*   **Overloading** = Same name, different inputs (NOT native in Python)
*   **Overriding** = Same name, redefined in child class
*   Python supports polymorphism mainly via:
    *   Dynamic typing
    *   Overriding
    *   Operator overloading

***

If you want, I can also provide:
✅ Cheat sheet  
✅ MCQs for practice  
✅ Real-world coding problems  
✅ Diagrams for better understanding
