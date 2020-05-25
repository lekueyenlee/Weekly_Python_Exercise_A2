# Example 2
# Date: 05/15/2020


def left_right_chars(*args, numchars=1):
    results = []

    for item in args:
        for entry in item:
            results.append([entry[:numchars],entry.rstrip()[-numchars:]])
            #left_character = entry[:numchars]
            #right_character = entry.rstrip()[-numchars:]
            #results.append([left_character,right_character])
    
    return results

#print(acrobot("Here is my String", min_word_length=3))
#print(left_right_chars(['a','g'], ['h', 'p'], "this is a test this is only a test"))
#, ["a", "g"]
#print(left_right_chars("this is a test this is only a test", ["a", "g"]))
#print(left_right_chars('''abcdefghijklmnopqrstuvwxyz'''))