def intersection(set1, set2):
    inter = list(set(set1) & set(set2))
    return inter

set_1 = [1,1,2]
set_2 = [3,1,2,4,5]
print(intersection(set_1, set_2))

set_1 = ['A','B','C']
set_2 = ['C','E', 1]
print(intersection(set_1, set_2))