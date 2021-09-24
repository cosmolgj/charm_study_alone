
# integer
output_a = "{:d}".format(52)

# print
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# fill 0 in vacant filed
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# basic")
print(output_a)
print("# print")
print(output_b)
print(output_c)
print("# fill 0")
print(output_d)
print(output_e)

a = "Hello Python Programming!"
print(a.upper())
print(a.lower())

a = "10 20 30 40 50".split(" ")
print(a)