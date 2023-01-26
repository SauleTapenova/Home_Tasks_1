import mod_calc as c

def get_number():
    while True:
        try:
            num = float(input('Enter number: '))
            return num
        except ValueError:
            input('Error.Enter number: ')    
def menu_compl():
    
    num1 = get_number()
    num2 = get_number()
    num = get_number()
    nn = complex(num,num1)
    mm = complex(num1,num2)
    while True:
        m = input('Select an operation\n'
                    '1 - "sum+"\n'
                    '2 - "sub-"\n'
                    '3 - "mult*"\n'
                    '0 - "previos menu\n')
        match m:
            case '1':
                return print(f'{nn} + {mm} = {c.sum_data(nn,mm)}')
            case '2':
                return print(f'{nn} - {mm} = {c.sub_data(nn,mm)}')               
            case '3':
                return print(f'{nn} * {mm} = {c.mul_data(nn,mm)}')
            case '0':
                return menu()
            case _:
                print ("Err")
                break    



def menu_rac():
    num1 = get_number()  
    num2 = get_number() 
    while True:
        m = input('Select an operation\n'
                     '1 - "sum+"\n'
                     '2 - "sub-"\n' 
                     '3 - "mul*"\n'
                     '4 - "div /"\n'
                     '5 - "div //"\n'
                     '6 - "div %"\n' 
                     '7 - "pow**"\n'
                     '8 - "scrt**0.5"\n' 
                     '0 - previos menu\n'
                     ) 
        match m:
            case '1':
                return print(f'{num1} + {num2} = {c.sum_data(num1,num2)}')
            case '2':
                return print(f'{num1} - {num2} = {c.sub_data(num1,num2)}')
            case '3':
                return print(f'{num1} * {num2} = {c.mul_data(num1,num2)}')
            case '4': 
                return print(f'{num1} / {num2} = {c.div_data(num1, num2,"/")}') 
            case '5': 
                return print(f'{num1} //{num2}  = {c.div_data(num1, num2,"//")}')  
            case '6':
                return print(f'{num1} % {num2} = {c.div_data(num1, num2,"%")}')  
            case '7':
                return print(f'{num1} ** {num2} = {c.pow_data(num1,num2)}') 
            case '8':
                return print(f'{num1} ** 0.5 = {c.sqrt_data(num1)}') 
            case '0':
                return menu()
            case _:
                print ("Err")
                break    

def menu():
    print("Calculator welcome you!\n")
    while True:
        num_type = input("Enter\n"
                         "1 - compl\n"
                         "2 - ra\n"
                         "3 - ex\n")
        match num_type:
            case "1":
                return menu_compl()
            case "2":
                return menu_rac()
            case "3": 
                break
            case _:
                print("Err") 



