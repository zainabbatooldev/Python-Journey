# 📝 Phase 03 Notes – Loops

## 🔁 What is a Loop?

A loop is used to repeat a block of code multiple times.

---

# for Loop

Used when the number of iterations is known.

### Syntax

```python
for i in range(5):
    print(i)
```

---

# range()

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Example:

```python
for i in range(1, 6):
    print(i)
```

---

# while Loop

Used when the number of iterations is unknown.

### Syntax

```python
while condition:
    # code
```

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# break

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
```

---

# continue

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# pass

A placeholder statement.

```python
for i in range(5):
    pass
```

---

# else with Loops

Runs only if the loop finishes normally.

```python
for i in range(5):
    print(i)
else:
    print("Loop Finished")
```

---

# Nested Loop

A loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# Pattern Printing

Example

```python
for i in range(5):
    print("*" * i)
```

---

# Applications of Loops

- Menu-driven programs
- Games
- Pattern printing
- Data processing
- Searching
- Counting
- Automation

---

# Key Points

- `for` → Known number of repetitions.
- `while` → Unknown number of repetitions.
- `break` → Exit loop.
- `continue` → Skip current iteration.
- `pass` → Placeholder.
- `else` → Executes after successful loop completion.