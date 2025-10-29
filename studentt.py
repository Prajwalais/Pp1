# Student Grade Evaluation Program

# Accept marks of a student
marks = int(input("Enter marks: "))

# Determine grade
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)


print(f"Average Marks: {average:.0f}")
print(f"Grade: {grade}")