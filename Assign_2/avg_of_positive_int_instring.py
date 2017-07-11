class MyError(Exception):
         def __init__(self, value):
            self.value = value
         def __str__(self):
            return repr(self.value)


import re
s=raw_input()
try:
    a=re.findall('-?\d+',s)
    if not a:
        raise MyError('')
    a=list(map(float,a))
    def avg(a):
    
        count=0
        sum=0
        for x in a:
            if x>0:
                count=count+1
                sum=sum+x
        return sum/count
    print avg(a)
        
except (MyError , ZeroDivisionError):
    print 'No positive integers in the string'




 
