# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
WEEKS_WORKED = 50

MONTHS_IN_YEAR = 12

hourly_wage = float(input("Enter hourly wage\n"))
hours_per_week = float(input("Enter hours per week\n"))

weekly_income = hourly_wage * hours_per_week

annual_income = weekly_income * WEEKS_WORKED

monthly_income = annual_income / MONTHS_IN_YEAR

print("Income Summary")
print("-" * 20)

print("Weekly income:", weekly_income)
print("Monthly income: " + str(monthly_income))
print("Annual income $ %s" % annual_income)


