def union(set1, set2):
    listUnion = set1 + set2
    return listUnion

set_1 = [1,2,3]
set_2 = [4,5,6]
print(union(set_1, set_2))

set_1 = ['A','B','C']
set_2 = ['D','E', 1]
print(union(set_1, set_2))