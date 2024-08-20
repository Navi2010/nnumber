base = float(input('enter the base number: '))
exponent = int(input('enter the exponent you want to use: '))

result = 1

for _ in range(exponent):
    result = result * base

print ("base: ", base)
print ("to the power of: ", exponent)
print ('is: ', result)