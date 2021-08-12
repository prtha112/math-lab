import math
# link : https://www.mathsisfun.com/data/weighted-mean.html
# Example: Alex usually eats lunch 7 times a week, but some weeks only gets 1, 2, or 5 lunches.
# on 2 weeks: only one lunch for the whole week
# on 14 weeks: 2 lunches each week
# on 8 weeks: 5 lunches each week
# on 32 weeks: 7 lunches each week
lunches = [
    [2, 1], 
    [14, 2],
    [8, 5],
    [32, 7]
]

totalWeek = 0
totalLunches = 0

for l in lunches:
    totalWeek += l[0];
    totalLunches += (l[0] * l[1]);
    print(l)

print('Total week', totalWeek)
print('Total lunches', totalLunches)
print('Mean = ({0}/{1}) = {2}'.format(totalWeek, totalLunches, totalLunches/totalWeek))