# v as vertex
# e as edges
# a as matrix of order v*v
# f as first_vertex
# s as second_vertex
# sv as startingvertex
# vd as visited array
# ans as answer

print("""1. Enter number of verticies in the graph
2. Enter the number of edges in graph
3. Enter the staring vertex
4. Enter the edges btw 2 vertivies!\n\n""")

# ans function
def ans(a,v,sv,vd):
    print(sv)
    vd[sv]=1
    for _ in range(v):
        if(_==sv):
            continue
        if(a[sv][_]==1):
            if(vd[_]==1):
                continue
            ans(a,v,_,vd)


v=int(input())
e=int(input())
sv=int(input())

# creation of matrix of order v*v

import numpy as np

a=np.zeros(shape=(v,v),dtype=int)

# looping for updating the matrix

for _ in range(e):
    f,s=map(int,input().split())
    a[f][s]=True
    a[s][f]=True

# created an empty array to enter the visited verticies

vd=[]
for _ in range(v):
    vd.append(0)

# anspart

ans(a,v,sv,vd)


# CodeBy: RAHUL MAHAJAN
# CF: anonymous3107
# CC: anonymous0201