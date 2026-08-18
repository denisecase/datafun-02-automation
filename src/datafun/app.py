"""src/datafun/app.py - Project script.

Author: Denise Case
Date: 2026-08

DOMAIN: Penguins

Operate on a dataset of penguins with Python.

EXPLORE:

Use Python to repeat and make decisions:
- repeat work for each item in a list
- branch based on a condition
- transform values with a list comprehension
- repeat work while a condition is true

DESIGN:

Use this file to document your analysis
and orchestrate the work.
The functions that do the work live in process_utils.py.
We import those functions and pass them the
information they need.

RUN:

Open an integrated Terminal in the root project folder
and paste the following command to run this file as a script.
After pasting, press Enter to execute the command.

uv run python -m datafun.app

SKILLS:

This project illustrates several core Python skills:

- functions (encapsulate reusable instructions)
- calling functions in another file (import them, then pass what they need)
- for loops (repeat work for each item)
- branching with if / elif / else (choose what happens)
- list comprehensions (transform a collection of values)
- while loops (repeat while a condition is true)
- main function (where the instructions begin)
- conditional execution guard (where to start when this module is run as a script)

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import pandas as pd

from datafun.data_utils import inspect, load_data

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P02", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT,
# they do NOT change when the program runs.
# By convention, constants are named in
# UPPERCASE_WITH_UNDERSCORES.
# `Final` is added to indicate these variables
# should not be reassigned.

# === PATHS ARE IMPORTANT ===

# Clearly define relative paths to important items (like data files).
# The `Python Standard Library` is available in every Python project.

# One of the modules in the Python Standard Library is `pathlib`,
# which provides classes for handling filesystem paths.

# === LOCATE THE DATA FILE ===

# Use the Path() constructor to create a Path object
# representing the "data" folder.
DATA_FOLDER_PATH: Final[Path] = Path("data")

# Combine the data folder path
# with the CSV file name to get the
# full path to the data file.
DATA_FILE_PATH: Final[Path] = DATA_FOLDER_PATH / "penguins.csv"

# === DETERMINE WHAT A ROW REPRESENTS ===

# This is the GRAIN of the dataset - the single most
# important thing to know about any dataset.
# Come up with a short phrase that describes it.
# Fill this string value AFTER exploring the data.
GRAIN: Final[str] = "one penguin"


# WHAT categorical groups we want to process with a for loop.
GROUP_COLUMN: Final[str] = "species"
GROUP_VALUES: Final[list[str]] = [
    "Adelie",
    "Chinstrap",
    "Gentoo",
]

# WHAT measurement we want to explore.
MEASUREMENT_COLUMN: Final[str] = "body_mass_g"

# VALUES used to branch and describe a body mass.
LOW_MASS_G: Final[float] = 3500.0
HIGH_MASS_G: Final[float] = 4500.0
EXAMPLE_MASS_G: Final[float] = 4000.0


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.
    This is where the instructions begin.
    We call other functions to do the work
    and let this main() function show the process.
    Each function receives the information
    it needs because we "pass it in"
    through the parentheses that follow the function name.

    Functions are blocks of code that are
    easy to test and easy to reuse.

    The main function often takes no arguments
    see the empty parentheses in the function definition
    and returns no value (indicated by the -> None) in the
    function definition above.

    We document the arguments and return value of every function
    in these triple quoted strings.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P02")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    log_path(LOG, label="Data folder", path=DATA_FOLDER_PATH)
    log_path(LOG, label="Data file", path=DATA_FILE_PATH)

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    # Call the load_data function to read the CSV file into a DataFrame.
    # Pass in
    # 1. the relative path to the data file.
    # 2. the logger so the function can write to the same stream.
    # Store the resulting DataFrame in the variable named `df`.

    df: pd.DataFrame = load_data(
        data_file=DATA_FILE_PATH,
        log=LOG,
    )

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    # Call the inspect function to get a string
    # with basic information about the DataFrame.

    inspection_string: str = inspect(
        df=df,
        grain=GRAIN,
        log=LOG,
    )
    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. REPEAT logic using a for loop.")
    LOG.info("-------------------------------")

    # Get a list of all column names in the DataFrame.
    # Use the DataFrame's columns attribute and convert it to a list
    # Using the `columns` attribute built in tolist() method.
    column_names: list[str] = df.columns.tolist()

    # For each name in the column names list, log its name.
    # Note that we must use a colon at the end of the for loop line.
    # And we must indent the body of the for loop correctly.
    for name in column_names:
        LOG.info(f"Column name: {name}")

    # Get a list of all unique species in the DataFrame.
    # Use the df[column name] to get a one-dimensional array of values
    # by passing in the exact column name as a string (in quotes).
    # Then call the unique() method to get unique values.
    # Then call the tolist() method to convert
    # the array of unique values into a Python list.
    unique_species_list: list[str] = df["species"].unique().tolist()

    # For each unique species in the list, log its name.
    for species in unique_species_list:
        LOG.info(f"Species: {species}")

    LOG.info("-------------------------------")
    LOG.info("04. TRANSFORM one list to another list.")
    LOG.info("-------------------------------")

    # Python uses something called a "list comprehension"
    # to transform one list into another when the transformation is simple.
    # It is often more concise and readable than using a for loop.
    # The list comprehension syntax is:
    # [expression for item in iterable]
    # where the expression is a simple transformation applied to each item.

    # Common simple string transformations include:
    # - converting strings to uppercase. e.g., name.upper()
    # - converting strings to lowercase. e.g., name.lower()
    # - stripping whitespace, e.g., name.strip()

    capitalized_column_names: list[str] = [name.upper() for name in column_names]
    LOG.info(f"Capitalized column names: {capitalized_column_names}")

    # common string transformations include:
    # - converting strings to lowercase. e.g., name.lower()
    # - stripping whitespace, e.g., name.strip()

    LOG.info("-------------------------------")
    LOG.info("05. BRANCH based on conditions.")
    LOG.info("-------------------------------")

    bill_length_mm_minimum: float = df["bill_length_mm"].min()
    bill_length_mm_maximum: float = df["bill_length_mm"].max()
    bill_length_mm_average: float = df["bill_length_mm"].mean()
    LOG.info(f"Bill length (mm) - Minimum: {bill_length_mm_minimum}")
    LOG.info(f"Bill length (mm) - Maximum: {bill_length_mm_maximum}")
    LOG.info(f"Bill length (mm) - Average: {bill_length_mm_average}")
    LOG.info("-------------------------------")

    # Get the bill length for the first row in the DataFrame.
    # Provide the exact column name as a string to access its values
    # as an array-like object, from which we can select specific rows using iloc.
    # iloc stands for "index location" and is used to select rows by their integer index.
    # Python starts counting at 0, so iloc[0] refers to the first row.
    # If it helps, you can think of it as 0 as "different from the list start".
    # There is no difference between the first item and the start of the list so
    # its offset or index is 0,
    # and it can be accessed using iloc[0]
    # The second item is one away from the start,
    # so it can be accessed using iloc[1].
    bill_length_mm_first: float = df["bill_length_mm"].iloc[0]
    LOG.info(f"First row bill length (mm): {bill_length_mm_first}")

    # Calculate some thresholds for classifying bill lengths.
    SHORT_THRESHOLD: Final[float] = bill_length_mm_average * 0.9
    LONG_THRESHOLD: Final[float] = bill_length_mm_average * 1.1
    LOG.info(f"Short threshold: {SHORT_THRESHOLD}")
    LOG.info(f"Long threshold:  {LONG_THRESHOLD}")

    # Use the Python keywords if, elif, and else
    # to classify the bill length based on the calculated thresholds.
    # elif means "else if"
    if bill_length_mm_first < SHORT_THRESHOLD:
        classification_string: str = "SHORT"
    elif bill_length_mm_first > LONG_THRESHOLD:
        classification_string: str = "LONG"
    else:
        classification_string: str = "MEDIUM"

    LOG.info(f"First row bill length classification: {classification_string}")

    LOG.info("-------------------------------")
    LOG.info("06. REPEAT while a condition is true.")
    LOG.info("-------------------------------")

    # We can also perform logic repeatedly using a while loop.
    # This is often used for streaming data or continuously monitoring a condition.
    # In this example, we simulate streaming data by repeatedly processing
    # one measurement from the CSV file
    # every so many seconds, for a total of MAX_RECORDS measurements.

    # Constant values used by the while loop.
    MAX_RECORDS: Final[int] = 10
    STREAM_WAIT_SECONDS: Final[int] = 1

    LOG.info("Starting to process measurements periodically...")
    LOG.info(f"Max records to process: {MAX_RECORDS}")
    LOG.info(f"Stream wait seconds: {STREAM_WAIT_SECONDS}")

    # Initialize the count variable used by the while loop.
    count: int = 0
    LOG.info(f"Current count: {count}")

    # Start the while loop to process measurements periodically
    # while the count is less than the maximum number of records.
    while count < MAX_RECORDS:
        # Get the current measurement from the first row of the DataFrame.
        current_measurement: float = df["bill_length_mm"].iloc[count]
        LOG.info(f"Current bill length (mm): {current_measurement}")

        count += 1
        LOG.info(f"Updated count: {count}")

        time.sleep(STREAM_WAIT_SECONDS)

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard.

if __name__ == "__main__":
    main()
