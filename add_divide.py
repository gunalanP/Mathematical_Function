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
    divis = x/y
    modlus=x%y
    print(modlus)
    return divis
def subtract(x,y):
    subt = x-y
    return subt




calc_add=add(user_input_Value_1,user_input_value_2)
print('\nFirst Value:',user_input_Value_1,'\nSecond Value',user_input_value_2,'\nAddition Value:',calc_add)

calc_multi= multiply(user_input_Value_1,user_input_value_2)
print('\nFirst Value:',user_input_Value_1,'\nSecond Value',user_input_value_2,'\nMultiplied Value:',calc_multi)

calc_divi= divide(user_input_Value_1,user_input_value_2)
print('\nFirst Value:',user_input_Value_1,'\nSecond Value',user_input_value_2,'\nDivided Value:',calc_divi)

calc_subt= subtract(user_input_Value_1,user_input_value_2)
print('\nFirst Value:',user_input_Value_1,'\nSecond Value',user_input_value_2,'\nSubtracted Value:',calc_subt)
