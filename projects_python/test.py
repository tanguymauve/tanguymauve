'''
for number in range(len(numbers)):
    print(len(numbers))
    sum = sum + number

print(sum)
#for i in range(numbers)


X = int(input())
N = int(input())

for i in range(N):
    sum = X*i
    print(sum)
  '''
numbers=[]
sum = 0

for i in range(1001):
    if i%2!=0:
        numbers.append(i)

def getMultiples(num, number_of_multiples):
	i = 1
	while i <= number_of_multiples:
		print(num*i)
		i += 1