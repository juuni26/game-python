'''
This is Just Scratch
i make for test code and learn

'''


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
# print("test dictionary!")
# kamus_berjalan = {
#     "xp": "experience",
#     "hp": "Health Player",
#     "mp": "Mana Player",
#     5: "position 5 noob"

# }
# print(kamus_berjalan["xp"])
# print(kamus_berjalan[5])
# print(kamus_berjalan.get("Xpe", "keyword ga ada"))


# making guessing game
# secret_word = "bunny"
# inputan = ""
# attempt = 3
# try1 = 1
# while inputan != secret_word and try1 <= attempt:
#     inputan = input("tebak kata depannya huruf b : ")
#     print("attempt " + str(try1))
#     print("%d left to try " % (attempt-try1))
#     try1 += 1

# if secret_word == inputan:
#     print("berhasil hore !!!")
# else:
#     print("Anda Gagal , coba lagi !")


# for
# angka = range(10)  # range is iterable but not integer

# mynum = iter(angka)
# print(next(mynum))
# print(next(mynum))
# print(next(mynum))
# print(next(mynum))


# orang = "oraa oraa "
# myorg = iter(orang)

# print(next(myorg))
# print(next(myorg))
# print(next(myorg))
# print(next(myorg))
# print(next(myorg))
# # string is iterable object


# ----

# # versi simple pangkat function
# def pangkat(angka, pangkat):
#     return angka ** pangkat


# print(pangkat(3, 9))

# # versi ribet loop
# def raise_numb(numb, power):
#     result = 1
#     for i in range(power):
#         result = result * numb
#     return result

# print(raise_numb(3, 9))

# 2d list
# from sensai import *
# angka = [
#     [1, 2, 3],
#     [9, 1, 2],
#     [0, 1, 5]
# ]

# # we can acces using row column
# print(angka[1][0])  # this will be print row = 1 and collumn 0, which is 9
# print(angka[2][2])

# # nested loop nyari angka di setiap kolom
# for baris in angka:
#     for kolom in baris:
#         print(kolom)


# we make simple translator
# setiap huruf vokal jadi z
# dog  = dzg
# def translate(kata):

#     translation = ""
#     for huruf in kata:
#         if huruf.lower() in "aiueo":
#             if huruf.isupper():
#                 translation = translation + "Z"
#             else:
#                 translation = translation + "z"

#         else:
#             translation = translation + huruf

#     return translation


# print(translate(input("Masukkan kata: ")))


# -- catching error using try and except , except can be specified and make them a special variable to define whats made error.
# try:
#     number = int(input("masukkan bilangan :"))
#     kp = 10 / 0
#     print(number)

# except ZeroDivisionError as zerosucks:
#     print("error", zerosucks)
# except ValueError as err:
#     print(err)  # print with the error description


# relative path is based on current directory, and best practice to use it in same domain/web.
# absolute path is based on root directory, it always start in the root directory, and is used to link to another domain/web except ours/


# # open file a= append, w = write/create new/overwrite the old , r = read.

# gamelist = open("index.html", "w")
# gamelist.write("<h1>this created in the python compiler, omegalull<h1?")

# gamelist = open("game.txt", "r")
# print(gamelist.read())
# gamelist = open("game.txt", "a")
# gamelist.write("\nCSGO - Good Fps Game")
# gamelist = open("game.txt", "r")
# print(gamelist.read())
# # or this print(gamelist.readlines())
# gamelist.close()  # dont forget to close the door ^^


# --------------------------------------------------------------

# pip and external python module
# we can download external python module using pip package manager, and the download will place in lib/site-packages.
# we can easily import the module, we can create to by ourself. so considering you need to use module to fasten your works !


# sensei1 = sensei("John", 50, "Karate Teacher")

# print(sensei1.name)
# print(sensei1.age)
# print(sensei1.job)
# print("sensei name is", sensei1.senseiName())

# sensei1.name = "maddog"
# print(sensei1.name)
# del sensei1.age
# sensei1.age = 50
# print(sensei1.age)

# # class is like making other data type in python / template, than object is actually the representative of the class itself/the real object that use the template.
# del for delete , modifiy just assign it to the value like sensei1.name = "bla bla"


# multiple quiz test
# class Question:

#     def __init__(self, promp, answer):

#         self.promp = promp
#         self.answer = answer


# pertanyaaan = [
#     "\nWhat is the color of banana ? \na.Blue\nb.Yellow\nc.Black\n",
#     "\nWhat is the color of sky ? \na.Blue\nb.Yellow\nc.Black\n",
#     "\nWhat is the color of hair ? \na.Blue\nb.Yellow\nc.Black\n"
# ]

# Questions = [
#     Question(pertanyaaan[0], "b"),
#     Question(pertanyaaan[1], "a"),
#     Question(pertanyaaan[2], "c")

# ]
# score = 0
# for q in Questions:
#     answer = input(q.promp)
#     if answer == q.answer:
#         score += 1
# if score == 3:
#     print("congrats perfect score !!")
#     print("score : {}/{} correct".format(score, len(Questions)))
# else:
#     print("score : {}/{} correct".format(score, len(Questions)))


# scratch

# jumlah_arr = int(input("masukkin jumlah array:"))

# array1 = []
# for i in range(jumlah_arr):

#     array1.append(int(input("masukkan array{}: ".format(i+1))))

# print(array1)

# test_2d = [
#     [1, 2, 3],
#     1, 4, 5,
#     9, 2, 1

# ]

# print(len(test_2d[0]))

# list1 = ["halo2", "hai", "3213331"]
# angka = 0
# bangka = 0
# angka = list1[0]
# bangka = list1[2]
# list1[2] = angka
# list1[0] = bangka

# print(list1[-1])

# input_kata = []

# input_kata.append("masuk")
# input_kata.append("pulang")
# print(input_kata)

# for i in range (2): #2x
#     for j in index[i]: #5x
#         if j.index() %2 == 0:
#             result1 += j
#         if j.index() %1 == 0:
#             result2 += k  #h a c k e r
#         PRINT (J,K)

# input_n = int(input())
# input_kata = []
# for i in range(input_n):
#     input_kata.append(input())
# ganjil = []
# genap = []

index = [[1, 2, 3],
         [2, 3, 2]

         ]

print(index[0][1]+index[0][0])

#
'''
1,2,3,4      index[0,1,2]  => 0,0 , 0,1 , 0,2     0,1 , 0,2 , 0,3 
4,5,6,4      index[1]     => 1,1                  1,2
2,2,2,5      index[0,1,2] -> 1,0 , 1,1 , 1,2      1,1  , 1,2, 1,3 
total 16

loop for 4 =


fibonnaci = a , b, ab ,bab, abbab ,
            0 , 1 , 


'''
