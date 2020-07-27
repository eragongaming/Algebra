#only single digit numbers

print("Use x for variable, and '+-*/=' as operators")
formula=list(input("Give the formula without spaces: "))
left=formula[:formula.index('=')]
right=formula[formula.index('='):]
if 'x' in left:
    for value in left:
        first_negative=left[0]=='-'
        if value.isnumeric():
            int(value)
            if left[value+1]=='+' and first_negative==True:
                right.append(value)
            elif left[value+1]=='-' and first_negative==True:
                right.append(-value)
            elif left[value + 1] == '+':
                right.append(-value)
            elif left[value + 1] == '-':
