'''"""This module provides a basic arithmetic calculator using a class-based approach."""
'''
class BasicCalculator:
    '''It is basic calculator that can perform 
    Addition,
    Subtraction,
    Multiplication
    Division'''
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        '''Performing addition'''
        return f"The result of {self.num1} + {self.num2} is {self.num1 + self.num2}"
    def subtraction(self):
        '''Performing Subtraction'''
        return f"The result of {self.num1} - {self.num2} is {self.num1 - self.num2}"
    def multiply(self):
        '''Performing Multiplication'''
        return f"The result of {self.num1} * {self.num2} is {self.num1 * self.num2}"
    def divide(self):
        '''Performing Division'''
        if self.num2 == 0:
            return 'Division by zero is not possible'
        return f"The result of {self.num1} / {self.num2} is {self.num1 / self.num2}"
def arith_oper_by_user():
    '''Taking inputs from user and vailidate those inputs'''
    try:
        print("Here is a basic calculator. You can perform:\n"
    "1. Addition \n"
    "2. Subtraction \n"
    "3. Multiplication \n"
    "4. Division \n")
        num1 = int(input("Enter First Number: "))  
        num2 = int(input("Enter Second Number: "))  
        operator = input("operator:")  
        user = BasicCalculator(num1,num2)
        match operator:
            case '+':
                result = user.addition()
                print(result)
            case '-':
                result = user.subtraction()
                print(result)
            case '*':
                result = user.multiply()
                print(result)
            case '/':
                result = user.divide()
                print(result)
            case _:
                print("something went wrong")
    except ValueError:
        print("please provide vailid numbers and operator")    
arith_oper_by_user()
