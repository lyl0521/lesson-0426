fruits = ['apple','pear','lemon','watermelon']

for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        print('found')
        break
else:
    print('not found')