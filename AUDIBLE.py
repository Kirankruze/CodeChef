# cook your dish here
n=int(input())
#binary can hear in range of 67hz to 45000hz
for i in range(0,n):
    z=int(input())
    if(z>=67 and z<=45000):
        print("YES")
    else:
        print("NO")