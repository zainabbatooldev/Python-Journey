# Phase 02: Decision Making Notes

## What is Decision Making?

Decision making allows a program to choose different actions based on conditions.

---

# 1. if Statement

The `if` statement executes a block of code only when the condition is `True`.

### Syntax

```python
if condition:
    # code
```

### Example

```python
age = 18

if age >= 18:
    print("You can vote.")
```

---

# 2. if-else Statement

The `else` block runs when the `if` condition is `False`.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
num = 10

if num > 0:
    print("Positive")
else:
    print("Negative or Zero")
```

---

# 3. elif Statement

`elif` is used to check multiple conditions.

### Syntax

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

### Example

```python
marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
else:
    print("B")
```

---

# 4. Nested if

A nested if means an `if` statement inside another `if`.

### Example

```python
age = 20
citizen = "yes"

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal to |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

---

# Logical Operators

## and

Returns `True` only if **both conditions** are true.

```python
age >= 18 and age <= 60
```

---

## or

Returns `True` if **at least one condition** is true.

```python
emergency == "yes" or oxygen_level < 90
```

---

## not

Reverses the result.

```python
not True
```

---

# Programs Practiced

- Greatest of Four Numbers
- Positive, Negative or Zero Checker
- Even or Odd Checker
- Leap Year Checker
- University Admission System
- Hospital Patient Priority System

---

# Mini Project

## ATM System

### Features

- Password Verification
- Balance Checking
- Withdraw Money
- Deposit Money
- Insufficient Balance Handling

---

# Key Concepts Learned

- Conditional Statements
- Decision Making
- Comparison Operators
- Logical Operators
- Nested Conditions
- User Input Handling
- Problem Solving

---

# Summary

After completing this phase, I can:

- Use `if`, `elif`, and `else` statements.
- Write nested conditions.
- Apply comparison and logical operators.
- Solve real-world decision-making problems.
- Build beginner-level Python applications.

---

**Status:** ✅ Completed