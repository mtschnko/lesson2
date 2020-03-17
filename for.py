#задание1
school_grade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(school_grade)

grade = 0
for grade in school_grade:
		print(grade+1)

#задание2
line = input('Введите строку: ')
for word in list(line):
    print(word)

#задание3
school_scores = [
    {'school_class': '5a', 'scores': [4, 4, 5]},
    {'school_class': '5b', 'scores': [2, 3, 4]},
    {'school_class': '5c', 'scores': [3, 3, 2]},
				]
def _sum(arr, n):
    return(sum(arr))
school_avg = []
for score in school_scores:
    for num in score['scores']:
        school_avg.append(num)
    n = len(score['scores'])
    print(f"Средний балл класса {score['school_class']}: {int((_sum(score['scores'], n)) / n)}")

n = len(school_avg)
summ = _sum(school_avg, n)
schoolavg = summ / n

print(f"Средний балл по всей школе: {int(schoolavg)}")