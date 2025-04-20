'''"""This module provides a basic arithmetic calculator using a class-based approach."""
'''
import argparse
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
def cli_mode():
    """Run the calculator in CLI mode using command-line arguments."""
    parser = argparse.ArgumentParser(description="Basic CLI Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="Arithmetic operator")
    args = parser.parse_args()
    user = BasicCalculator(args.num1, args.num2)
    match args.operator:
        case '+':
            print(user.addition())
        case '-':
            print(user.subtraction())
        case '*':
            print(user.multiply())
        case '/':
            print(user.divide())
        case _:
            print("Invalid operator")
cli_mode()              
