# cook your dish here
T=int(input())
for i in range(T):
    (X,Y)=map(int,input().split(" "))
    steps=0
    moved=0
    for j in range(X):
        if ((Y>1) and (Y+moved)<=X):
            moved+=Y
            steps+=1
        else:
            moved+=1
            steps+=1
        if(moved==X):
            print(steps)
            break