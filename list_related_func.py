
list_a = [1, 2, 3, 4, 5]

list_reversed = reversed(list_a)

print("# reversed() function")
print("reversed([1, 2, 3, 4, 5]): ", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])): ", list(list_reversed))
print()

print("# list_reversed")
list_reversed = reversed(list_a)
for i in list_reversed:
    print(i)

print("# reversed() function and repeat statement")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

#========================================
print("===================================")
numbers = [1, 2, 3, 4, 5]
print("numbers[::-1] : ", numbers[::-1])


#========================================
print("===================================")
example_list = ["elementA", "elementB", "elementC"]

print("# just print")
print(example_list)
print()

print("# enumerate() function print")
print(enumerate(example_list))
print()

print("# convert to list() function")
print(list(enumerate(example_list)))
print()

print("# join with repeat statement")
for i, value in enumerate(example_list):
    print("{}th element is {}".format(i, value))

#========================================
print("===================================")
example_dict = {
    "keyA" : "valueA",
    "keyB" : "valueB",
    "keyC" : "valueC"
}

print("# items() function of dictionary")
print("items(): ", example_dict.items())
print()

print(" join with items() function of dictionary and repeat statement")
for key, element in example_dict.items():
    print("dictionary[{}] = {}".format(key, element))


#========================================
print("===================================")
array = []

for i in range(0, 20, 2):
    array.append(i*i)

print(array)

#========================================
print("===================================")
array = [i*i for i in range(0, 20, 2)]

print(array)

#========================================
print("===================================")
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)