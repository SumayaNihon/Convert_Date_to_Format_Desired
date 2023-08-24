# Convert_Date_to_Format_Desired
# Datetime Format Converter

This is a Python script that converts a date in the format "YYYY/MM/DD" to a desired formatted string.

## Usage

You can use the `datetime_format_converter` function to convert a date in the your own desired format for more readablility. The function takes the input date as a string argument and prints the desired result.

## How to Run

1. Clone the repository or download the script.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command python script_name.py.

## Example

**Suppose you run the script and enter the following inputs:**


> Enter the Date (YYYY/MM/DD):  2023/08/23

`Enter the Desired Format:     %A, %Y %b %d`

**The output will be:**

```Tuesday, 2023 Aug 23```


## Code
```python
import datetime

def datetime_format_converter(input,desired_format):

    datetime_input = datetime.datetime.strptime(input,"%Y/%m/%d")

    output = datetime_input.strftime(desired_format)
    print(output)

datetime_format_converter(input("Enter the Date (YYYY/MM/DAY) : "),input("Enter the Desired Format : "))

