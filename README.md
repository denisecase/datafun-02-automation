# datafun-02-automation

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: automation with loops, branches, and functions.

Data analytics requires a variety of skills.
This course builds capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project introduces **automation**, using code to repeat a set of logic without doing it manually.

Think of logic you might want to repeat:

- logic for each number in a sequence
- logic for each item in a list
- converting a list into another list
- logic that repeats while a condition is true

You will run the example module, read the code,
and apply the same patterns to automate your own logic.

## Working Files

You'll work with just these areas:

- **docs/** - the project narrative and documentation
- **src/datafun** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/datafun-02-automation

cd datafun-02-automation
code .
```

### In a VS Code terminal

```shell
# reset uv cache only after suspected cache corruption or strange dependency errors
# uv cache clean

uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run the module
uv run python -m datafun.app_case

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output

```shell
| P02 | ========================
| P02 | START main()
| P02 | ========================
| P02 | ========================
| P02 | FUNCTION 1: for loop over a numeric range
| P02 | ========================
| P02 | First quarter: 1
| P02 | Last quarter:  4
| P02 | Wrote file: case_quarter_1.txt
| P02 | Wrote file: case_quarter_2.txt
| P02 | Wrote file: case_quarter_3.txt
| P02 | Wrote file: case_quarter_4.txt
| P02 | ========================
| P02 | FUNCTION 2: for loop over a list
| P02 | ========================
| P02 | Pet list: ['dog', 'cat', 'fish']
| P02 | Wrote file: case_dog.txt
| P02 | Wrote file: case_cat.txt
| P02 | Wrote file: case_fish.txt
| P02 | ========================
| P02 | FUNCTION 3: list comprehension
| P02 | ========================
| P02 | Original list: ['dog', 'cat', 'fish']
| P02 | Transformed list: ['favorite_dog', 'favorite_cat', 'favorite_fish']
| P02 | Wrote file: case_favorite_dog.txt
| P02 | Wrote file: case_favorite_cat.txt
| P02 | Wrote file: case_favorite_fish.txt
| P02 | ========================
| P02 | FUNCTION 4: while loop with counter
| P02 | ========================
| P02 | Files to create: 3
| P02 | Seconds between files: 1
| P02 | Wrote file: case_01.txt
| P02 | Waiting 1 second(s)...
| P02 | Wrote file: case_02.txt
| P02 | Waiting 1 second(s)...
| P02 | Wrote file: case_03.txt
| P02 | Waiting 1 second(s)...
| P02 | ========================
| P02 | Executed successfully!
| P02 | ========================
```

![VS Code When Running](./docs/images/vscode_when_running.png)
