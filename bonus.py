#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on December 2020
# This program calculates an employee's bonus

import constants


def main():
    # input
    current_salary = int(input("Enter your current salary : "))
    years_of_service = int(input("Enter your number of years of service : "))
    print("")

    # process
    bonus = current_salary*constants.BONUS_PERCENTAGE
    salary_with_bonus = current_salary + bonus

    # output
    if years_of_service > constants.REQUIREMENT:
        print("Your bonus is ${}".format(bonus))
        print("Your new salary, including bonus is ${}".format
              (salary_with_bonus))
    elif years_of_service < constants.REQUIREMENT:
        print("You need more than 5 years of service to gain a bonus:(")
    else:
        print("No clue")


if __name__ == "__main__":
    main()
