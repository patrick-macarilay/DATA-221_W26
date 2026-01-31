# Safe Function Application

def power(x1, y1):
    return x1 ** y1

pairs = [[5,2],[3,-1],[4,3],[2,0]]

results = []

for firstValue,secondValue in pairs:
    if not secondValue < 0:
        results.append(pow(firstValue,secondValue))

print(results)



