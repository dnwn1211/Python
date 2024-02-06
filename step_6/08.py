grade_list = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

sum_of_points = 0
count = 0
sumgrade_ =0

for _ in range(20):
    subject, point, grade = input().split()
    if grade == 'P':
        count+=1
    else:
        sum_of_points += float(point) * grade_list[grade]
        sumgrade_+=float(point)
if count ==20:
    print(float(count)/20)
else:
    print(sum_of_points/sumgrade_)
