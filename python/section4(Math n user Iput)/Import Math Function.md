Below is a **neat, clean, and beginner‑friendly cheat sheet** based on your Python math‑functions session.  
I’ve corrected minor terminology slips (like *float vs floor*) and organized everything for quick revision.

***

# ✅ Python Math Module – Cheat Sheet

## 1. Why Use the `math` Module?

*   Python can perform math manually (`*`, `**`, etc.)
*   But the **`math` module** provides:
    *   Cleaner syntax
    *   Better readability
    *   Powerful, ready‑made mathematical functions
    *   Built‑in constants like π and e

***

## 2. Importing the Math Module

### Import the Entire Math Module

```python
import math
```

Usage:

```python
math.sqrt(25)
math.pow(3, 2)
```

***

### Import with Alias (Short Name)

```python
import math as m
```

Usage:

```python
m.sqrt(25)
m.pi
```

✅ Helpful when module names are long or used frequently.

***

### Import Specific Functions Only

```python
from math import sqrt, pow
```

Usage:

```python
sqrt(25)
pow(3, 2)
```

✅ Advantage:

*   No need to write `math.` every time
*   Cleaner and faster code

***

## 3. Square Root

### Find Square Root

```python
import math
x = math.sqrt(25)
print(x)
```

Output:

    5.0

✅ Always returns a **float**

***

## 4. Power Function

### Using `pow()` from math module

```python
math.pow(3, 2)
```

Output:

    9.0

### Using Double Star (`**`)

```python
3 ** 2
```

Output:

    9

✅ **Best Practice** for large projects:  
Use `math.pow()` for clarity and readability.

***

## 5. Floor and Ceil Functions

⚠️ **Correction:**  
The function name is **`floor()`**, not `float()`.

***

### `floor()` – Always Rounds Down

```python
math.floor(2.9)
```

Output:

    2

✅ Takes the **lowest integer**

***

### `ceil()` – Always Rounds Up

```python
math.ceil(2.1)
```

Output:

    3

✅ Takes the **highest integer**

***

### Comparison with `round()`

| Function | Example    | Result |
| -------- | ---------- | ------ |
| round    | round(2.5) | 3      |
| floor    | floor(2.9) | 2      |
| ceil     | ceil(2.1)  | 3      |

***

## 6. Factorial

```python
math.factorial(5)
```

Output:

    120

✅ Works only with **non‑negative integers**

***

## 7. Trigonometric Functions

> All angles must be in **radians**

```python
math.sin(x)
math.cos(x)
math.tan(x)
```

Example:

```python
math.sin(math.pi / 2)
```

Output:

    1.0

***

## 8. Important Math Constants

### Pi (π)

```python
math.pi
```

Output:

    3.141592653589793

***

### Euler’s Number (e)

```python
math.e
```

Output:

    2.718281828459045

***

## 9. When NOT to Import Everything

❌ Avoid:

```python
from math import *
```

✅ Recommended:

```python
from math import sqrt, pow
```

Reason:

*   Prevents name conflicts
*   Improves performance
*   Easier debugging

***

## 10. Best Practices

✅ Use math functions for:

*   Readability
*   Team collaboration
*   Large‑scale projects

✅ Always:

*   Read documentation
*   Experiment in IDE
*   Practice with examples

***

## 11. Quick Summary

*   `sqrt()` → Square root
*   `pow(a, b)` → Power
*   `floor()` → Lowest integer
*   `ceil()` → Highest integer
*   `factorial()` → Factorial
*   `pi`, `e` → Constants
*   Use aliases (`math as m`) for convenience

***

### 🚀 Practice Tip

After watching tutorials:

*   Explore the official Python documentation
*   Try different math functions
*   Write small programs

That’s how you become a **good programmer** 👨‍💻👩‍💻

If you want:

*   ✅ Printable PDF cheat sheet
*   ✅ Practice questions
*   ✅ Mini python math project

Just tell me 😊
