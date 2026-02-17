file = open('9_23193.csv')
k = 1

for line in file:
    numbers = [int(x) for x in line.split(';')]
    numbers = sorted(numbers)
    counts = [numbers.count(x) for x in numbers]
    if counts.count(3) == 3 and counts.count(1) == 3:
        povt = [x for x in numbers if numbers.count(x) == 3]
        nepovt = [x for x in numbers if numbers.count(x) == 1]
        sr_nepovt = sum(nepovt) // 3
        if povt[0] > sr_nepovt:
            print(numbers, counts,k)
    k += 1