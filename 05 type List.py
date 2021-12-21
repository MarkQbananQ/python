list = ["Ola", "Ania", 23, 30, "Rafał"]
print(type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1])
# print(list[5]) IndexError: list index out of range

print(list[-1])
print(list[-2])
# print(list[-6]) IndexError: list index out of range

print(list[1:4]) # ['Ania', 23, 30]
print(list[2:]) # [23, 30, 'Rafał']

list[0] = "Kasia"
print(list) # ['Kasia', 'Ania', 23, 30, 'Rafał']

del list[2]
print(list) # ['Kasia', 'Ania', 30, 'Rafał']

print(30 in list) # True
print("Rafał" in list) # True
print("Ola" in list) # False

if "Ania" in list:
    print("Ania jest w liście list")
    print("Kolejny kod")

print("Dalszy kod")

for el in list:
    print(el)



data = [ ["Daniel", "Rafał"],
         ["Kasia", "Ania"],
         ["Ola", "Adam"] 
]

print(len(data))

print(data[1][0])
print(data[2][1])