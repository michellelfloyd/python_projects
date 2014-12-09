x = int(float(raw_input('Please enter a speed in miles/hour:')))

print 'You entered', x, 'miles/hour'
#There are 1609.34 meters in a mile, 117.647 barleycorn in a meter, 24 hours in a day
print 'That is equal to', 1609.344 * 117.647 * 24 * x, 'barleycorn/day'
#There are 1760 yards in a mile, a furlong is 220 yards, there are 8 furloughs in a mile, a fortnight is 2 weeks
print 'It is equal to', 8 * 336 * x, 'furlongs/fortnight'
#1 mach is 761.2 mph
print 'Converted to a mach number', x / 761.2
#The speed of light is 670616629 mph
print 'Converted to the percentage of speed of light', 100 * (x / 670616629.0)
