# Program name: MetriConversion
# Author: Pj Slover
# Date: 04/28/2022
# Summary: The purpose of this program is to convert imperial units of length to metric units of length and vice versa.
# Variables:
#   inches: a small imperial unit of length
#   feet: a submedian imperial unit of length
#   yards: a median imperial unit of length
#   miles: a large imperial unit of length
#   millimeters: a small metric unit of length
#   centimeters: a submedian metric unit of length
#   meters: a median metric unit of length
#   kilometers: a large metric unit of length

# Here the user will select a conversion method

def print_menu():
    print('01. Inches = Millimeters')
    print('02. Inches = Centimeters')
    print('03. Inches = Meters')
    print('04. Inches = Kilometers')
    print('05. Feet = Millimeters')
    print('06. Feet = Centimeters')
    print('07. Feet = Meters')
    print('08. Feet = Kilometers')
    print('09. Yards = Millimeters')
    print('10. Yards = Centimeters')
    print('11. Yards = Meters')
    print('12. Yards = Kilometers')
    print('13. Miles = Millimeters')
    print('14. Miles = Centimeters')
    print('15. Miles = Meters')
    print('16. Miles = Kilometers')
    print('17. Millimeters = Inches')
    print('18. Millimeters = Feet')
    print('19. Millimeters = Yards')
    print('20. Millimeters = Miles')
    print('21. Centimeters = Inches')
    print('22. Centimeters = Feet')
    print('23. Centimeters = Yards')
    print('24. Centimeters = Miles')
    print('25. Meters = Inches')
    print('26. Meters = Feet')
    print('27. Meters = Yards')
    print('28. Meters = Miles')
    print('29. Kilometers = Inches')
    print('30. Kilometers = Feet')
    print('31. Kilometers = Yards')
    print('32. Kilometers = Miles')
    
# The user will then be prompted to insert their data for conversion
   
def inches_millimeters():
    inches = float (input('Enter a distance in inches: '))
    millimeters = inches / 1.609
    print('Distance in millimeters: {0}'. format (millimeters))

def inches_centimeters():
    inches = float (input('Enter a distance in inches: '))
    centimeters = inches * 2.54
    print('Distance in centimeters: {0}'.format(centimeters))

def inches_meters():
    inches = float (input('Enter a distance in inches: '))
    meters = inches / 39.37
    print('Distance in meters: {0}'.format(meters))

def inches_kilometers():
    inches = float (input('Enter a distance in inches: '))
    kilometers = inches / 39370
    print('Distance in kilometers: {0}'.format(kilometers))


def feet_millimeters():
    feet = float (input('Enter a distance in feet: '))
    millimeters = feet * 305
    print('Distance in millimeters: {0}'. format (millimeters))

def feet_centimeters():
    feet = float (input('Enter a distance in feet: '))
    centimeters = feet * 30.48
    print('Distance in centimeters: {0}'.format(centimeters))

def feet_meters():
    feet = float (input('Enter a distance in feet: '))
    meters = feet / 3.281
    print('Distance in meters: {0}'.format(meters))

def feet_kilometers():
    feet = float (input('Enter a distance in feet: '))
    kilometers = feet / 3281
    print('Distance in kilometers: {0}'.format(kilometers))


def yards_millimeters():
    yards = float (input('Enter a distance in yards: '))
    millimeters = yards * 914
    print('Distance in millimeters: {0}'. format (millimeters))

def yards_centimeters():
    yards = float (input('Enter a distance in yards: '))
    centimeters = yards * 91.44
    print('Distance in centimeters: {0}'.format(centimeters))

def yards_meters():
    yards = float (input('Enter a distance in yards: '))
    meters = yards / 1.094
    print('Distance in meters: {0}'.format(meters))

def yards_kilometers():
    yards = float (input('Enter a distance in yards: '))
    kilometers = yards / 1094
    print('Distance in kilometers: {0}'.format(kilometers))


def miles_millimeters():
    miles = float (input('Enter a distance in miles: '))
    millimeters = miles * 1609000
    print('Distance in millimeters: {0}'. format (millimeters))

def miles_centimeters():
    miles = float (input('Enter a distance in miles: '))
    centimeters = miles * 160934
    print('Distance in centimeters: {0}'.format(centimeters))

def miles_meters():
    miles = float (input('Enter a distance in miles: '))
    meters = miles * 1609
    print('Distance in meters: {0}'.format(meters))

def miles_kilometers():
    miles = float (input('Enter a distance in miles: '))
    kilometers = miles * 1.609
    print('Distance in kilometers: {0}'.format(kilometers))



def millimeters_inches():
    millimeters = float (input('Enter a distance in millimeters: '))
    inches = millimeters / 25.4
    print('Distance in inches: {0}'. format (inches))

def millimeters_feet():
    millimeters = float (input('Enter a distance in millimeters: '))
    feet = millimeters / 305
    print('Distance in feet: {0}'.format(feet))

def millimeters_yards():
    millimeters = float (input('Enter a distance in millimeters: '))
    yards = millimeters / 914
    print('Distance in yards: {0}'.format(yards))

def millimeters_miles():
    millimeters = float (input('Enter a distance in millimeters: '))
    miles = millimeters / 1609000
    print('Distance in miles: {0}'.format(miles))


def centimeters_inches():
    centimeters = float (input('Enter a distance in centimeters: '))
    inches = centimeters / 2.54
    print('Distance in inches: {0}'. format (inches))

def centimeters_feet():
    centimeters = float (input('Enter a distance in centimeters: '))
    feet = centimeters / 30.48
    print('Distance in feet: {0}'.format(feet))

def centimeters_yards():
    centimeters = float (input('Enter a distance in centimeters: '))
    yards = centimeters / 91.44
    print('Distance in yards: {0}'.format(yards))

def centimeters_miles():
    centimeters = float (input('Enter a distance in centimeters: '))
    miles = centimeters / 160934
    print('Distance in miles: {0}'.format(miles))


def meters_inches():
    meters = float (input('Enter a distance in meters: '))
    inches = meters * 39.37
    print('Distance in inches: {0}'. format (inches))

def meters_feet():
    meters = float (input('Enter a distance in meters: '))
    feet = meters * 3.281
    print('Distance in feet: {0}'.format(feet))

def meters_yards():
    meters = float (input('Enter a distance in meters: '))
    yards = meters * 1.094
    print('Distance in yards: {0}'.format(yards))

def meters_miles():
    meters = float (input('Enter a distance in meters: '))
    miles = meters / 1609
    print('Distance in miles: {0}'.format(miles))


def kilometers_inches():
    kilometers = float (input('Enter a distance in kilometers: '))
    inches = kilometers * 39370
    print('Distance in inches: {0}'. format (inches))

def kilometers_feet():
    kilometers = float (input('Enter a distance in kilometers: '))
    feet = kilometers * 3281
    print('Distance in feet: {0}'.format(feet))

def kilometers_yards():
    kilometers = float (input('Enter a distance in kilometers: '))
    yards = kilometers * 1094
    print('Distance in yards: {0}'.format(yards))

def kilometers_miles():
    kilometers = float (input('Enter a distance in kilometers: '))
    miles = kilometers / 1.609
    print('Distance in miles: {0}'.format(miles))

# A conversion will be generated and printed for the user

print_menu()

choice = input('Select a conversion method: ')

if choice == '01':
    inches_millimeters()
if choice == '02':
    inches_centimeters()
if choice == '03':
    inches_meters()
if choice == '04':
    inches_kilometers()
    
if choice == '05':
    feet_millimeters()
if choice == '06':
    feet_centimeters()
if choice == '07':
    feet_meters()
if choice == '08':
    feet_kilometers()
    
if choice == '09':
    yards_millimeters()
if choice == '10':
    yards_centimeters()
if choice == '11':
    yards_meters()
if choice == '12':
    yards_kilometers()
    
if choice == '13':
    miles_millimeters()
if choice == '14':
    miles_centimeters()
if choice == '15':
    miles_meters()
if choice == '16':
    miles_kilometers()
    
if choice == '17':
    millimeters_inches()
if choice == '18':
    millimeters_feet()
if choice == '19':
    millimeters_yards()
if choice == '20':
    millimeters_miles()
    
if choice == '21':
    centimeters_inches()
if choice == '22':
    centimeters_feet()
if choice == '23':
    centimeters_yards()
if choice == '24':
    centimeters_miles()
    
if choice == '25':
    meters_inches()
if choice == '26':
    meters_feet()
if choice == '27':
    meters_yards()
if choice == '28':
    meters_miles()
    
if choice == '29':
    kilometers_inches()
if choice == '30':
    kilometers_feet()
if choice == '31':
    kilometers_yards()
if choice == '32':
    kilometers_miles()
    
