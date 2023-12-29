# cook your dish here
T=int(input())
V = ['a','e','i','o','u']
while(T>0):
    N=int(input())
    S=str(input())
    c=0
    for a in S:
        if a in V:
            c=0
        else:
            c+=1
        if (c==4):
            break
    if(c>=4):
        print("No")
    else:
        print("Yes")
    T=T-1
