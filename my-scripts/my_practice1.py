from functools import reduce

employees_numbers = [100, 117, 126, 133, 135, 136]
employees_numbers.reverse()

increase_numbers = [num - employees_numbers[idx + 1] if idx + 1 < len(employees_numbers) else 0
                    for idx, num in enumerate(employees_numbers)]
increase_numbers.reverse()
print(increase_numbers)
