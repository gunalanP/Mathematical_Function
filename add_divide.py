#user input Based addition Subtraction Methods with User Defined Function

#user input
user_input_Value_1 = int(input('Enter The 1st Value:'))
user_input_value_2 = int(input('Enter The 2nd Value:'))

#function defintion for mathematical Function

def add(x,y):
    added_value=x+y
    return added_value
def multiply(x,y):
    multi = x*y
    return multi
def divide(x,y):
    divis = x//y
    modlus = x%y
    return divis , modlus
def subtract(x,y):
    subt = x-y
    return subt




calc_add=add(user_input_Value_1,user_input_value_2)
print('\nAddition Value:',calc_add)

calc_multi= multiply(user_input_Value_1,user_input_value_2)
print('\nMultiplied Value:',calc_multi)

calc_divi= divide(user_input_Value_1,user_input_value_2)
print('\nDivided Value:',calc_divi)

calc_subt= subtract(user_input_Value_1,user_input_value_2)
print('\nSubtracted Value:',calc_subt)


input('\n\n Press Enter to exit')
