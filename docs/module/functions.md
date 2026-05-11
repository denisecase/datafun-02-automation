# Functions (P2)

This page introduces **functions**: named blocks of code that perform a specific task.

Functions are essential because they let you:

- organize code into logical units
- reuse logic without copying
- make programs easier to read, test, and maintain
- describe _what_ the program does at a higher level

You have already been **using** functions.
This page gives you the vocabulary to **talk about them clearly**.

## What Is a Function?

A function is a named sequence of statements that runs when it is called.

Example:

```python
def greet():
    print("Hello")
```

- `def` starts a function definition
- `greet` is the function name
- the indented block is the function body

The function does **nothing** until it is called.

## Calling a Function

To run a function, use its name followed by parentheses:

```python
greet()
```

This executes the code inside the function body.

## Why Functions Matter

Without functions:

- programs become long and repetitive
- logic is harder to understand
- changes must be made in many places

With functions:

- each function has a clear purpose
- complex programs are built from small pieces
- code reads more like a plan

Example:

```python
read_data()
process_data()
write_results()
```

This is how pipelines are expressed in Python.

## Functions with Parameters

Parameters allow functions to accept input values.

```python
def greet(name):
    print(f"Hello {name}")
```

Calling the function:

```python
greet("Alice")
```

- `name` is a parameter
- `"Alice"` is an argument

## Functions with Return Values

Some functions return a result.

```python
def add(a, b):
    return a + b
```

Calling the function:

```python
total = add(3, 4)
```

- `return` sends a value back to the caller
- execution stops at `return`

## Functions That Return Nothing

Many functions exist only to create **side effects**:

- writing files
- logging
- printing
- modifying external state

Example:

```python
def log_message(msg):
    logger.info(msg)
```

These functions return `None`.

## Type Hints (Why We Use Them)

Type hints make function inputs and outputs explicit.

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)
```

Benefits:

- clearer intent
- better editor feedback
- easier collaboration

Type hints do **not** change how Python runs.

## Function Docstrings

A docstring explains what a function does.

```python
def compute_stats(values: list[float]) -> dict:
    """Compute summary statistics for numeric values."""
```

Docstrings:

- appear immediately after `def`
- use triple quotes
- describe purpose, arguments, and return values

## Functions as Building Blocks

In your projects, functions typically do one thing:

- read data
- extract values
- compute statistics
- write output
- log activity

Example pattern:

```python
values = extract_values(data)
stats = compute_stats(values)
write_results(stats)
```

Each function is small and focused.

## `main()` as the Coordinator

Most scripts define a `main()` function.

```python
def main():
    process_csv()
    process_json()
```

`main()`:

- coordinates the workflow
- calls other functions
- contains little logic itself

## Conditional Execution Guard

This pattern appears in every project:

```python
if __name__ == "__main__":
    main()
```

Meaning:

- run `main()` if this file is executed as a script
- do nothing if the file is imported as a module

This enables reuse.

## Common Mistakes

### Forgetting parentheses when calling

```python
process_data    # WRONG
process_data()  # RIGHT
```

### Putting too much logic in one function

Functions should be focused and readable.

## How Functions Fit with Branching and Repetition

- **Operators** produce True/False
- **Branching** decides which function runs
- **Repetition** calls functions many times
- **Functions** organize the work

Together, they form readable, maintainable programs.

## Reminders

- Functions group related code
- Parameters pass data in
- Return values pass data out
- `main()` organizes the workflow
- Small functions lead to clear programs
