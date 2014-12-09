try:
    x = int(float(raw_input('Please enter number of gallons of gas:')))
except:
    x = int(float(raw_input('Please enter a number:')))
print 'You entered', x, 'gallons'
# There are 3.7854 liters in a gallon
print 'This is the equivalent of', x * 3.7854, 'liters'
# It takes 1 barrel of oil to make 19.5 gallons of gas
print 'It takes', x / 19.5, 'barrels of oil to make that much gas'
#One gallon of gas produces 20 pounds of co2
print 'That much gas produces', x * 20, 'pounds of CO2'
#One gallon of ethanol produces 75700 BTUs
print 'That much ethanol produces', x * 75700, 'BTUs'
print 'That much gas costs $', x * 4.00, 'based on $4.00 per gallon'
