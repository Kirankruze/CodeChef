# cook your dish here
T=int(input())
for i in range(T):
    (N,X,Y)=map(int,input().split(" "))
    Sum=0
    flag=0
    for j in range(N+1):
        if(Sum==Y):
            flag=1
            print("YES")
            break
        Sum+=X
    if(flag==0):
        print("NO")
        