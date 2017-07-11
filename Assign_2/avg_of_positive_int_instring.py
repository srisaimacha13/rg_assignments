class MyError(Exception):
         def __init__(self, value):
            self.value = value
         def __str__(self):
            return repr(self.value)


import re

try:
    input_string = raw_input()
    if not input_string:
        raise MyError('String is empty.')

    
    list_of_integers = re.findall('-?\d+',input_string)

    if not list_of_integers:
        raise MyError('String contains all characters or special characters.')

    list_of_integers = list(map(float,list_of_integers))

    def avg(list_of_integers):
    
        count=0
        sum=0
        for x in list_of_integers:
            if x>0:
                count=count+1
                sum=sum+x
        if count == 0:
            raise MyError('No positive integers in string')
        return sum/count
    print avg(list_of_integers)
        
except MyError as e:
    print e



 
