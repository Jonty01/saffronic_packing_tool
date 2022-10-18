# Saffronic Packaging Tool

## Installation instructions

- Install required python3 dependencies using `pip install -r requirements.txt`.
- File paths are read from an Excel file in a specific format.
Refer to `testxl.xlsx` for more. This is a test excel file and contains paths of
files which are present on the machine in which the tool have been tested.

## Logs

- All operations are logged in a file named `.saffronic_log.csv`.
- The logs file is created in the same directory the Excel file is read from.
