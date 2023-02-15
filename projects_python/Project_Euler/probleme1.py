numbers=[]
sum = 0

for i in range(1000):
    if i%3==0 or i%5 == 0 :
        numbers.append(i)

for number in numbers:
    sum = sum + number

print(sum)
#solution = 233168

