# Example 1
# Date: 05/05/2020
# list comprenhension

def acrobot(input_string_value, min_word_length=1):
    acronym = ''.join([value[0].capitalize() for value in [item for item in input_string_value.split(" ")] if (len(value) >= min_word_length)])
    return acronym

#print(acrobot("Here is my String", min_word_length=3))