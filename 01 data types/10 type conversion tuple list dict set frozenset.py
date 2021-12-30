listData = [1,2,3,4,5,6,7,8,9]

tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 234))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Ola", 1234), ("Adam", 3124))

dictData = dict(tupleData)
print(type(dictData))
print(dictData)
print(dictData["Ola"])