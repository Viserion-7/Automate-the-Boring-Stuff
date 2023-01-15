import sys
def collatz(number):
    if number%2==0:
        a=number//2
    elif number==1:
        a=1
    else:
        a=3*number+1
    print(a)
    return a
while True:
    try:
        n=int(input())
        x=collatz(n)
        while True:
            if x!=1:
                x=collatz(x)
            else:
                break
        break
    except ValueError:
        continue
