# Example 2
# Date: 05/15/2020

import io

def left_right_chars_2(*files, numchars=1):
    results = []

    for file in files:
        if (isinstance(file, str)):
            value = io.StringIO(file).read()
            first_character = value[:numchars]
            right_character = value[-numchars:]
            results.append(first_character + right_character)
        else:
            for record in files:
                value = io.StringIO(record).read()
                first_character = value[:numchars]
                right_character = value[-numchars:]
            
                results.append(first_character + right_character)
            #str_value = ""
            #collection = file
            #str_value.join(collection)
            #results.append(str_value)


    return results


def left_right_chars_review(*files, numchars=1):
    char_list = [
        [line.rstrip('\n')[:numchars], line.rstrip('\n')[-numchars:]]
        for file in files
        for line in file
    ]
    return char_list



def left_right_chars(*files, numchars=1):
    results = []
    #result_list = []
    
    for file in files:
        #checks to see if string
        if (isinstance(file, str)):
            first_character = file[:numchars]
            right_character = file[-numchars:]
            results.append(first_character + right_character)
        else:

            for entry in file:
                if entry:

                    left_character = entry[:numchars]
                    right_character = entry[-numchars:]
                    
                    #result_list.append(right_character)
                    #result_list.append(left_character)

                results.append([left_character, right_character])

            #worked, however it needs to loop through for 
            #left_character = file[:numchars]
            #right_character = file[-numchars:]

            #results.append(left_character + right_character)

    return results


        #first_character = file[0:numchars]
        #last_character = file[-numchars:]
        #results.append(first_character + last_character)
                        #pass
                #loops through each word in the list to get info
                #first_character = entry[slice(0,numchars)]
                #last_character = entry[-numchars:]

                #results.append(first_character + last_character)

#print(acrobot("Here is my String", min_word_length=3))
#print(left_right_chars(['a','g'], ['h', 'p'], "this is a test this is only a test"))
#, ["a", "g"]
#print(left_right_chars("this is a test this is only a test", ["a", "g"]))
print(left_right_chars('''abcdefghijklmnopqrstuvwxyz'''))