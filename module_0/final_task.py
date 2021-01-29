import numpy as np


def mean(min, max):
	return round(min + (max - min) / 2)


def get_count_try(min, max):
	number = np.random.randint(min, max + 1)
	result = mean(min, max)

	counter = 0
	while (result != number):
		counter += 1
		
		if (max - min == 1):
			if (number > result):
				result = max
			else:
				result = min
			break

		if (number > result):
			min = result
		else:
			max = result

		result = mean(min, max)

	return counter 


def get_statistics(min, max, count_try):
	count_try_total = 0

	for i in range(0, count_try):
		count_try_total += get_count_try(min, max)

	return round(count_try_total / count_try)


stat = get_statistics(1, 100, 1000)
print(f"Ваш алгоритм угадывает число в среднем за {stat} попыток")