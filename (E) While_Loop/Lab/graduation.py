student_name = input()
student_class = 1
failed_class = 0
grades_sum = 0
while True:
    grade = float(input())
    if grade < 4:
        failed_class += 1
        if failed_class > 1:
            print(f"{student_name} has been "
                  f"excluded at {student_class} grade")
            break
        continue
    student_class += 1
    grades_sum += grade
    if student_class > 12:
        average_grades = grades_sum / 12
        print(f"{student_name} graduated."
              f" Average grade: {average_grades:.2f}")
        break
