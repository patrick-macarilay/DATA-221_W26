# Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1
integerCausingProductToExceedThreshold = 0

while product < threshold:
    product *= currentNumber
    if product > threshold:
        integerCausingProductToExceedThreshold = currentNumber
    currentNumber += 1


print("The final product is " + str(product))
print("The number that caused the product to exceed the threshold is " + str(integerCausingProductToExceedThreshold))