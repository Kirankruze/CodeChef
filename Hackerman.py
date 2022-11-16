# cook your dish here
T=int(input())
for i in range(T):
    (A,B)=map(int,input().split(" "))
    S=A+B
    j=1
    c=0
    while(j<=S/2):
        if(S%j==0):
            c+=1
        j+=1
    if(c==1):
        print("alice")
    else:
        print("bob")
