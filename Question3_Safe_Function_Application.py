# Safe Function Application

def power(x1, y1):
    return x1 ** y1

pairs = [[5,2],[3,-1],[4,3],[2,0]]

results = []

for x,y in pairs:
    if not y < 0:
        results.append(pow(x,y))

print(results)



