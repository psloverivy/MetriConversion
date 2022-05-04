# Program name: MetriConversion
# Author: Pj Slover
# Date: 04/28/2022
# Summary: The purpose of this program is to convert imperial measurements to metric and vice versa.
# Variables:
#   kilometers: a large metric unit of measurement
#   miles: a large imperial unit of measurement
#   meters: a median metric unit of measurement
#   yards: a median imperial unit of measurement

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Meters to Yards')
    print('4. Yards to Meters')
    
def kilometers_miles():
    kilometers = float (input('Enter a distance in kilometers: '))
    miles = kilometers / 1.609
    print('Distance in miles: {0}'. format (miles))

def miles_kilometers():
    miles = float (input('Enter a distance in miles: '))
    kilometers = miles * 1.689
    print('Distance in kilometers: {0}'.format(kilometers))

def meters_yards():
    meters = float (input('Enter a distance in meters: '))
    yards = meters * 1.0936132983
    print('Distance in yards: {0}'.format(yards))

def yards_meters():
    yards = float (input('Enter a distance in yards: '))
    meters = yards * 0.9144
    print('Distance in meters: {0}'.format(meters))

print_menu()

choice = input('Select a conversion method: ')

if choice == '1':
    kilometers_miles()
if choice == '2':
    miles_kilometers()
if choice == '3':
    meters_yards()
if choice == '4':
    yards_meters()
