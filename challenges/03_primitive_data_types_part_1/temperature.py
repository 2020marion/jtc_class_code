#question 1 formula for converting F to C
x = 100
celsius_100 = (x-32)*(5/9)
print(celsius_100)
#the resulting temp is a float (it has a decimal)
#question 2 convert temp of 0 degrees F to C
x = 0
celsius_0 = (x-32)*(5/9)
print(celsius_0)

#question 3 convert temp os 34.2 F to celsius
print((34.2-32)*(5/9))
#question 4 convert BACK. 5 degrees C to F
x = 5
farenheit_5 = ((9/5)*x)+32
print(farenheit_5)
#question 5 first convert 85.1 F to celsius, 
f = 85.1
celsius = (f-32)*(5/9)
print(celsius)
 #question 5 second - if they are both now celsius i can make the comparison which is hotter
print("30.2 degrees celsius is hotter than 85.1 degrees farenheit")