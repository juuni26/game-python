
# name = "Junio Akarda"
# spasi = "  d"

# print(str(len(name)) + " is my total abjad in my name !")
# print(name.index("n", 1, 3))  # where the n in index of my name start 1 end 3
# print("this nge gas mode of my name = "+name.upper())

# benda = input("masukkan nama benda:")
# verb = input("masukkan kata kerja:")


# print("Hidup itu seperti sebuah "+benda)
# print("jika kau "+verb+" maka kau akan sukses")

# making list

# nomor_togel = [1, 13, 14, 5, 10]
# orang = ["john", "cena", "mad", "dog", "dog"]
# print(orang.count("dog"))
# orang.pop()
# print(orang.count("dog"))
# print(orang)

# nomor_togel.sort()
# print(nomor_togel)
# nomor_togel.reverse()
# print(nomor_togel)

# nomor_togel_copyan = nomor_togel.copy()
# print("ini nomor togel copyan = ", str(nomor_togel_copyan))

# function
# def halo(nama, umur):

#     print("hello", nama, ", you are %d years old" % umur)


# halo("juuni", 17)


# def pangkat2(bilangan):
#     return bilangan * bilangan

# ola = pangkat2(10)
# print(pangkat2(9))
# print(ola)
# print(ola+pangkat2(9))


# if statement
# is_girl = True
# is_beauty = False

# if is_girl and is_beauty:
#     print("you are a girl and also beautiful !")
# elif is_girl and not is_beauty:
#     print("you are girl only not beauty (kidding ^^)")
# elif is_beauty and not is_girl:
#     print("how the fuck you have a pretty face but you're not a woman ! impossible")
# else:
#     print("you neither a girl nor a beauty ! what a sad for me")

# -----------------------------------------------------------------------------
# --create programm give max using function easy
# version 1
# input1 = input("masukkin bilangan1:")
# input2 = input("masukkin bilangan2:")
# input3 = input("masukkin bilangan3:")


# max_number = max(input1, input2, input3)

# print("max number:", str(max_number))

# -----------------------------------------
# version 2 max number using if else statement
# def max_num(numb1, numb2, numb3):

#     if numb1 >= numb2 and numb1 >= numb3:
#         print("the max number is numb1:", str(numb1))
#     if numb2 >= numb1 and numb2 >= numb3:
#         print("the max number is numb2:", str(numb2))
#     if numb3 >= numb1 and numb1 >= numb2:
#         print("the max number is numb3:", str(numb3))

# max_num(211, 211, 211)


# creating first dictionary
print("test dictionary!")
kamus_berjalan = {
    "xp": "experience",
    "hp": "Health Player",
    "mp": "Mana Player",
    5: "position 5 noob"

}
print(kamus_berjalan["xp"])
print(kamus_berjalan[5])
print(kamus_berjalan.get("Xpe", "keyword ga ada"))
