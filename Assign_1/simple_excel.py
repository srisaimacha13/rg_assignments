import pandas as pd
import operator

#######operatorsdictionary######

operator = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%'  : operator.mod,
        '^' : operator.xor,
        '**': operator.pow
        }

######setValue########
def setValue():
    s = raw_input('Enter set value command in format <DestinationCell> = value :')
    df.ix[int(s[1]),s[0]] = int(s.split()[-1])

    if setExpression_commands:
        for i in range(0,len(setExpression_commands)):
            
             setExpression(setExpression_commands[i])
        
    print df

######setExpression#####

def setExpression(com):
    if com:
        try:
            df.ix[int(com[1]),com[0]] = operator[com.split()[3]](df.ix[int(com.split()[2][1]),com.split()[2][0]],df.ix[int(com.split()[4][1]),com.split()[4][0]])
        except ZeroDivisionError:
            print "denominator is zero"
    return df    


#####ActionList#######

d = {chr(k+65) :[' ' for i in range(0,10)] for j in range(0,10*10,10) for k in range(0,10)} #empty dictionary

df = pd.DataFrame(d)

setExpression_commands = []


while True:
    main_input = str(raw_input("Action List: \n 1) Set Value \n 2) Set Expression \n 3) Exit \nEnter your action choice:\t"))
    
    if main_input.strip() == '1':
        
        #input_1 = "C1 = 11"
        setValue()
    if main_input.strip() == '2':
        setExpression_commands.append(raw_input("Enter Set Expression Command in format <DestinationCell> = <Cell1> <operator> <Cell2> :"))
        print setExpression(setExpression_commands[-1])
       
    if main_input.strip() == '3':
        print "Bye!"
        exit()
    else:
        print "Please enter 1 or 2 or 3 as per the actions listed"

