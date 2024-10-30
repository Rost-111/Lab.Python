# TODO Напишите функцию find_common_participants
def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list:
    if group1:
        participants1 = set(group1.split(delimiter))
    else:
        participants1 = set()
    if group2:
        participants2 = set(group2.split(delimiter))
    else:
        participants2 = set()
    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)


participants_first_group_c = "Иванов,Петров,Сидоров"
participants_second_group_c = "Петров,Сидоров,Смирнов"

common_participants_c = find_common_participants(participants_first_group_c, participants_second_group_c)
print("Общие участники (разделитель ','):", common_participants_c)

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники (разделитель '|'):", common_participants)
