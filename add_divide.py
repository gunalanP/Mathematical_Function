#user input Based addition Subtraction Methods with User Defined Function

#user input
user_input_Value_1 = int(input('Enter The 1st Value:'))
user_input_value_2 = int(input('Enter The 2nd Value:'))

#function defintion for addition

def add(x,y):
    added_value=x+y
    return added_value

calc=add(user_input_Value_1,user_input_value_2)
print('\nFirst Value:',user_input_Value_1,'\nSecond Value',user_input_value_2,'\nAddition Value:',calc)
