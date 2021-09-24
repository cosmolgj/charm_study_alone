
#===================================================
print("============= factorial func ===============")

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))

#===================================================
print("============= factorial recursion func ===============")

def factorial_r(n):
    if n == 0:
        return 1
    else:
        return n * factorial_r(n - 1)

print("1! : ", factorial_r(1))
print("2! : ", factorial_r(2))
print("3! : ", factorial_r(3))
print("4! : ", factorial_r(4))
print("5! : ", factorial_r(5))

#===================================================
print("============= fibonacci recursion func ===============")

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(1) : ", fibonacci(1))
print("fibonacci(2) : ", fibonacci(2))
print("fibonacci(3) : ", fibonacci(3))
print("fibonacci(4) : ", fibonacci(4))
print("fibonacci(5) : ", fibonacci(5))
print()

#===================================================
print("============= fibonacci count func ===============")
counter = 0

def fibonacci_cnt(n):
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci_cnt(n - 1) + fibonacci_cnt(n - 2)

print("value of fibonacci ({}) : {}".format(35, fibonacci_cnt(35)))
print("count of fibonacci : {}".format(counter))
print()

#===================================================
print("============= fibonacci memo func ===============")
dic = {
    1 : 1,
    2 : 2
}

def fibonacci_m(n):
    if n in dic:
        return dic[n]
    else:
        output = fibonacci_m(n - 1) + fibonacci_m(n - 2)
        dic[n] = output
        return output

print("fibonacci(10) : ", fibonacci_m(10))
print("fibonacci(20) : ", fibonacci_m(20))
print("fibonacci(30) : ", fibonacci_m(30))
print("fibonacci(40) : ", fibonacci_m(40))
print("fibonacci(50) : ", fibonacci_m(50))