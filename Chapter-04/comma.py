def comma(l):
    out=''
    n=len(l)
    for i in range(0,n-1):
        out += l[i] + ', '
    out += 'and ' + l[-1]
    return out

l=[] 
n=int(input("Length of list : "))
if n==0:
    print("Empty List")
else:
    for i in range(0,n):
        a=input()
        l.append(a)
    print(comma(l))