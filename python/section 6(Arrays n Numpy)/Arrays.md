Below are **clear, neat, and exam‑ready notes** based on your video content, rewritten cleanly and structured for easy learning and revision.

***

# Python Arrays – Clear Notes

## 1. What is an Array in Python?

*   An **array** is a collection of elements **of the same data type**.
*   Arrays are **similar to lists**, but:
    *   Lists can store **different data types**
    *   Arrays can store **only one data type**
*   Arrays are **dynamic**:
    *   They can **grow (expand)** and **shrink**

✅ Use arrays when:

*   You need better **type consistency**
*   You store **large numeric data**

***

## 2. Why Use Arrays? (Real‑World Example)

*   Suppose a class has **100 students**
*   Each student has **Python marks**
*   Creating 100 separate variables is inefficient
*   ✅ Use an array to store all marks together

***

## 3. Importing the Array Module

Arrays are **not built‑in**, so we must import the module.

### Different ways to import:

```python
import array
```

```python
import array as ar
```

```python
from array import *
```

***

## 4. Creating an Array

### Syntax:

```python
array(typecode, [values])
```

Example:

```python
from array import *

vals = array('i', [5, 9, -8, 4, 2])
print(vals)
```

Output:

    array('i', [5, 9, -8, 4, 2])

***

## 5. Type Codes in Arrays

Each data type has a **type code**.

| Type Code | Meaning           |
| --------- | ----------------- |
| `'b'`     | Signed byte       |
| `'B'`     | Unsigned byte     |
| `'i'`     | Signed integer    |
| `'I'`     | Unsigned integer  |
| `'l'`     | Signed long       |
| `'f'`     | Float             |
| `'d'`     | Double            |
| `'u'`     | Unicode character |

⚠️ **Important Notes**:

*   `'i'` → allows **negative values**
*   `'I'` → **no negative values**
*   Float values **cannot** be stored in integer arrays

Example Error:

```python
array('i', [5, 9, 8.5])   # ❌ Error
```

***

## 6. Common Array Methods

### `append()`

Adds a value at the end

```python
vals.append(10)
```

### `remove()`

Removes a value

```python
vals.remove(9)
```

### `reverse()`

Reverses the array **in place**

```python
vals.reverse()
```

***

## 7. `buffer_info()`

Returns:

*   Memory address
*   Number of elements

```python
vals.buffer_info()
```

Example Output:

    (address, 5)

***

## 8. `typecode`

Returns the array’s type

```python
vals.typecode
```

Output:

    'i'

***

## 9. Accessing Array Elements (Indexing)

*   Index starts from **0**

```python
print(vals[0])   # First element
```

***

## 10. Traversing an Array

### Using `for` loop (with index)

```python
for i in range(len(vals)):
    print(vals[i])
```

### Using `for` loop (direct values ✅ best)

```python
for e in vals:
    print(e)
```

***

## 11. Character (Unicode) Array

Use type code `'u'`

```python
chars = array('u', ['a', 'e', 'i'])
print(chars)
```

***

## 12. Creating a New Array from an Existing Array

### Copy values

```python
newArr = array(vals.typecode, (a for a in vals))
```

***

### Create Squares of Elements

```python
newArr = array(vals.typecode, (a*a for a in vals))
print(newArr)
```

✅ This uses **array comprehension**

***

## 13. Printing Array Using `while` Loop

```python
i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1
```

⚠️ While loop requires:

*   Initialization
*   Condition
*   Increment/Decrement

***

## 14. For Loop vs While Loop

| For Loop                 | While Loop            |
| ------------------------ | --------------------- |
| Cleaner                  | More manual           |
| Best for arrays          | Requires more steps   |
| No index handling needed | Index handling needed |

✅ **Prefer `for` loop** for arrays

***

## 15. Key Takeaways

*   Arrays store **same-type elements only**
*   Must be imported using `array` module
*   Arrays are **dynamic in size**
*   Efficient for numerical data
*   Powerful methods like:
    *   `append()`
    *   `reverse()`
    *   `buffer_info()`
*   Python allows **quick array transformations**

***

✅ **This video covered array basics, traversal, copying, and transformations.**

If you want:

*   Short revision notes
*   Interview questions
*   Practice programs
*   Comparison: List vs Array

Just tell me 👍
