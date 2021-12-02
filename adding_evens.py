total = 0
''' You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
'''
# to count from 1 to 100, use range(1, 100), step 2 would be range(1, 100, 2)
for count in range(1, 101):
    if (count % 2) == 0:
        print(count)
        total += count
print(f"Total of even number from 1 to 100 is {total}")
