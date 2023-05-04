import random

numbers = [random.randint(0, 9) for i in range(0, 1000)]

count_dict = {}
for n in numbers:
	if n in count_dict:
		count_dict[n] += 1
	else:
		count_dict[n] = 1

greater_90 = [n for n in count_dict.keys() if count_dict[n] > 90]
print("Numbers created more than 90 times:", greater_90)

max_number = max(count_dict.values())
print("Most common number generated", max_number, "times")
