# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(group1, group2, separator=','):

    participants_group1 = group1.split(separator)
    participants_group2 = group2.split(separator)


    common_participants = list(set(participants_group1).intersection(participants_group2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
separator = '|'

common_participants = find_common_participants(participants_first_group, participants_second_group, separator)
print(f'Общие участники: {common_participants}')
