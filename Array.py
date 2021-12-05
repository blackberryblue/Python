countries = list(('United Kingdom', 'Ghan', 'Nigeria', 4))

list1 = [14,35,53,1,5]
list2 = ['banana','apples','mango','oranges']
list3 = ['hanjin', 12, False]
list4 = ['banana','apples','mango','oranges']

list2.extend(list1)
# 추가

print(list2)
print(len(list1))

# banana 만 제거
list4.remove('banana')
print(list4)


print(list4.index('mango'))
# 
list1.sort()
print(list1)


del list2
print(list2)