# Distribution Analysis

def distribution_analysis(numbers):
    if not numbers:
        return {}

    total = len(numbers)
    sortedNumbers = sorted(numbers)
    finalDictionary = {}
    count = 0

    for value in sortedNumbers:
        count += 1
        if value not in finalDictionary:
            finalDictionary[value] = f"{count / total * 100:2f}%"

    return finalDictionary

print(distribution_analysis([3,1,2,3,4,2]))
print(distribution_analysis([]))