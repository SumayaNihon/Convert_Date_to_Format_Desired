import datetime
import arrow

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

def datetime_format_converter(input,desired_format):

    datetime_input = arrow.get(input)

    output = datetime_input.strftime(desired_format)
    print(output)

datetime_format_converter(input("Enter the Date (YYYY-MM-DD) : "),input("Enter the Desired Format : "))

