# Combine CSV Files

This Python script combines all CSV files from the directory where the script is run into a single output CSV file.

## Requirements

- Python 3

## Installation

No installation is required beyond having a Python interpreter.

## Usage

1. Place `combinecsv.py` in the directory containing the CSV files you want to combine.

2. Open a terminal/command prompt.

3. Navigate to the directory containing the CSV files and the `combinecsv.py` script. You can navigate to a directory by using the `cd` command followed by the path to the directory. For example:

```bash
cd path/to/your/directory
```

4. Run the `combinecsv.py` script with the following command:

```bash
python combinecsv.py
```

5. The script will create a new CSV file named `combined.csv` in the same directory. This file will contain all rows from all CSV files in the directory, including the header row from the first file and excluding the header rows from the remaining files.

## Notes

- Please back up your data before running the script, as dealing with files always has the risk of data loss if there's an error or unexpected behavior.
- If you want to change the name of the output file, you can do so by modifying the `output_filename` variable in the `main` function of `combinecsv.py`.
