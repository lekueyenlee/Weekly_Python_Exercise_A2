# Example 3
# Date: 05/25/2020


def family_ages(item, **kwargs):
    ages = {}
    sort_ages = []
    #if file != '':
        #for item in args:
            #file_name = str(item)
    for key, value in kwargs.items():        
        ages.update({key: value})
        sort_ages = sorted(ages.items(), key=lambda x: x[1], reverse=False)
            
    for age in sort_ages:
        output_format = (f"{age[0]},{age[1]}\n")
        item.write(output_format) 

        #file = open(file_name, "w")

        #for age in sort_ages: 
            #print(age)
            #print(f"Name: {age[0].capitalize()}, Age: {age[1]}")
            #output_format = (f"Name: {age[0].capitalize()}, Age: {age[1]}" + "\n")
            #output_format = (f"{age[0].capitalize()},{age[1]}" + "\n")
            #output_format = (f"{age[0]},{age[1]}"+"\n")
            #file.write(output_format) 
        
        #file.close() 


#family_ages('ages.txt', reuven=48, atara=18, lee=9, shikma=16, amotz=13)