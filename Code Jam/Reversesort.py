t=int(input())
case=1
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    ta=sorted(a.copy())
    mi=0
    #print(ta)
    c=0
    for i in range(n-1):
        ta=(a[i:])
        
        j=a.index(min(ta))
        a[i:j+1]=(a[i:j+1][::-1])
        #a[i],a[j]=a[j],a[i]
        c+=j-i+1
        
    print(f'Case #{case}: {c}')
    case+=1
    t-=1
