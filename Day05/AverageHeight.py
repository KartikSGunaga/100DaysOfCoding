student_heights = [156, 178, 165, 171, 187]
avg = 0
sum = 0
count = 0

for height in student_heights:
    sum = sum + height
    count = count + 1

avg = round(sum / count)
print(f"""total height = {sum}
number of students = {count}
average height = {avg}""")