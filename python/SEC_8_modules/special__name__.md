Below are **clean, structured notes**, **clear use cases**, and **commonly asked interview questions** on the Python concept  
👉 **`__name__ == "__main__"`**  
Perfect for **learning, revision, teaching, and interviews**.

***

# 📘 Python `__name__` and `__main__` – Clean Notes

## 🔹 What is `__name__`?

`__name__` is a **special built-in variable** in Python.

*   It is surrounded by **double underscores** (called *dunder* variables)
*   Python automatically assigns a value to it

✅ You **do not create it**—Python creates it for every module.

***

## 🔹 What Value Does `__name__` Hold?

| Situation                 | Value of `__name__` |
| ------------------------- | ------------------- |
| File run directly         | `"__main__"`        |
| File imported as a module | `"module_name"`     |

***

## 🔹 Why is `__name__` Important?

In real projects:

*   You may have **multiple Python files (modules)**
*   One file is the **entry point**
*   Others are **supporting modules**

`__name__` helps Python identify:
✅ **Which file is being executed first**
✅ **Which file is imported**

***

## 🔹 Example 1: Running a File Directly

### demo.py

```python
print(__name__)
```

### Output

```text
__main__
```

✅ Because `demo.py` is executed directly

***

## 🔹 Example 2: Importing a Module

### calc.py

```python
print(__name__)
```

### demo.py

```python
import calc
```

### Output

```text
calc
```

✅ Because `calc.py` is imported, not executed directly

***

## 🔹 The Problem Without `__name__ == "__main__"`

Consider this:

```python
print("Hello")
print("Welcome User")
```

If this file is imported:
✅ These lines **run automatically**
❌ Which is usually **not desired**

***

## 🔹 Solution: The `if __name__ == "__main__"` Pattern

This condition ensures:
✅ Code runs **only when the file is executed directly**
✅ Code does **not run when imported**

***

## 🔹 Standard Python Entry Point Pattern

```python
def main():
    print("Hello")
    print("Welcome User")

if __name__ == "__main__":
    main()
```

***

## 🔹 What Happens Here?

### ✅ If file is run directly:

*   `__name__ == "__main__"` → TRUE
*   `main()` is executed

### ✅ If file is imported:

*   `__name__` ≠ `"__main__"`
*   `main()` is NOT executed

***

## 🔹 Why Python Uses This Pattern

*   Prevents unwanted execution
*   Makes modules reusable
*   Keeps code clean and professional
*   Standard practice in production-level Python

***

# 💡 Use Cases of `__name__ == "__main__"`

## ✅ 1. Entry Point for Applications

Used to define **starting point**:

*   CLI tools
*   Scripts
*   Automation programs

***

## ✅ 2. Library Development

*   Run tests only when file is executed
*   Avoid auto-execution on import

***

## ✅ 3. Debugging & Testing

```python
if __name__ == "__main__":
    test_function()
```

***

## ✅ 4. Real-World Projects

Frameworks like:

*   Django
*   Flask
*   FastAPI

Use this pattern extensively

***

## ✅ 5. Microservices

*   Start servers only when service is executed
*   Safe imports across services

***

# 🧠 Interview Questions on `__name__ == "__main__"`

***

## 🔹 Beginner Level

### Q1. What is `__name__` in Python?

✅ A special variable that indicates whether a file is run directly or imported.

***

### Q2. What is `"__main__"`?

✅ It represents the **entry point of execution**.

***

### Q3. What happens when you print `__name__`?

✅ It prints `"__main__"` or the module name depending on execution.

***

***

## 🔹 Intermediate Level

### Q4. Why do we use `if __name__ == "__main__"`?

✅ To prevent code from running when imported as a module.

***

### Q5. What will `__name__` be when a module is imported?

✅ The name of the module (file name without `.py`)

***

### Q6. Can we have multiple `main()` functions?

✅ Yes, but only the one guarded by `__main__` executes

***

***

## 🔹 Advanced Level

### Q7. Is `main()` a keyword in Python?

✅ No, it is just a **naming convention**

***

### Q8. What happens if we don’t use `__main__` in large projects?

✅ Unwanted execution, bugs, poor maintainability

***

### Q9. How does this help in unit testing?

✅ Prevents production code from running during tests

***

### Q10. Is `__name__ == "__main__"` Python-specific?

✅ Yes, but similar concepts exist in other languages

***

# ✅ Summary (Quick Revision)

*   `__name__` is auto-created by Python
*   Value depends on execution context
*   `"__main__"` is the entry point
*   Prevents unwanted execution
*   Essential in **real-world Python projects**
*   Common **interview question**

***

If you want next:
✅ **MCQ questions**
✅ **Code-based interview problems**
✅ **Project-level folder structure**
✅ **Comparison with Java / C main method**

Just tell me 👽🐍
