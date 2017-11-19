__author__ = 'Gavin Siver'
print ('Hello World Test Program \n \n')

name = 'Gavin'
greeting = 'Hello'
print ('Hi. I am %s. Who are you?' % name)
name = raw_input('Please enter your name: ')
print(greeting + ' ' + name + '.')

age = raw_input('Please enter your age (numbers only please): ')
print('Your age is %d years. \n' % int(age))

for i in range(1, 12):
    print('No. %2d squared is %4d and cubed is %4d' % (i, i ** 2, i ** 3))

print('Pi is approximately %1.2f' % (22.0 / 7))
