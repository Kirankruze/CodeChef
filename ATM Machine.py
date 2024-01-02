# cook your dish here
T = int(input())
while(T>0):
    (N,K) = map(int,input().split(" "))
    lst = input().split()
    lst = [int(i) for i in lst]
    S=""
    for i in lst:
        if(K>=i):
            K=K-i
            S=S+"1"
        elif(K<i):
            S=S+"0"
    print(S)
    T=T-1
    
            
