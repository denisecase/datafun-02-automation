"""src/datafun/app.py - Project script.

Author: Denise Case
Date: 2026-08-20

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / New Terminal to
open an integrated Terminal in the root project folder.
Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m datafun.app

DOMAIN:

A dataset of penguins.
See docs/data-card.md for more information about the dataset.

EXPLORE:

Use Python to repeat and make decisions:
- repeat work for each item in a list
- branch based on a condition
- transform values with a list comprehension
- repeat work while a condition is true

ORGANIZATION:

This file is the main script for the project.
Execution begins at the start of the main() function.
We organize the instructions into different files
(a Python file is called a module).
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
from eda_vizkit import save_chart, show_numeric_distribution
import matplotlib.pyplot as plt
import pandas as pd

from datafun.utils_data import inspect

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

# Use the Path() constructor to create a Path object representing the "data" folder.
# Combine with the CSV file name
# to get the full path to the data file.
DATA_FILE_PATH: Final[Path] = Path("data") / "penguins.csv"

# === OPEN THE DATA FILE IN EXCEL ===

# Look in the data/ folder. Open the file in Excel.
# Understand what is there and record your observations.

# === DETERMINE WHAT A ROW REPRESENTS ===

# CUSTOM: This is the GRAIN of the dataset - the single most
# important thing to know about any dataset.
# Come up with a short phrase that describes it.
# Fill this string value AFTER exploring the data.
GRAIN: Final[str] = "one penguin"  # CUSTOM


# CUSTOM: Choose a categorical group that we could process with a for loop.
GROUP_COLUMN: Final[str] = "species"
# CUSTOM: Describe why we choose it.
# Use a triple-quoted string (three double quotes) to allow multi-line text.
# Use a raw string (r before the opening quotes) so it appears just
# like I typed it.
WHY_THIS_GROUP: Final[str] = r"""
The species column has a small number of unique values.
There are three unique species, so a for loop can
process and log each one.
"""

# CUSTOM: WHICH measurement to classify, and why this one.
MEASUREMENT_COLUMN: Final[str] = "bill_length_mm"

# CUSTOM: Describe why we choose it.
# Use a triple-quoted string (three double quotes) to allow multi-line text.
# Use a raw string (r before the opening quotes) so it appears just
# like I typed it.
WHY_THIS_MEASUREMENT: Final[str] = r"""
Bill length varies across penguins.
There is no fixed cutoff, so we'll calculate the average
and assign a classification depending on a threshold
around the average value.
"""

# CUSTOM: Set thresholds around the mean to
# classify a reading.
SHORT_THRESHOLD_MULTIPLIER: Final[float] = 0.9
LONG_THRESHOLD_MULTIPLIER: Final[float] = 1.1

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    This is where the instructions begin.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P02")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    # Use the imported privacy-preserving log_path() function
    # To indicate where we will look for the data file.
    log_path(LOG, "data file", path=DATA_FILE_PATH)

    # Call the built-in pandas `read_csv` function.
    # Store the tabular pandas DataFrame returned
    # in a local variable named `df`.

    df: pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

    LOG.info("Data loaded successfully.")

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    # Call the inspect() function to get a string
    # with basic information about the DataFrame.
    # Pass in the pandas DataFrame (df)
    # The grain (what one row represents)
    # And the log so it knows where to send messages.

    inspection_string: str = inspect(df=df, grain=GRAIN, log=LOG)

    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. REPEAT logic using a for loop.")
    LOG.info("-------------------------------")

    # Get a list of all column names in the DataFrame.
    # Use the DataFrame's `columns` attribute and convert it to a list
    # with the built-in tolist() method.
    column_names: list[str] = df.columns.tolist()

    # For each name in the column names list, log its name.
    # Note that we must use a colon at the end of the for loop line.
    # And we must indent the body of the for loop correctly.
    for name in column_names:
        LOG.info(f"Column name: {name}")

    # Up above, we choose a column to group by and log the reason for choosing it.
    LOG.info(f"Selected group column: {GROUP_COLUMN}")
    LOG.info(f"Reason for choosing this group: {WHY_THIS_GROUP}")

    # Now, let us use Python to get the unique values in the selected group column.
    # Use the df[column name] to get a one-dimensional array of values
    # by passing in the exact column name as a string (in quotes).
    # NOTE: The entry above must exactly match
    # the column name in the CSV file, including case and spaces.
    # Once we have that, we can apply the .unique() method to get the unique values.
    # Once we have that, we can apply the .tolist() method to convert
    # the array of unique values into a Python list of strings.
    unique_list: list[str] = df[GROUP_COLUMN].unique().tolist()

    # For each unique item in the list, log the value.
    for item in unique_list:
        LOG.info(f"Item: {item}")

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

    LOG.info("-------------------------------")
    LOG.info("05. BRANCH based on conditions.")
    LOG.info("-------------------------------")

    # Log the selected measurement column and the reason for choosing it.
    LOG.info(f"Selected measurement column: {MEASUREMENT_COLUMN}")
    LOG.info(f"Reason for choosing this measurement: {WHY_THIS_MEASUREMENT}")

    minimum: float = df[MEASUREMENT_COLUMN].min()
    maximum: float = df[MEASUREMENT_COLUMN].max()
    mean: float = df[MEASUREMENT_COLUMN].mean()
    LOG.info(f"{MEASUREMENT_COLUMN} - Minimum: {minimum}")
    LOG.info(f"{MEASUREMENT_COLUMN} - Maximum:  {maximum}")
    LOG.info(f"{MEASUREMENT_COLUMN} - Mean:     {mean}")
    LOG.info("-------------------------------")

    # Get the selected measurement for the first row in the DataFrame.
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
    sample_index: int = 0
    sample_reading: float = df[MEASUREMENT_COLUMN].iloc[sample_index]
    LOG.info(f"Sample {MEASUREMENT_COLUMN}: {sample_reading}")

    LOG.info(f"Short threshold multiplier: {SHORT_THRESHOLD_MULTIPLIER}")
    LOG.info(f"Long threshold multiplier:  {LONG_THRESHOLD_MULTIPLIER}")

    short_threshold: float = SHORT_THRESHOLD_MULTIPLIER * mean
    long_threshold: float = LONG_THRESHOLD_MULTIPLIER * mean

    LOG.info(f"Short threshold: {short_threshold}")
    LOG.info(f"Long threshold:  {long_threshold}")

    # Use the Python keywords if, elif, and else
    # to classify the selected measurement based on the calculated thresholds.
    # elif means "else if"
    if sample_reading < short_threshold:
        classification_string: str = "SHORT"
    elif sample_reading > long_threshold:
        classification_string: str = "LONG"
    else:
        classification_string: str = "MEDIUM"

    LOG.info(f"First row {MEASUREMENT_COLUMN} classification: {classification_string}")

    LOG.info("-------------------------------")
    LOG.info("06. REPEAT while a condition is true.")
    LOG.info("-------------------------------")

    # We can also perform logic repeatedly using a while loop.
    # This is often used for streaming data or continuously monitoring a condition.
    # In this example, we simulate streaming data by repeatedly processing
    # one measurement from the CSV file
    # every so many seconds, for a total of MAX_RECORDS measurements.

    # Constant values used by the while loop.
    MAX_RECORDS: Final[int] = 10  # CUSTOM: change this from 10.
    STREAM_WAIT_SECONDS: Final[int] = 1  # CUSTOM: Change this from 1 second.

    LOG.info("Starting to process measurements periodically...")
    LOG.info(f"Max records to process: {MAX_RECORDS}")
    LOG.info(f"Stream wait seconds: {STREAM_WAIT_SECONDS}")

    # Initialize the count variable used by the while loop.
    # By convention, counting starts at 0, so the first pass reads row 0.
    count: int = 0
    LOG.info(f"Current count: {count}")

    # Start the while loop to process measurements periodically
    # while the count is less than the maximum number of records.
    while count < MAX_RECORDS:
        # Get the measurement from row `count`, which advances each pass.
        current_measurement: float = df[MEASUREMENT_COLUMN].iloc[count]
        LOG.info(f"Current {MEASUREMENT_COLUMN}: {current_measurement}")

        count += 1
        LOG.info(f"Updated count: {count}")

        time.sleep(STREAM_WAIT_SECONDS)

    LOG.info("-------------------------------")
    LOG.info("07. VISUALIZE the selected measurement.")
    LOG.info("-------------------------------")

    LOG.info("Creating a chart to visualize the selected measurement.")
    LOG.info("We selected one numeric column, so let's look at the distribution.")

    # Define a path to save the distribution plot.
    # REQUIRED: Use the "docs/images" folder to store generated charts.
    CHART_PATH = Path("docs/images/measurement-distribution.png")

    # Call an imported function that will show a distribution plot
    # Pass in the pandas DataFrame (df) along with the selected measurement column.
    # It will return a matplotlib Axes object representing the distribution plot.
    ax = show_numeric_distribution(
        df,
        column=MEASUREMENT_COLUMN,
    )

    # call the save_chart() function and pass in the Axes and the path
    save_chart(ax, CHART_PATH)
    LOG.info(f"Chart saved successfully at {CHART_PATH}.")

    LOG.info(
        "IMPORTANT: Close chart window to continue by clicking its X or close button."
    )
    plt.show()

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
