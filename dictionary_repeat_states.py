
diction = {
    'name':'7D dried mango',
    'type':'dried sugar',
    'ingredient':['mango', 'sugar', 'metaSNa', '치차황색소'],
    'origin':'philippines'
}

print("name : ", diction['name'])
print("type : ", diction['type'])
print("ingredient : ", diction['ingredient'])
print("origin : ", diction['origin'])

diction['name'] = "8D dried mango"
print("name : ", diction['name'])
diction['price'] = 5000

print(diction)

#================================================================

dictionary = {}

print("before element add : ", dictionary)
dictionary["name"] = "new name"
dictionary["head"] = "new spirit"
dictionary["body"] = "new body"

print("after element add : ", dictionary)


#================================================================

dictionary2 = {
    "name" : "7D dried mango",
    "type" : "당절임",
    "ingredient" : ["mango", "sugar", "메타중아황산나트륨", "치차황색소"],
    "origin" : "philippines"
}

value = dictionary2.get("존지하지 않는 키")
print("value : ", value)

if value == None:
    print("accessed invalid key")
