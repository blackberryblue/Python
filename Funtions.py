def greetings_function(name):
    print('Welcome ' + name)


def greetings_function2(name,age):
    print('Welcome ' + str(name) + '. You are ' +str(age)+ ' years old.')

def greetings_function3(*names):
    print('Welcome ' + names[0])

greetings_function('John')
greetings_function2('John',27)
greetings_function3('John','Jin','jung')
greetings_function2(name = 'jin', age=33)

name  = input('Enter your name :')
age = input('Enter your age')
greetings_function2(name,age)