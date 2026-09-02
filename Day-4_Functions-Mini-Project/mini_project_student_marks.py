def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = calculate_grade(average)

print("\n----- Student Result -----")
print("Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)