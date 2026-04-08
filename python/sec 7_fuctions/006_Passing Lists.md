Below are **clean, neat, well‑structured Python notes** based on your explanation.  
These are **revision‑ready**, beginner‑friendly, and clear enough for **interview preparation**.

***

# Python Functions – Passing Lists & Returning Multiple Values

***

## 1. Can We Pass a List to a Function?

✅ **Yes**  
In Python, a list can be passed to a function just like any other argument.

A function can:

*   Accept a **list as input**
*   Process multiple values inside that list
*   **Return multiple results**

***

## 2. Problem Statement

👉 **Input:** A list of numbers  
👉 **Task:**

*   Count how many numbers are **even**
*   Count how many numbers are **odd**
    👉 **Output:**
*   Return **both counts** from the function

***

## 3. Key Concepts Used

*   Passing a **list** to a function
*   Looping through list elements
*   Using `if-else`
*   Returning **multiple values**
*   Receiving multiple returned values

***

## 4. Function Definition

### Function Name: `count`

*   Takes **one argument**: a list
*   Returns **two values**:
    *   Number of even elements
    *   Number of odd elements

```python
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
```

***

## 5. Calling the Function

```python
nums = [12, 15, 18, 20, 25, 30, 33, 40, 42]

even_count, odd_count = count(nums)

print(even_count, odd_count)
```

### Output

    6 3

✅ Python automatically unpacks the returned tuple into two variables.

***

## 6. Printing Output in a Proper Format

```python
print("Even: {} and Odd: {}".format(even_count, odd_count))
```

### Output

    Even: 6 and Odd: 3

***

## 7. Important Points to Remember ✅

### ✅ Passing List

*   Lists are passed **by reference**
*   Function works on original list values

### ✅ Multiple Return Values

*   Python returns multiple values as a **tuple**

```python
return even, odd
```

Internally becomes:

```python
return (even, odd)
```

***

## 8. Why Functions Return Multiple Values?

✅ Cleaner code  
✅ No need for global variables  
✅ Better readability  
✅ Easier testing

***

## 9. Common Mistakes ❌

❌ Forgetting to return values  
❌ Not unpacking returned values  
❌ Using wrong modulo condition  
❌ Passing non‑list input

***

## 10. Real‑World Use Cases 🌍

### ✅ Use Case 1: Data Analysis

Counting:

*   Valid vs invalid records
*   Passed vs failed students

***

### ✅ Use Case 2: User Activity Tracking

```python
active_users, inactive_users = analyze_users(user_list)
```

***

### ✅ Use Case 3: Input Validation

Counting:

*   Valid inputs
*   Error inputs

***

## 11. Assignment (from Video)

### ✅ Task:

Take **10 names from user** and count:

*   Names having **more than 5 characters**

### Hint Solution Outline:

```python
def count_names(names):
    count = 0
    for name in names:
        if len(name) > 5:
            count += 1
    return count
```

***

## 12. Interview Questions & Answers ✅

### Q1. Can a function take a list as an argument?

**Answer:**  
Yes, Python functions can accept lists as parameters like any other object.

***

### Q2. How does Python return multiple values?

**Answer:**  
Python returns multiple values as a tuple.

***

### Q3. What is returned by this function?

```python
return even, odd
```

**Answer:**  
A tuple: `(even, odd)`

***

### Q4. How do you receive multiple returned values?

```python
a, b = function_name()
```

***

### Q5. What happens if you store it in one variable?

```python
result = count(nums)
```

**Answer:**  
`result` will contain a tuple `(even, odd)`.

***

## 13. One‑Line Summary ✅

> **Python functions can accept lists as arguments and return multiple values using tuples.**

***

If you want, I can also:

*   Convert this into **PDF notes**
*   Add **MCQs**
*   Share **practice problems**
*   Provide **real interview coding questions**

Just let me know 👍
