"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def program():
  # Inputs for month and year
  month = input('Please enter month: ')
  year = input('Please enter year: ')

  try:
    # Return month current month if no inputs are entered
    if (month == '') and (year == ''):
      print('The current month is: ', datetime.now().month)

    # Returns month and current year if only month is entered
    elif (month != '') and (year ==''):
      calendar.prmonth(datetime.now().year, int(month))

    # Returns the whole calendar of that year if month is not entered
    elif (month == '') and (year !=''):
      calendar.prcal(int(year))

    # Returns the month and year if both are entered
    else:
      calendar.prmonth(int(year), int(month))
  except ValueError:
    print('Inputs are not in integer. Please try again.')

    # Restart program if there's an error
    program()
  finally:
    restart = input('Enter a new date? y or n: ')
    while (restart != 'y') and (restart != 'n'):
      restart = input('Please input y or n: ')
    else:
      if restart =='y':
        program()
      elif restart =='n':
        print('End Program')


program()