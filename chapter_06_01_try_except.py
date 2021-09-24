#===============================================
print("=============== try-except =================")
try:
    number_input_a = int(input("integer input> "))
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
except:
    print("something's wrong")

#===============================================
print("=============== try-pass =================")

list_input_a = ["52", "273", "32", "스파이", "102"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

#===============================================
print("=============== try-pass-finally =================")
def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "hello!")
