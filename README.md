# Convert_Date_to_Format_Desired
# Datetime Format Converter

This Python script allows users to convert input dates from various formats to a desired format using the datetime module. Users can specify the input date format as either `YYYY/MM/DD` or `YYYY/MM/DD HH:MM:SS` and provide a custom desired format using format codes.

## Usage

You can use the `datetime_format_converter` tool to convert a date in the user desired format for more readablility. The function takes the input date as a string argument and prints the desired result.

## How to Run

1. Clone the repository or download the script.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command python script_name.py.

Run the script.


The script will attempt to convert the input date to the desired format and display the output.

## Example

**Suppose you run the script and enter the following inputs:**


> **Enter the input date following the specified formats: "YYYY/MM/DD" or "YYYY/MM/DD HH:MM:SS" :  2023/08/23 or 1960/04/21 12:34:54**

> **Enter the desired format using format codes (e.g., %Y, %m %d, %A, etc.) :  %A, %Y %b %d**

**The output will be:**

> **Tuesday, 2023 Aug 23**


## Code
```python
import re
from datetime import datetime

format_specifications = """
        Available Format Codes:
        %a - Weekday as Sun, Mon
        %A - Weekday as full name as Sunday, Monday
        %w - Weekday as decimal no as 0, 1, 2...
        %d - Day of month as 01, 02
        %b - Months as Jan, Feb
        %B - Months as January, February
        %m - Months as 01, 02
        %y - Year without century as 11, 12, 13
        %Y - Year with century 2011, 2012
        %H - 24 Hours clock from 00 to 23
        %I - 12 Hours clock from 01 to 12
        %p - AM, PM
        %M - Minutes from 00 to 59
        %S - Seconds from 00 to 59
        %f - Microseconds 6 decimal numbers
        """

print(format_specifications)



input_date = input("(Date Format: (YYYY/MM/DD) OR (YYYY/MM/DD HH:MM:SS)) \n Enter the Date: ")
desired_format = input("Enter the Desired Format: ")



def is_valid_format(format_string):
    valid_format_regex = r'(%[aAbBcdHIlmMpPSyYzZ123@#$%^&(){}[\]])'
    return re.match(valid_format_regex, format_string) is not None



def convert_date(input_date, desired_format):

    if not is_valid_format(desired_format):
        return "Invalid desired format  \nExample:\nDesired Format: %A, %Y %b %d"

    try:
        parsed_date = datetime.strptime(input_date, '%Y/%m/%d %H:%M:%S')
        formatted_date = parsed_date.strftime(desired_format)
        return formatted_date
    except ValueError:
        pass


    input_date_formats = ["%Y/%m/%d", "%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%d/%m/%Y", "%d-%m-%Y"]

    for format in input_date_formats:
        try:
            parsed_date = datetime.strptime(input_date, format)
            formatted_date = parsed_date.strftime(desired_format)
            return formatted_date
        except ValueError:
            pass

    return "Invalid date format"

output_date = convert_date(input_date, desired_format)

print("Output:", output_date)

