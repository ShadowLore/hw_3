homework_list = ['Пропылесосить', 'Помыть полы', 'Погладить белье', 'Приготовить ужин', 'Повесить полку', 'Отдохнуть', 'Помочь с уроками']
#                      0                 1                 2                 3                   4              5             6

print(homework_list[2])

print(homework_list[len(homework_list) - 1])
print(homework_list[-1])

print(homework_list[-4])
print(homework_list[len(homework_list) - 4])

homework_list.append('Почистить обувь')
print(homework_list)

homework_list.insert(6, 'Поиграть с котом')
print(homework_list)

last_work = homework_list.pop()
print(last_work)
print(homework_list)

print(homework_list.count('Отдохнуть'))

print(homework_list.index('Отдохнуть'))
