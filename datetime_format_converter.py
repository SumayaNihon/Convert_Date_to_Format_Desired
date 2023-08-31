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

