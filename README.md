# Convert_Date_to_Format_Desired
# Datetime Format Converter

This is a Python script that converts a date in the format "YYYY/MM/DD" to a desired formatted string.

## Usage

You can use the `datetime_format_converter` function to convert a date in the "YYYY/MM/DD" format to a more readable format. The function takes the input date as a string argument and prints the result.

```python
import datetime

def datetime_format_converter(input,desired_format):
    datetime_input = datetime.datetime.strptime(input,"%Y/%m/%d")

    output = datetime_input.strftime(desired_format)
    print(output)

datetime_format_converter("2023/3/11","%A, %Y %b %d")
