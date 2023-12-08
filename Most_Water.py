def most_water(h):
    l=0
    r=n-1
    max=0
    while l<r:
        if h[l]<h[r]:
            m=h[l]
        else:
            m=h[r]
        if m*(r-l)>max:
            max=m*(r-l)
        if h[l]<h[r]:
            l=l+1
        else:
            r=r-1
    print(max)
    
    
n=int(input("Number of pillers "))
h=[]
for i in range(n):
    ph=int(input("lengths "))
    h.append(ph)
most_water(h)
