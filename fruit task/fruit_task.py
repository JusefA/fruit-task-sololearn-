c = int(input())
if c % 2 != 0:
    print("input must be even!")

pie = 0
half = c/2
print('there are ' +str(half)+ ' apples')
if half < 3:
    print(0)

while half > 3:

    half -= 3
    pie += 1
    if half < 3:
        print(pie)
        break
    else:
        continue


