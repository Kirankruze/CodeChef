# cook your dish here
T=int(input())
for i in range(T):
    (X,Y,Z)=map(int,input().split(" "))
    mintime=Y/X
    if(Z-mintime>=0):
        print(int(Z-mintime))
    else:
        print("0")
