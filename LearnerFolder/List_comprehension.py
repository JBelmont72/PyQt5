'''pythonSimplified

'''

fruits =['apples','bananas', 'strawberries']

new_fruits= []

# for fruit in fruits:
#     fruit=fruit.capitalize()
#     new_fruits.append(fruit)
# print(new_fruits)

Fruits =[fruit.upper() for fruit in fruits]
print(fruits)
print(Fruits)
## next work with boolean values
bits = [0,1,1,1,0,0,0,1,1,1]
# new_bits =[]
# for bit in bits:
#     if bit == True:
#         new_bits.append(True)
#     else:
#         new_bits.append(False)
# print(new_bits)
        
myNewBits=[True if bit == 1 else False for bit in bits]
print(myNewBits)
myCount=[bit+1 for bit in bits]
print(myCount)
