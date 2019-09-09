# version 1 calculator full !
print("Welcome to my Calculator - v1")
print("choose what do you want :")
print("1.Addition ")
print("2.Substract ")
print("3.Multiply ")
print("4.division")


jawaban = 0

while jawaban < 1 or jawaban > 4:
    jawaban = int(input("masukkan input: "))
    if jawaban == 1:
        number1 = int(input("masukkan bilangan1:"))
        number2 = int(input("masukkan bilangan2:"))
        print("hasil = "+str(number1+number2))

    if jawaban == 2:
        number1 = int(input("masukkan bilangan1:"))
        number2 = int(input("masukkan bilangan2:"))
        print("hasil = "+str(number1-number2))
    if jawaban == 3:
        number1 = int(input("masukkan bilangan1:"))
        number2 = int(input("masukkan bilangan2:"))
        print("hasil = "+str(number1*number2))
    if jawaban == 4:
        number1 = int(input("masukkan bilangan1:"))
        number2 = int(input("masukkan bilangan2:"))
        print("hasil = "+str(number1/number2))

# --------------------------------------------------
# version 2 calculator
# numb1 = float(input("enter number1:"))
# operator1 = input("enter operator: ")
# numb2 = float(input("enter number2:"))

# if operator1 == "+":
#     print("hasil pertambahan:", (numb1+numb2))
# elif operator1 == "-":
#     print("hasil pengurangan:", (numb1-numb2))
# elif operator1 == "*":
#     print("hasil perkalian:", (numb1*numb2))
# elif operator1 == "/":
#     print("hasil pembagian:", (numb1/numb2))
# else:
#     print("operator invalid, yang bener woy masukinnya !")
