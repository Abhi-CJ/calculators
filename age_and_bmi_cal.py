"""
This module contains two calculators:
1. BMI (Body Mass Index) Calculator
2. Current Age Calculator
"""

import datetime


class BmiCal:
    """It is BMI Calculator."""

    def __init__(self, user_weight, user_height):
        self.user_weight = user_weight
        self.user_height = user_height

    def bmi_cal(self):
        """Calculating BMI of user."""
        bmi = self.user_weight / (self.user_height ** 2)
        return bmi


class AgeCal:
    """It is current age calculator."""

    def __init__(self, dob):
        self.dob = dob

    def current_age_cal(self):
        """Calculating current age of user."""
        today = datetime.date.today()
        current_age = today.year - self.dob.year - (
            (today.month, today.day) < (self.dob.month, self.dob.day)
        )
        return current_age


def user_input():
    """Asking user for choosing BMI or Age calculator."""
    print("You can calculate your 'Age' or 'Body Mass Index'")
    choice = input(
        "For calculating your age enter 'age'\n"
        "For calculating your Body Mass Index enter 'bmi': "
    ).lower()

    try:
        if choice == 'bmi':
            user_weight = float(input("Enter your weight in kg:\n"))
            user_height = float(input("Enter your height in meter:\n"))
            bmi_user = BmiCal(user_weight, user_height)
            user_bmi = bmi_user.bmi_cal()
            print(f"Your BMI is: {round(user_bmi, 2)}")

        elif choice == 'age':
            dob_input = input("Enter your Date of Birth (YYYY-MM-DD):\n")
            dob_date = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
            age_user = AgeCal(dob_date)
            user_age = age_user.current_age_cal()
            print(f"Your Current Age is: {user_age}")

        else:
            print("Enter only 'age' or 'bmi'.")

    except (ValueError, TypeError, ZeroDivisionError):
        print("Please provide valid input.")


if __name__ == "__main__":
    user_input()
