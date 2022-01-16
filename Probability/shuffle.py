from random import randrange
A =[1,2,3,4,5]

def shuffle(A):
  #i from 0 - n-1 
  for i in range(len(A)-1):
    #j from i to n
    j =randrange(i,len(A))
    A[i],A[j]=A[j],A[i]
#[4, 5, 1, 2, 3]
