import math
# Example: we travel 10 km at 60 km/h, than another 10 km at 20 km/h, what is our average speed?

kilo = [60, 20]
kiloSum = 0

for k in kilo:
    kiloSum += 1/k

print(kiloSum)
print("Harmonic mean = 2/(1/60 + 1/20) = {0} km/h".format(len(kilo)/kiloSum))