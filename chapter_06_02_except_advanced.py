#==========================================
print("================  ===================")
try:
    number_input_a = int(input("integer input> "))
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)

#==========================================
print("================ except-as ===================")
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("integer input > "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
    exception_occurred()
except ValueError as exception:
    print("input integer!")
    print("exception : ", exception)
except IndexError as exception:
    print("out of index!")
    print("exception : ", exception)
except Exception as exception:
    print("unoticeable exception occurred!")
    print(type(exception), exception)