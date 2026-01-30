# Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1

while product < threshold:
    product *= currentNumber
    currentNumber += 1

print("The final product is " + str(product))
print("The number that caused the product to exceed the threshold is " + str(currentNumber))