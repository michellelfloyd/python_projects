try:
    x = int(raw_input('Please enter number of years into the future:'))
except:
    x = int(raw_input('Please enter a number:'))
sec_minute = 60
sec_hour = sec_minute * 60
sec_day = sec_hour * 24
sec_year = sec_day * 365
births = sec_year / 7
death = sec_year / 13
new_immigrant = sec_year / 35
t = births - death
t += new_immigrant
change = t * x
print 'You entered:', x
print 'In', x, 'years the population will change by', change, 'to make it', 307357870 + change
print sec_year