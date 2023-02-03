import random
import time
correct = 0
for i in range(10):
    tries = 0
    first = random.randint(0,9)
    second = random.randint(0,9)
    start = time.time()
    while tries < 3:
        answer = int(input("{} x {} = ".format(first,second)))
        if answer == first * second:
            end = time.time()
            if end - start > 8:
                print("Time out")
                time.sleep(1)
                break
            print("Correct")
            correct += 1
            time.sleep(1)
            break
        else:
            print("Wrong")
            tries += 1

print("Number of correct answers = ",correct)