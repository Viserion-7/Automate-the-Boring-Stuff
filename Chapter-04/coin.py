import random
numberOfStreaks = 0
c=0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    l=[]
    i=0
    while i<100:
        if random.randint(0,1):
            l.append('H')
        else:
            l.append('T')
        i += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
    i=0
    c=0
    while i<95:
        if  l[i]==l[i+1]==l[i+2]==l[i+3]==l[i+4]==l[i+5]:
            numberOfStreaks+=1
            c+=1
            i+=5
        i+=1
print("Total no of streaks in 10000 experiments of 100 coinflip each",numberOfStreaks)
print('Chance of streaks in 10000 experiments of 100 coinflip each: %s%%' % (numberOfStreaks / 10000))