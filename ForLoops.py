__author__ = 'rob00000'
age = [10, 102, 20, 340]
age_sum = age[0] + age[1] + age[2] + age[3]
print age_sum
average = age_sum / len(age)
print average

print range(len(age))

sum_numbers = 0

for index in range(len(age)):
    sum_numbers = sum_numbers + age[index]

print sum_numbers
average = sum_numbers / len(age)
print average
