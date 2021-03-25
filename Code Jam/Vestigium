t=int(input())
case=1
while t>0:
    a=[]
    n=int(input())
    r=0
    c=0
    
    for i in range(n):
        inp=list(map(int,input().split()))
        a.append(inp)
    trace=sum([a[i][i] for i in range(len(a)) ])
    for i in a:
        #print(i,'==',sorted(set(i), key=i.index),'?')
        if i!=sorted(set(i), key=i.index):
            #print(i,"row is unique")
            r+=1
    for i in [[i[j] for i in a]for j in range(n)]:
        #print(i,'==',sorted(set(i), key=i.index),'?')
        if i!=sorted(set(i), key=i.index):
            #print(i,"column is unique")
            c+=1
    print(f'Case #{case}:',trace,r,c)
    case+=1        
    t-=1
    
