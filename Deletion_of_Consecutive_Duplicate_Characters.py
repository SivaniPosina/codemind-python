t=int(input())
for k in range(t):
    a=input()
    l=len(a)
    c=0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            c+=1
    print(c)