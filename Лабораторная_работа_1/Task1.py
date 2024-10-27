numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_position = numbers.index(None)
current_total = sum(filter(lambda x: x is not None, numbers))
average_result = current_total / len(numbers)
numbers[none_position] = average_result

print("Измененный список:", numbers)