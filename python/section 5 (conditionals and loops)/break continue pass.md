Here you go — a **clean, neat, beginner‑friendly cheat sheet** for **break, continue, and pass** — exactly following your video flow.  
This is perfect for revision, notes, or interview prep.

***

# ✅ Python `break`, `continue`, `pass` — Clean & Neat Cheat Sheet

***

# 1️⃣ Why These Keywords Matter

Inside loops (`for` or `while`), sometimes you need to:

*   **stop** the loop early → `break`
*   **skip** the current iteration → `continue`
*   **do nothing** (placeholder) → `pass`

These keywords control **flow inside loops**.

***

# 2️⃣ `break` — Stop the Loop Completely

Used when you want to **exit the loop immediately**, even if condition is still true.

### Use‑case example: Vending Machine

(Stop giving candies when stock ends)

```python
x = int(input("How many candies you want? "))
av = 10
i = 1

while i <= x:
    if i > av:
        print("Out of stock!")
        break           # exit the loop completely
    print("candy")
    i += 1

print("bye")
```

### What `break` does:

✔ Leaves **only the loop**  
✔ Continues with code after loop  
✔ Useful in search operations, menus, vending machine logic, etc.

***

# 3️⃣ `continue` — Skip the Current Iteration

Used when you want to **ignore current step** and jump to next iteration.

### Example: Skip numbers divisible by 3

```python
for i in range(1, 101):
    if i % 3 == 0:
        continue    # skip printing
    print(i)
```

### Behavior:

*   When condition is true → it jumps to next iteration
*   Loop does NOT stop
*   Useful for filtering values

***

# 4️⃣ `pass` — Do Nothing (Empty Block Placeholder)

Used when Python **expects a statement**,  
but you want to **leave that block empty**.

Python **does not allow empty blocks**, so we write `pass`.

### Example: Skip odd numbers using `pass`

```python
for i in range(1, 11):
    if i % 2 != 0:    # odd number
        pass          # do nothing here
    else:
        print(i)      # even numbers only
```

### When to use pass:

*   creating empty `if`, `for`, `while`, `class`, or `function`
*   writing code structure first (future code will be added later)

***

# 5️⃣ Summary Table

| Keyword      | Meaning                | Loop Continues? | Example Use                  |
| ------------ | ---------------------- | --------------- | ---------------------------- |
| **break**    | Exit loop completely   | ❌ No            | Stop on error / out of stock |
| **continue** | Skip current iteration | ✔ Yes           | Skip certain values          |
| **pass**     | Do nothing             | ✔ Yes           | Placeholder, empty block     |

***

# 6️⃣ Quick Mini‑Examples

### break

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output → 1 2 3 4

***

### continue

```python
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
```

Output → 1 2 3 4 6 7 8 9

***

### pass

```python
for i in range(5):
    pass  # Loop runs but does nothing
```

***

If you want, I can also create:
✅ Pattern-printing cheat sheet  
✅ Loop interview questions  
✅ A PDF version of all your loop notes  
Ready when you are!
