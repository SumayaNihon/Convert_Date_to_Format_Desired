import datetime

def datetime_format_converter(input):
    datetime_input = datetime.datetime.strptime(input,"%Y/%m/%d")

    desired_format_converter = datetime_input.strftime("%A, %Y %b %d")
    print(desired_format_converter)

datetime_format_converter("2023/3/11")