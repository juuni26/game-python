# https://www.hackerrank.com/challenges/30-review-loop/problem


input_n = int(input())
input_kata = []
for i in range(input_n):
    input_kata.append(input())
ganjil = []
genap = []

for i in range(input_n):
    ganjil.append("")
    genap.append("")
    kata = 0

    for huruf in input_kata[i]:
        if kata % 2 == 0:
            genap[i] += huruf
        else:
            ganjil[i] += huruf
        kata += 1

    print(genap[i], ganjil[i])
