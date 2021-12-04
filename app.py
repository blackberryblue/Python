#-*- coding:utf-8 -*-

name = 'Tim'

print('Hi. \nHow are you')
print('Hi. \' How areyou')


print(name.upper())
print(name.lower())

# 전부 lower이어야만 true값이 나온다. 
print(name.lower().islower())

# 스트링 길이 확인
print(len(name))