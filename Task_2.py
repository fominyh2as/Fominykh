def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Пример использования функции
group1 = "Иванов, Петров, Сидоров"
group2 = "Петров, Сидоров, Смирнов"

common_participants = find_common_participants(group1, group2)
print(common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
