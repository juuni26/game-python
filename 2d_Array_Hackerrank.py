
# https://www.hackerrank.com/challenges/2d-array/problem
# 6x6 matrick , make pattern then find the max (number  )


# Complete the hourglassSum function below.


def hourglassSum(arr):
    daftar = []

    for j in range(4):

        for i in range(4):
            daftar.append(arr[0+j][0+i]+arr[0+j][1+i]+arr[0+j][2+i] +
                          arr[1+j][1+i]+arr[2+j][0+i]+arr[2+j][1+i]+arr[2+j][2+i])

    return max(daftar)
