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
        n=int(input("Enter Number :\n"))
        x=collatz(n)
        while True:
            if x!=1:
                x=collatz(x)
            else:
                break
        break
    except ValueError:
        print("Enter an integer")
        continue