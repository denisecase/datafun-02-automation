# Repetition (P2)

This page introduces **repetition**: how Python repeats actions using loops.

Repetition is used when:

- processing many rows
- iterating over collections
- performing repeated tasks

## Repetition and Uses

Repetition means executing the same block of code multiple times.

- Use `for` for known collections
- Use `range()` for numeric sequences
- Use `while` for condition-based repetition
- Use list comprehensions to transfrom each item in a list to a new list

## `for` Loops (Most Common)

Use a `for` loop when you know **what you are iterating over**.

```python
for name in names:
    print(name)
```

## `range()` for Numeric Sequences

Use `range()` when you need a sequence of numbers.

```python
for year in range(2020, 2024):
    print(year)
```

Important:

- `range(start, stop)` **does not include** `stop`
- This prints 2020, 2021, 2022, 2023

Use cases:

- years
- counts
- indexes

## `while` Loops (Condition-Controlled)

Use a `while` loop when repetition depends on a condition.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Rules:

- The condition is checked before each iteration
- You must update the condition

## When NOT to Use Loops

Do not use loops to schedule work over time (e.g., “run nightly”).

That belongs to:

- operating system schedulers
- workflow tools
- pipelines

Loops are for repetition **inside** a running program.

## List Comprehensions

List comprehensions create a new list by transforming another list.

```python
lower_names = [name.lower() for name in names]
```

Use them when:

- the transformation is simple
- readability stays high

## Nested Repetition (Briefly)

Loops can be nested:

```python
for row in rows:
    for value in row:
        process(value)
```

Keep nesting shallow when possible.

## Repetition in Data Pipelines

Repetition appears everywhere in data work:

- CSV rows
- JSON records
- Excel rows
- text lines

## Common Mistakes

### Off-by-one errors

```python
range(1, 5)  # produces 1, 2, 3, 4
```

### Infinite `while` loops

Forgetting to update the condition variable.
