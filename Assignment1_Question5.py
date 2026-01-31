# Circle Area Comparison With Validation
import math

def circleAreaComparison(radiusOfCircle1, radiusOfCircle2):
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Both radii must be integers."

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Both radii must be positive integers."

    area1 = math.pi * radiusOfCircle1 * radiusOfCircle1
    area2 = math.pi * radiusOfCircle2 * radiusOfCircle2

    smaller = min(area1, area2)
    larger = max(area1, area2)

    percentage = (smaller / larger) * 100

    return 'The percentage of area that the smaller circle would cover the larger circle is: ' + str(percentage)

print(circleAreaComparison(1, 2))
print(circleAreaComparison(-1, 3))
print(circleAreaComparison('it', 2))