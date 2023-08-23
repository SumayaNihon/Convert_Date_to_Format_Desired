import datetime

def datetime_format_converter(input,desired_format):
    datetime_input = datetime.datetime.strptime(input,"%Y/%m/%d")

    output = datetime_input.strftime(desired_format)
    print(output)

datetime_format_converter("2023/3/11","%A, %Y %b %d")