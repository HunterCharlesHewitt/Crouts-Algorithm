import matplotlib.pyplot as plt
import numpy as np
import math

def crouts_alg(mid_diag,top_diag,bottom_diag,solution,n):
    x = []
    for i in range(0,n):
        x.append(0)
    lower = []
    upper = []
    lower_i1 = [0]
    z = []
    lower.append(mid_diag[0])
    upper.append(bottom_diag[0]/lower[0])
    z.append(solution[0]/lower[0])

    for i in range(1,n-1):
        lower_i1.append(bottom_diag[i])
        lower.append(mid_diag[i] - ((lower_i1[i])*upper[i-1]))
        upper.append(top_diag[i]/lower[i])
        z.append((solution[i] - bottom_diag[i]*z[i-1])/lower[i])

    lower_i1.append(bottom_diag[n-1])
    lower.append(mid_diag[n-1] - (lower_i1[n-1]*upper[n-2]))
    z.append((solution[n-1] - (lower_i1[n-1]*z[n-2]))/lower[n-1])

    x[n-1] = z[n-1]
    #for i in range(0,n-1):
    #   print("u: ", i, " ", upper[i])
    for i in range(n-2,-1,-1):
       x[i] = (z[i] - (upper[i]*x[i+1]))
       # print(x[i])

    return x


def make_array(val,n):
    array = []
    for i in range(0,n):
        array.append(val)
    return array

def main():
    a1 = make_array(4,16) #array a_i = 4
    b1 = make_array(1,16) #array b_i = 1
    c1 = make_array(1,16) #array c_i = 1
    f1 = make_array(1,16) #array f_i = 1
    x1 = crouts_alg(a1,b1,c1,f1,16)
    a2 = make_array(2014,16) #array a_i = 4
    b2 = make_array(4,16) #array b_i = 1
    c2 = make_array(10,16) #array c_i = 1
    f2 = make_array(14,16) #array f_i = 1
    x2 = crouts_alg(a2,b2,c2,f2,16)
    for i in range(0,len(x1)):
        print("case 1 x",i,": ", x1[i])
    print()
    for i in range(0,len(x2)):
        print("case 2 x",i,": ", x2[i])


if __name__ == "__main__":
        main()