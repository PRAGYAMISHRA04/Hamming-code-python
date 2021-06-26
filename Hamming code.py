# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:25:35 2021

@author: pragy
"""
def binary(x):
    b=[0,0,0,0,0]
    k=1
    while(x>0):
        b[-k]=int(x%2)
        x=x//2
        k+=1
    return b
def setparity(M,Ci,C):
    D=list(map(int,M))  # making a list of integer
    print(D)
    for i in range(1,13,1): 
        B=binary(i)
        if B[-1]==1:
            C[0].append(D[12-i])
        if B[-2]==1:
            C[1].append(D[12-i])
        if B[-3]==1:
            C[2].append(D[12-i])
        if B[-4]==1:
            C[3].append(D[12-i])
        if B[-5]==1:
            C[4].append(D[12-i])
    for i in range(4):
        if((C[i].count(1))%2)==0 :
            Ci[i]=0
        else:
            Ci[i]=1
    Ci.reverse()
    print(" Printing Parity Bits ")
    print(Ci) # Printing the parity bits
    return Ci
def XOR(a,b):
    if a==b:
        return 0
    else:
        return 1
def checkparity():
     print(" Enter sender's message ")
     M1=input()  # 010111110110
     k=0
     while(((2**k)-1)<(len(M1)+k)):
           k+=1
     CL=list()
     CI=list()
     for i in range(k):
        CI.append(0)
        CL.append(list())
     PARITY=setparity(M1,CI,CL)
     print(" Enter the received message ")
     M2=input()  # 010111010110
     CL=list()
     CI=list()
     for i in range(k):
        CI.append(0)
        CL.append(list())
     PAR=setparity(M2,CI,CL)
     if PAR==PARITY:
         print(" No error")  
     else:
         print(" Error detected")
         POS=list()
         for i in range(k):
              POS.append(XOR(PARITY[i],PAR[i]))
         print(" Found at position :")
         K=0;
         position=0
         for i in range(k):
             position+=POS[4-i]*(2**K)
             K+=1
         print(position)
         print(" The corrected message will be ")   
         D=list(map(int,M2))
         if D[len(M2)-position-1]:
            D[len(M2)-position-1]=0
         else :
            D[len(M2)-position-1]=1
         print(D)
checkparity()