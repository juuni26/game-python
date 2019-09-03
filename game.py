''' making programm and know how it works well !'''
from math import *
import random
import pygame
# x = 10
# x = x % 2
# print("X:", x)

# jumlah_bocah = 10 + 2 + 3 + 4 + 5 + 11 + 2*2
# print("jumlah bocah:", jumlah_bocah)
# x = sin(30)
# print("sin 30:", x)

# velocity = 60 / 12.5
# print("velocity: ", velocity)

# nama = input("namae wa :")
# akhiran = input("akhiran wa :")
# full = nama+" "+akhiran
# print("nama lengkap:", full)

# bilangan_1 = input("masukkan bilangan 1 :")
# bilangan_2 = input("masukkan bilangan 2 :")
# total = int(bilangan_1) + int(bilangan_2)
# print("hasil dari bilangan1+bilangan2=", total)

# print("indentation is great\nhere the example !")
# if True:
#     print("this is must printed because the value is true")
#     print("oyoo")
# print("this too always printed, because its outscope from indentation")
# a = 3
# b = 4
# c = a == b
# d = True

# temperature = int(input("masukkan suhu:"))

# if temperature > 40:
#     print("wedewww panas bett")
# elif temperature < 15:
#     print("wedewww dingin bangett")
# else:
#     print("suhu normal")

# nama = input("masukkan nama:")


# if nama.lower() == "juuni":
#     print("you have cool insane name")
# else:
#     print("you have good name")

# inputan = nama.upper()
# print(inputan)

print("Welcome to my code , enjoy it !")
print("Hi ! maen tebak angka yuk , coba tebak angka random dari 1-100")
print("--percobaan")


# lemah = "weak"
# for i in range(5, 0, -1):
#     print(f"hey, {i}"+(i*(".")))

# print("duarr !!")

# for i in range(3):
#     print("hello "+str(i+1))
#     for j in range(3):
#         print("hi "+str(j+1))

# total = 0

# for i in range(1, 101):
#     total = total + i

# print("total :", total)

# a = 0
# for i in range(5):
#     a += 1
# print(a)

# a = 0
# for i in range(5):
#     a = a + 1

# for i in range(5):
#     a = a+1

# print(a)

# a = 0
# for i in range(5):
#     a = a+1
#     for i in range(5):
#         a = a+1

# print(a)

# a = 0
# while a < 10:
#     print("im here !", str(a))
#     a += 1

# done = False
# while not done:
#     quit = input("do you want quit ?")
#     if quit == "y":
#         done = True
#     attack = input("does your elf atack the dragon?")
#     if attack == "y":
#         print("lol , u died")
#         done = True
#     else:
#         print("good job for your elf!")

# quit = "n"  # quit assign to string n
# while quit == "n":   # selama quit == "n" dibandingin
#     quit = input("Do you want to quit? ")

# angka = random.randrange(100)

# index = ['kucing0', 'anjing', 'kelinci']
# index1 = ['AK47', 'K2', 'MP7']

# masukkan = ""
# while masukkan != "exit":
#     masukkan = input("random pet / senjata: ")
#     random1 = random.randrange(3)
#     if masukkan.lower() == "pet":
#         print("apa yang lu dapetin buat pet : ", index[random1])
#         exit()

#     if masukkan.lower() == "senjata":
#         print("apa yang lu dapetin buat senjata : ", index1[random1])
#         exit()

# angka = random.random() * 10 + 20
# print(angka)
# tuple immutable  using ()/ list mutable using []

pygame.init()

PI = 3.141592653
BLACK = (0, 0, 0)
BLUE = (0,   0, 255)
WHITE = (255, 255, 255)
print(BLACK, BLUE)

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Juuni's Game")

done = False  # declrae flag done

clock = pygame.time.Clock()  # manage fps , berapa refresh rate per second update

# main programm
while not done:  # looping biar window ga ke closed sampai di exit
    for event in pygame.event.get():  # event masukin ke queue
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # clear screen to white . jgn taro drawing command diatas ini
    screen.fill(WHITE)
    # klo ga bakal ke apus ama command ini .

    # --- Drawing code should go here
    pygame.draw.rect(screen, BLUE, [50, 20, 500, 100], 0)

    pygame.display.flip()  # update screen dengan apa yg kita gambar

    clock.tick(60)  # limit clock game to 60 fps


pygame.quit()  # close window and quit.
