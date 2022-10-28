# cook your dish here
(P1,P2,P3,P4)=map(int,input().split(" "))
li=[P1,P2,P3,P4]
W=0
for i in li:
    if(i>=10):
        W+=1
print(W)