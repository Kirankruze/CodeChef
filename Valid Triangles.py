# cook your dish here
T=int(input())
for i in range(T):
    (A,B,C)=map(int,input().split(' '))
    S=(A+B+C)
    if (A==0 or B==0 or C==0 or S!=180):
        print("NO")
    else:
        print("YES")