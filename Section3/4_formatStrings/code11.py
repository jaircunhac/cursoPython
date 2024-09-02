a = 'Vas'
b = 'co'
c = 3.14 # Can also use the :.1f
String = '{}{} is better than {}' # The values of the {} are defined by the order of the variables in the .format
formato = String.format(a, b, c)

String2 = '{1}{0} are not that good {2}' # Can't let the third value incomplete after using the numbers
formato2 = String2.format(a, b, c)

print(formato)
print(formato2)