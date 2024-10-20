numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_left = numbers[:4]
numbers_right = numbers[5:]
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = numbers_left + numbers_right
sum_of_numbers = sum(numbers_without_none)
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
numbers[4] = average_of_numbers
print("Измененный список:", numbers)
