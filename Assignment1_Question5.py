# Circle Area Comparison With Validation

import math as Math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 or radiusOfCircle2 < 0:
        Invalid = print("Please give positive integers for both radii.")
        return Invalid

    areaCircle1 = Math.pi * radiusOfCircle1 ** 2
    areaCircle2 = Math.pi * radiusOfCircle2 ** 2

    if areaCircle1 < areaCircle2:
        areaCoverage = areaCircle1 / areaCircle2
    else:
        areaCoverage = areaCircle2 / areaCircle1
    return areaCoverage

print(circleAreaCoverage(4, 4))


