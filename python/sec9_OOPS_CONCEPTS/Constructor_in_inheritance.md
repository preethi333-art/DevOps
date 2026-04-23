Below is a **clean, structured, and interview‑ready explanation** of **constructors in inheritance, `super()`, and Method Resolution Order (MRO)** in Python, with **use cases and common interview questions**.  
This is written exactly like a **polished teaching note / video explanation**, but clearer and more professional.

***

# 🔹 Constructors, `super()` & MRO in Python Inheritance

***

## 1️⃣ Constructor Behavior in Inheritance

### ✅ What is a Constructor?

A **constructor** is a special method named:

```python
__init__()
```

*   It executes **automatically** when an object is created
*   Used to initialize values or perform setup

***

## 2️⃣ Constructor Call in Single Inheritance

### Example

```python
class A:
    def __init__(self):
        print("In A __init__")

class B(A):
    pass

obj = B()
```

### ✅ Output

    In A __init__

### 🔍 Why?

*   Python looks for `__init__` in **class B**
*   If not found, it **moves to parent class A**
*   So parent constructor executes

***

## 3️⃣ When Both Parent and Child Have Constructors

```python
class A:
    def __init__(self):
        print("In A __init__")

class B(A):
    def __init__(self):
        print("In B __init__")

obj = B()
```

### ✅ Output

    In B __init__

### 🔑 Key Rule

*   **Child constructor overrides parent constructor**
*   Parent constructor is **not called automatically**

***

## 4️⃣ Calling Parent Constructor Using `super()`

### ✅ Correct Way

```python
class A:
    def __init__(self):
        print("In A __init__")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B __init__")

obj = B()
```

### ✅ Output

    In A __init__
    In B __init__

### 🔍 Execution Flow

1.  Object of `B` created
2.  `B.__init__()` called
3.  `super().__init__()` jumps to `A.__init__`
4.  Control returns back to `B`

***

## ✅ Key Points on `super()`

*   Refers to **immediate parent** according to MRO
*   Used to call:
    *   Parent constructors
    *   Parent methods
*   Works for **methods also**, not just `__init__`

***

## 5️⃣ Calling Parent Methods Using `super()`

```python
class A:
    def feature2(self):
        print("Feature 2 from A")

class B(A):
    def feature3(self):
        super().feature2()
        print("Feature 3 from B")

obj = B()
obj.feature3()
```

### ✅ Output

    Feature 2 from A
    Feature 3 from B

✅ `super()` is **not limited to constructors**

***

## 6️⃣ Multiple Inheritance & Constructor Behavior

```python
class A:
    def __init__(self):
        print("In A __init__")

class B:
    def __init__(self):
        print("In B __init__")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("In C __init__")

obj = C()
```

### ✅ Output

    In A __init__
    In C __init__

### ❓ Why not B?

Because of **Method Resolution Order (MRO)**

***

## 7️⃣ What is Method Resolution Order (MRO)?

📌 **MRO defines the order in which Python searches for methods**

### ✅ Rules:

1.  Current class
2.  Then parent classes
3.  **Left to right**
4.  Depth‑first
5.  Uses **C3 Linearization**

***

### 🔍 View MRO

```python
print(C.mro())
```

### ✅ Output

```text
[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]
```

✅ That’s why `A.__init__()` was called before `B.__init__()`

***

## 8️⃣ Method Name Conflict in Multiple Inheritance

```python
class A:
    def feature1(self):
        print("Feature1 from A")

class B:
    def feature1(self):
        print("Feature1 from B")

class C(A, B):
    pass

obj = C()
obj.feature1()
```

### ✅ Output

    Feature1 from A

### 🔍 Reason

*   Python follows **left‑to‑right MRO**
*   `A` appears before `B`

***

## 9️⃣ Real‑World Use Cases

### ✅ 1. Framework Development

```python
class BaseView:
    def setup(self):
        print("Setup logic")

class LoginView(BaseView):
    def setup(self):
        super().setup()
        print("Login setup")
```

***

### ✅ 2. Banking Systems

```python
class Account:
    def __init__(self):
        print("Account Created")

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        print("Savings Account Created")
```

***

### ✅ 3. Game Engines

```python
class Character:
    def spawn(self):
        print("Spawn Character")

class Warrior(Character):
    def spawn(self):
        super().spawn()
        print("Spawn Warrior")
```

***

## 🎯 Interview Questions & Answers

***

### 🔹 Q1: Does child constructor call parent constructor automatically?

❌ No  
✅ Must use `super().__init__()`

***

### 🔹 Q2: What is `super()`?

✅ A built‑in function used to access parent class methods using MRO

***

### 🔹 Q3: What is MRO?

✅ Order Python follows to resolve method calls in inheritance

***

### 🔹 Q4: Does Python support multiple inheritance?

✅ Yes, using MRO to avoid ambiguity

***

### 🔹 Q5: How to check MRO?

```python
ClassName.mro()
```

***

### 🔹 Q6: Why is `super()` preferred over class name?

✅ Enables:

*   Clean hierarchy traversal
*   Better maintainability
*   Works correctly in multiple inheritance

***

### 🔹 Q7: Can `super()` call normal methods?

✅ Yes, not just constructors

***

## 🧠 Final Summary

✔ Constructors run when objects are created  
✔ Child overrides parent constructor  
✔ `super()` calls parent logic  
✔ MRO defines execution order  
✔ Left‑to‑right resolution in multiple inheritance  
✔ Crucial for real projects and interviews

***

If you want, next topics can be:
✅ Polymorphism  
✅ Method Overriding vs Overloading  
✅ Abstract Classes  
✅ Real‑world project examples

Just say the word 🚀
