def quick(x,first,last):
    if first < last:
        pivot = first
        i = first
        j = last
        while i < j:
            while x[i] <= x[pivot] and i < last:
                i  += 1
            while x[j] > x[pivot]:
                j -= 1
            if i < j:
                x[i],x[j] = x[j],x[i]
        x[pivot],x[j] = x[j],x[pivot]
        quick(x,first,j-1)
        quick(x,j+1,last)
        
a = list(map(int,input().split()))
quick(a,0,len(a)-1)
print (a)
    
