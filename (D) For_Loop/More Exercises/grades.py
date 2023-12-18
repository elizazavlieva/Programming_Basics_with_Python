# Read input

num_of_students = int(input())
average_rating = 0
fail_grade = 0
low_grade = 0
average_grade = 0
excellent_grade = 0
for i in range( 1, num_of_students + 1):
    student_grade = float(input())
    if 2.00 <= student_grade <= 2.99:
        fail_grade += 1
        average_rating +=student_grade
    elif 3.00 <= student_grade <= 3.99:
        low_grade += 1
        average_rating += student_grade
    elif 4.00 <= student_grade <= 4.99:
        average_grade += 1
        average_rating += student_grade
    elif student_grade >= 5.00:
        excellent_grade +=1
        average_rating += student_grade

average_rating /= num_of_students
fail_grade_percent = fail_grade / num_of_students * 100
low_grade_percent = low_grade / num_of_students * 100
average_grade_percent = average_grade / num_of_students * 100
excellent_grade_percent = excellent_grade / num_of_students * 100

# Print output

print(f'Top students: {excellent_grade_percent:.2f}%')
print(f'Between 4.00 and 4.99: {average_grade_percent:.2f}%')
print(f'Between 3.00 and 3.99: {low_grade_percent:.2f}%')
print(f'Fail: {fail_grade_percent:.2f}%')
print(f'Average: {average_rating:.2f}')