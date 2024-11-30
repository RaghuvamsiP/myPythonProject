"""Write a function to return 'Up' if the input number is positive,
'Down' if it's negative, and 'Zero' if it's zero."""


def number_status(num):

    if num > 0:
        return "up"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"


print(number_status(-92))
