def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "hello", "pleasant", "python programming")

#=====================================
print("==================================")

def print_n_default_param_times(value, n=2):
    for i in range(n):
        print(value)

print_n_default_param_times("hello")

#=====================================
print("============= basic param after variable param =================")
def print_n_basic_variable_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_basic_variable_times("hello", "pleasant", "python programming", 3)

#=====================================
print("============= keyword param =================")
def print_n_keyword_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_keyword_times("hello", "pleasant", "python programming", n=3)

#=====================================
print("============= return value =================")
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i

    return output

print("0 to 100 : ", sum_all(0, 100))
print("0 to 1000 : ", sum_all(0, 1000))
print("50 to 100 : ", sum_all(50, 100))
print("500 to 1000 : ", sum_all(500, 1000))