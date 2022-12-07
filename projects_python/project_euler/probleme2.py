'''
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''
sum = 0
list_numbers = []
for i in [x for x in range(10) if x != 0]:
    list_numbers.append(i)
    

for i in range(10):
    print(list_numbers[0])
    sum = sum + (list_numbers[0] + list_numbers[1])
    print(sum)



        
        