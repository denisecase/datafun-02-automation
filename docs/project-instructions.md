# Project Instructions (Module 4: Exploratory Data Analysis with Notebooks)

## WEDNESDAY: Complete Workflow Phases 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs
2. Phase 2. **Change Authorship** - update the project to your name and GitHub account
3. Phase 3. **Read & Understand** - review the project structure and code

Open `notebooks/eda_case.ipynb` in VS Code, select the kernel (`.venv`), and run all cells.
Confirm the notebook executes without errors and commit it with output visible.

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Again, follow the instructions above to complete:

1. Phase 4. **Make a Technical Modification** - make a change and verify it still runs
2. Phase 5. **Apply the Skills to a New Problem**

## Phase 4 Suggestions

Make a small technical change to the example notebook that does not break it.
Choose any one of these (or a different modification as you like):

- Add a new Markdown cell with a section heading and one observation about the data
- Change the color palette or chart style in a seaborn plot
- Add a second chart of a different type (e.g., add a box plot alongside a histogram)
- Add a cell that prints the number of missing values per column using `df.isnull().sum()`
- Add a cell that filters the DataFrame to a subset of rows and re-runs a chart on the subset

Re-run all cells after your change and confirm the notebook executes cleanly.
Commit with output visible.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. EDA on a Built-in Dataset (Directed)

Use seaborn's built-in datasets to perform EDA on a dataset different from the example.

Steps:

- Choose a dataset from seaborn (see list below)
- Create a new notebook file: `notebooks/eda_yourname.ipynb`
- Follow the same numbered section structure as the example
- Include: shape, dtypes, missing values, descriptive statistics, and at least two charts
- Add Markdown narrative cells explaining your observations after each section

Good seaborn datasets for practice:

- `tips` — restaurant tipping data (244 rows, 7 columns)
- `iris` — flower measurements (150 rows, 5 columns)
- `mpg` — car fuel efficiency (398 rows, 9 columns)
- `titanic` — passenger survival data (891 rows, 15 columns)
- `diamonds` — diamond prices and attributes (53940 rows, 10 columns)

Load with: `df = sns.load_dataset('dataset_name')`

Then:

- Describe the dataset: what each column represents and where the data comes from
- Identify one surprising or interesting pattern you found
- Explain what a next analytical step might be (e.g., grouping, filtering, modeling)

### Phase 5 Suggestion 2. EDA on Your Own Dataset (Original)

Perform EDA on a dataset you bring yourself.

Steps:

- Find a tabular dataset (CSV) relevant to your field or interests
  (e.g., from <https://www.kaggle.com>, <https://data.gov>, or your own work)
- Place the file in `data/raw/`
- Create a new notebook: `notebooks/eda_yourname.ipynb`
- Load the data with `pd.read_csv()`
- Follow the same numbered section structure as the example
- Include: shape, dtypes, missing values, descriptive statistics, and at least two charts
- Add Markdown narrative explaining your observations

Then:

- Cite the data source and describe what it contains
- Identify at least one data quality issue you found (missing values, outliers, wrong types)
- Describe what question you would investigate next if you had more time

## Key Skill Focus

As you work, focus on:

- how notebooks combine narrative and code for exploratory work
- how `df.info()`, `df.describe()`, and `df.isnull()` give a quick dataset overview
- how distributions reveal shape, spread, and outliers
- how grouping and filtering expose patterns within subsets
- how Markdown narrative turns a notebook into a readable analysis

Your goal is to produce a notebook that tells a clear story about a dataset.

## Professional Communication

Make sure the title and narrative reflect your work.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub Pages)
- notebooks/ (executed notebooks committed with output visible)

Ensure your project clearly demonstrates:

- a complete EDA with all standard sections
- at least two meaningful charts with narrative
- a readable notebook someone else could follow
