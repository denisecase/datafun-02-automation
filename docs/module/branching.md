# Branching (P2)

This page introduces **branching**:
how a Python program makes decisions and
chooses different paths of execution.

Branching depends directly on **operators**.
If operators produce `True` or `False`,
branching decides **what to do next**.

## What Is Branching?

Branching is the ability of a program to
execute different code blocks depending on a condition.

In Python, branching uses:

- `if`
- `elif`
- `else`

Example:

```python
if score >= 6.0:
    result = "high"
```

If the condition is `True`, the block runs.
If it is `False`, the block is skipped.

## The `if` Statement

An `if` statement evaluates a condition.

```python
if value > 0:
    print("Positive value")
```

- The condition must evaluate to `True` or `False`
- The indented block runs only when the condition is `True`

## `if` / `else`

Use `else` when there are exactly two paths.

```python
if count == 0:
    print("No records")
else:
    print("Records found")
```

Only one branch will run.

## `if` / `elif` / `else`

Use `elif` (else if) when there are multiple possible conditions.

```python
if score >= 7.5:
    level = "high"
elif score >= 5.0:
    level = "medium"
else:
    level = "low"
```

Rules:

- Conditions are checked **top to bottom**
- The **first True condition wins**
- Only one block executes

## Branching with Boolean Operators

Conditions often combine multiple comparisons using Boolean operators.

```python
if score >= 4.0 and score <= 7.5:
    status = "typical"
```

## Branching with Membership Tests

Membership operators are common in data work.

```python
if file_type in ["csv", "json", "excel"]:
    process_file()
```

## Branching for Data Validation

Branching is often used to **skip invalid data**.

```python
if value is None:
    return
```

or:

```python
if value < 0:
    logger.warning("Invalid value")
```

## Indentation Matters (Python Rule)

Branching blocks are defined by **indentation**, not braces.

```python
if condition:
    do_this()
    do_that()
```

## Common Mistakes

### Forgetting the colon

```python
# WRONG
if score > 5

# RIGHT
if score > 5:
```

### Misaligned indentation

```python
if score > 5:
print("High")  # WRONG
```

## How Branching Fits into Pipelines

Branching is used to:

- validate inputs
- skip bad rows
- choose output paths
- handle edge cases

## Reminders

- Branching controls **which code runs**
- Conditions rely on operators
- Only one branch runs per `if` chain
- Branching is essential for real data work
