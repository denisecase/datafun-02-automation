# Glossary

> Key terms for this module and professional Python projects.

## 1. Variables and Values

### variable

A name that holds a value in a program.
Variables make it possible to store, reuse, and describe data clearly.

```python
course_name: str = "Data Analytics Fundamentals"
```

The name `course_name` holds the text value on the right.
A good variable name describes what value it holds.

### constant

A variable whose value is not meant to change while the program runs.
Constants are named in `ALL_CAPS_WITH_UNDERSCORES` and use `Final` in their type hint.

```python
from typing import Final

COURSE_NAME: Final[str] = "Data Analytics Fundamentals"
```

### type hint

An annotation that declares what type of data a variable holds.
Type hints do not change how Python runs the code,
but they help editors and tools catch errors early.

```python
name: str = "Abbie"        # str is the type hint
age: int = 5               # int is the type hint
scores: list[float] = []   # list[float] is the type hint
```

### string

A sequence of characters used to represent text.
In Python, strings are surrounded by single or double quotes.

```python
city: str = "Kansas City"
```

### f-string

A formatted string that embeds variable values directly into text.
f-strings begin with the letter `f` before the opening quote.
Variable names go inside curly braces `{}`.

```python
name: str = "Abbie"
age: int = 5
print(f"{name} is {age} years old.")
# Output: Abbie is 5 years old.
```

## 2. Python Files

### file

A named collection of text or data stored on a computer.
Python source code is stored in `.py` files.
One Python file typically defines one **module**.

### module

A Python file that contains code (instructions made of variables, constants, and logic)
that can be run directly or imported by other files.
The module name is the file name without the `.py` extension.

```shell
# Runs the module named app_case inside the datafun package
uv run python -m datafun.app_case
```

### script

A Python file intended to be run directly from the terminal.
Scripts end with a **conditional execution guard** that starts execution.

### package

A folder containing Python modules.
Packages allow related modules to be grouped and imported together.
The dot in `datafun.app_case` separates the package name from the module name.

```text
src/
  datafun/
    __init__.py
    app_case.py
```

## 3. Running Code

### import

A statement that brings code from another module into the current file,
making its constants and tools available to use.

```python
import logging
from typing import Final
from datafun_toolkit.logger import get_logger
```

### logging

Recording messages about what a program is doing while it runs.
Logging is preferred over `print()` in professional projects because
log messages include timestamps, severity levels, and can be written to files.

```python
LOG.info("Starting main processing.")
LOG.warning("Value is unusually high.")
LOG.error("File not found.")
```

Common log levels from least to most severe: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

### main function

The `main()` block is the starting point of a script.
It contains the code that runs when the file is executed.

```python
def main() -> None:
    summary = get_summary()
    LOG.info(summary)
```

You don't need to understand how `def` works yet.
Just know that `main()` is where execution begins,
and it is called by the **conditional execution guard** at the bottom of the file.

### conditional execution guard

The block at the bottom of a Python script that ensures `main()` runs
only when the file is executed directly, not when it is imported by another module.

```python
if __name__ == "__main__":
    main()
```

This is standard Python practice and appears at the bottom of every script in this course.

### execute / run

To start a program so Python carries out its instructions.
"Execute" and "run" mean the same thing.

```shell
uv run python -m datafun.app_case
```
