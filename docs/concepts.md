# Concepts

> Key concepts introduced in this module.

<!--
Only the first sentence/paragraph of h3 entries
are used for the integrated quiz.
Wrap code terms in double asterisks
rather than single backtics so they can be read aloud.
-->

## Programming Foundations

### Sequential Execution

**Sequential execution** runs instructions in order,
once each, from top to bottom.

Python uses sequential execution.
Useful programs often need more control than this:
the ability to decide whether an instruction runs,
and to repeat an instruction many times.

```python
value = 10
double_value = value * 2
print(double_value)
```

### Branching

Lets a program choose what to do based on a condition.

Python uses **if**, **elif**, and **else**.
The condition evaluates to either **True** or **False**,
and the program follows the matching branch.
Analytical programs use branching to respond
to different values and situations in the data.

```python
if value > 0:
    print("positive")
else:
    print("zero or negative")
```

### Boolean Expressions

A **Boolean expression** is a condition that
evaluates to **True** or **False**.

It is what branching and repetition test against.

Comparison operators include:

| Operator | Comparison               |
| -------- | ------------------------ |
| **==**   | equal to                 |
| **!=**   | not equal to             |
| **<**    | less than                |
| **<=**   | less than or equal to    |
| **>**    | greater than             |
| **>=**   | greater than or equal to |

```python
value > 10
value == 0
name == "Adelie"
```

## Repetition

Performs the same work more than once.

The work is described once, and Python repeats it.
Each pass through the repeated block is one **iteration**.

### For Loop

Repeats once for each item in a collection,
and is a good choice when the collection is already known.

```python
for value in values:
    print(value)
```

### While Loop

Repeats as long as a condition stays **True**,
and is a good choice when the number of repetitions is not known in advance.

```python
while running:
    process_data()
```

### List Comprehension (List to new List)

A **list comprehension** is a compact **for** loop that builds
a new list by transforming an existing one
with a simple transformation.

```python
upper_names = [name.upper() for name in names]
```

## Program Flow

### State

**State** is the information a program remembers while it runs,
held in variables that change as the work proceeds.

A repeating program might track how many items
it has processed (a **counter**), a running total,
the most recent values, or whether it should keep going.

### Moving Average

Summarizes a limited window of recent values.

When a new value arrives, the oldest drops out and the newest joins.
Moving summaries matter when recent observations count
for more than the full history.
For **8, 10, 12** the mean is **(8 + 10 + 12) / 3 = 10**.

---

[◄ Back to Home](index.md)
