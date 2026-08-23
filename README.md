# datafun-02-automation

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: automation with loops and branching.

## Our Approach: Learn by Doing

Data analytics requires a variety of skills.
This course builds capabilities through working projects.
**Durable skills** are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each example is a professional Python project.

## Start By Running this Example

After completing **Workflow A: Set Up Your Machine** in
[pro-analytics-02](https://denisecase.github.io/pro-analytics-02/),
then clone this example project and run it
using the provided **Workflow B: Apply Example Project**.

NOTE: Getting a professional Python environment set up and successfully
running an example project can be the most challenging part.
Go slow, follow the detailed instructions and post in the discussions
when things don't go as planned.

**Once the example runs**, you know you are in good shape.
**Only after that** is it time to read the project,
understand what it does, and start playing with it.

## Project Motivation

Explore data while learning some Python basics like branching and repetition.
Analysts often **repeat logic** (e.g. do the same thing for each observation/row
in a dataset) and **branch based on conditions**.
For example, **if** a missing value is detected,
**then** we apply special instructions.

## Use Python to Automate Logic

Python helps automate our analysis.
We will use:

- a `for` loop to repeat work for each item in a list
- a **list comprehension** to transform one list into another
- `if / elif / else` to branch based on conditions
- a `while` loop to repeat work while a condition is true

## Custom Narrative (Extracted from Output)

Selected group column: **species**

Reason for choosing this group:

The species column has a small number of unique values.
There are three unique species, so a for loop can
process and log each one.

Selected measurement column: **bill_length_mm**

Reason for choosing this measurement:

Bill length varies across penguins.
There is no fixed cutoff, so we'll calculate the average
and assign a classification depending on a threshold
around the average value.

```text
Sample bill_length_mm: 39.1
Short threshold multiplier: 0.9
Long threshold multiplier:  1.1
Short threshold: 39.529736842105265
Long threshold:  48.31412280701755
First row bill_length_mm classification: SHORT

Max records to process: 10
Stream wait seconds: 1
```

See [project.log](project.log) for more.

## Initial Results

The project creates a histogram showing the distribution
of the selected numeric measurement.

![Histogram of the selected measurement](docs/images/measurement-distribution.png)

## Working Files

Work with just these areas:

- **data/** - the CSV data file
- **src/datafun/** - the Python logic
- **docs/** - the project narrative and documentation
- **pyproject.toml** - project metadata
- **zensical.toml** - documentation site config

## Common Workflow

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
carefully.

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages,
and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have the example project,
running on your machine.
A new file `project.log` will appear in the root project folder
and running the example script will print out:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder,
change directory (cd) into the new folder,
and run `code .` to open only this example project in VS Code:

```shell
git clone https://github.com/denisecase/datafun-02-automation

cd datafun-02-automation
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14

uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
git add -A
uv run pre-commit run --all-files

# run the module
uv run python -m datafun.app

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress as you work
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Much Can Be Ignored

- You do not need to add to or modify `tests/`.
  Tests are recommended and provided for example only.
- Many files are silent helpers.
  [Explore](https://denisecase.github.io/professional-python-project-explainer/)
  as you like, but most files are never touched.
- You do NOT need to understand everything;
  let understanding build over time.

## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://denisecase.github.io/datafun-02-automation/)

## Data Card

- [Palmer Penguins Data Card](./docs/data-card.md)

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
