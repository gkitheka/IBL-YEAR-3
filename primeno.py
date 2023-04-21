p = int(input("starting number"))
k = int(input("ending number"))
for num in range(p, k+1):
    if num > 1:
        for i in range(2, num):
            if num% i == 0:
              break
        else:
            print(num)



            