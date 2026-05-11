# Python Operators

> Operators are symbols that compare values, combine conditions, and produce True/False results.

Operators are used for:

- branching (`if`, `elif`, `else`)
- filtering data
- validation and decision logic

Knowing operators improves our ability to write clear analytics.

## What Is an Operator?

An operator is a symbol that performs an operation on one or more values.

Example:

```python
score > 5
```

- > is the operator
- score and 5 are operands
- the result is a Boolean: True or False

## Comparison Operators (Most Important)

Comparison operators compare two values and return True or False.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `==`     | equal to              | `x == 10` |
| `!=`     | not equal to          | `x != 10` |
| `>`      | greater than          | `x > 10`  |
| `<`      | less than             | `x < 10`  |
| `>=`     | greater than or equal | `x >= 10` |
| `<=`     | less than or equal    | `x <= 10` |

Examples:

```python
age >= 18
score < 5.0
country == "USA"
```

These are the most common operators used in data analysis.

## Boolean Operators (Combining Conditions)

Boolean operators combine multiple conditions.

| Operator | Meaning              | Example                          |
| -------- | -------------------- | -------------------------------- |
| `and`    | both must be true    | `age >= 18 and age < 65`         |
| `or`     | either can be true   | `status == "A" or status == "B"` |
| `not`    | reverses a condition | `not is_active`                  |

Examples:

```python
score >= 4.0 and score <= 7.5
region == "Europe" or region == "Asia"
not has_missing_values
```

## Membership Operators (in, not in)

Membership operators test whether a value exists in a collection.

| Operator | Meaning                                |
| -------- | -------------------------------------- |
| `in`     | value exists in a list, string, or set |
| `not in` | value does not exist                   |

Examples:

```python
"csv" in ["csv", "json", "excel"]
country not in banned_countries
```

This is commonly used when validating inputs or filtering data.

## Identity Operators (is, is not)

Identity operators test whether two variables refer to the same object, not just equal values.

| Operator | Meaning           |
| -------- | ----------------- |
| `is`     | same object       |
| `is not` | different objects |

Examples:

```python
value is None
result is not None
```

Use is primarily when checking for None.

## Arithmetic Operators (Brief Review)

Arithmetic operators perform mathematical calculations.

| Operator | Meaning          |
| -------- | ---------------- |
| `+`      | addition         |
| `-`      | subtraction      |
| `*`      | multiplication   |
| `/`      | division         |
| `//`     | integer division |
| `%`      | remainder        |
| `**`     | exponent         |

Examples:

```python
total = count \* price
average = sum(values) / len(values)
remainder = total % 2
```

## Operator Results Feed Branching

Operators are most often used inside if statements.

Example:

```python
if score >= 6.0:
   print("High score")
```

The condition inside if must evaluate to True or False.

## Common Mistakes

Using only one equal sign instead of two equal signs for comparison.

- One = is used to initialize or set a variable value.
- Two == are used to test for equality.

  WRONG: `if x = 5:`

  RIGHT: `if x == 5:` (Use == to compare)

Comparing incompatible types

WRONG: `"5" > 3` (comparing a string to an int)

RIGHT: `int("5") > 3` (Convert types explicitly when needed)
