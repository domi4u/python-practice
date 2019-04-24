'''n = 0
while n < 5:
    print('My dream is being nothing')
    n = n + 1
    print(n)'''
    
'''foods = ['pizza', 'pasta', '떡볶이', '순대']
    
for food in foods:
    print(food)'''
    
numbers = list(range(1, 10))
New_number = []

for number1 in numbers:
    New_number.append(number1)
    print(New_number)
   
    for number2 in numbers:
        number1 = number1 * number2
        New_number.append(number1)
        print(New_number)
    