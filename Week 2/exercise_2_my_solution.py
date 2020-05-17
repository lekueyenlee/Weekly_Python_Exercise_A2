# Example 2
# Date: 05/15/2020


def left_right_chars():
    pass

def acrobot(input_string_value, min_word_length=1):
    list_values = []
    acronym = []
    
    if input_string_value:
        list_values = input_string_value.split(" ")
        
        for value in list_values:
            if (len(value) >= min_word_length):
                letter = value[0].capitalize()
                acronym.append(letter)
            else:
                pass
    else:
        pass

    return ''.join(acronym)

#print(acrobot("Here is my String", min_word_length=3))