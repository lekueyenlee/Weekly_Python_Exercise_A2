# Exercise #4
# Date: 05/26/2020

import os
from operator import itemgetter
from io import StringIO


def cryptogrammer(*files, **kwargs):
    output = []
    key_table = {}
    #print(os.getcwd())    
    
    for key, value in kwargs.items():
        key_table[key] = value

        #print(key_table) 
    
    for file in files:
        #with open(file, 'r') as f:
        #for line in file:
            string = file.read()
            print(string)
            #for key in key_table:
            table = str.maketrans(key_table)
            print(table)
            print("I'm here")
            for key in table:
                translate = string.translate(key)
                print(translate)
                output.append(translate)
        
    return output
    
    

    #for key, value in sorted(kwargs.items(), key=itemgetter(1), reverse=True):
        #f.write(f'{name},{age}\n')
    #    print(f'{key},{value}')

        #table = str.maketrans(dict.fromkeys('0123456789'))
        #file_name.translate(table)

    

s = StringIO()

print(cryptogrammer(s, a=1))