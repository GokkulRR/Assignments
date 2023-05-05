def addition(first_value,second_value):
    Sum = first_value + second_value
    print(Sum)
    print('-----------------------------------')
    
def subraction(first_value,second_value):
    Difference = first_value - second_value
    print(Difference)    
    print('-----------------------------------')
 
def Multiplication(first_value,second_value):
    Multiple = first_value * second_value
    print(Multiple)
    print('-----------------------------------')
 
def Division(first_value,second_value):
    divide = first_value / second_value
    print(divide)   
    print('-----------------------------------')

while True:
    print('''1. Addition
    2. Subraction
    3. Multiplication
    4. Division
    5. Exit''')

    User_input = int(input('\nEnter the option: '))
    
    if User_input == 1:
        first_value = int(input('First Value: '))
        Second_value = int(input('Second Value: '))
        addition(first_value,Second_value)
    elif User_input == 2:
        first_value = int(input('First Value: '))
        Second_value = int(input('Second Value: '))
        subraction(first_value,Second_value)
    elif User_input == 3:
        first_value = int(input('First Value: '))
        Second_value = int(input('Second Value: '))
        Multiplication(first_value,Second_value)
    elif User_input == 4:
        first_value = int(input('First Value: '))
        Second_value = int(input('Second Value: '))
        Division(first_value,Second_value)
    elif User_input == 5:
        print('THANK YOU FOR USING CALCULATOR')
        break
    else:
        print('Enter Valid Option')
        print('-----------------------------------')