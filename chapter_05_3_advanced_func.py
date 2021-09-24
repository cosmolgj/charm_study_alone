
#==========================================================
print("=================== call param of func ======================")
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("Hello")

call_10_times(print_hello)
print()

#==========================================================
print("=================== call map & filter ======================")
def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("#result of map() function")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("#result of filter() function")
print("filter(under_3, output_b) :", output_b)
print("filter(under_3, output_b)", list(output_b))
print()

#==========================================================
print("=================== lambda func ======================")
power_lambda = lambda x : x * x
under_3_lambda = lambda x : x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power_lambda, list_input_a)
print("# result of map() function")
print("map(power_lambda, list_input_a) :", output_a)
print("map(power_lambda, list_input_a) :", list(output_a))
print()

output_b = filter(under_3_lambda, list_input_a)
print("# result of filter function")
print("filter(under_3_lambda, output_b) :", output_b)
print("filter(under_3_lambda, output_b) :", list(output_b))
print()

#==========================================================
print("=================== inline lambda ======================")
list_input_c = [1, 2, 3, 4, 5]

output_c = map(lambda x : x * x, list_input_c)
print("# result of map() function")
print("map(power, list_input_c): ", output_c)
print("map(power, list_input_c): ", list(output_c))
print()

output_d = filter(lambda x : x < 3, list_input_c)
print("# result of filter() function")
print("filter(under_3, output_d): ", output_d)
print("filter(under_3, output_d): ", list(output_d))
print()

#==========================================================
print("=================== file open ======================")
file = open("basic.txt", "w")
file.write("Hello Python Programming...!")

file.close()

#==========================================================
print("=================== file read ======================")
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)
print()

#==========================================================
print("=================== make list file ======================")
import random
hanguls = list("가나다라마바사아자차카파타하")

with open("info.txt", 'w') as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

#==========================================================
print("=================== file readlines ======================")
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / (int(height) * int(height))
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name, weight, height, bmi, result))
        print()