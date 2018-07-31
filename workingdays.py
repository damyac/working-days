#Author: Da'Mya Campbell (damycamp@cisco.com)
#File: workingdays.py
#Date: May 2018 (c) Cisco Systems
#Description: Calculates the number of working days between two dates, excluding weekends and holidays.

import time
from dateutil import rrule
from datetime import datetime
from datetime import date

def workingdays(startdate, enddate):
    # Business days (working days) between the start date and end date
    days = list(rrule.rrule(rrule.DAILY, byweekday = range(0,5), dtstart = startdate, until = enddate))

    # List of company holidays, Memorial Day, Independence Day, Labor Day, Thanksgiving, Company Shutdown, MLK Birthday
    holidays = list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 5, byweekday = rrule.MO(-1))) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 7, bymonthday = 4)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 9, byweekday = rrule.MO(1))) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 11, byweekday = rrule.TH(4))) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 11, byweekday = rrule.FR(4))) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 25)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 26)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 27)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 28)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 29)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 30)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 12, bymonthday = 31)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 1, bymonthday = 1)) +\
    list(rrule.rrule(rrule.YEARLY, dtstart = startdate, until = enddate, bymonth = 1, byweekday = rrule.MO(3)))
    
    # Total number of working days
    totaldays = len(set(days) - set(holidays))
    return totaldays

#Example input
unit_test = 1
if unit_test :
    startdate = date(2018, 1, 1)
    enddate = date(2019, 1, 2)
    r = workingdays(startdate, enddate)
    print('The number of workingdays is', r)