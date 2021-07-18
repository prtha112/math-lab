def diff(set1, set2):
    diff1 = list(set(set1) - set(set2))
    diif2 = list(set(set2) - set(set1))
    summary = diff1 + diif2 
    return summary

set_1 = [1,1,2]
set_2 = [3,1,2]

print(diff(set_1, set_2))