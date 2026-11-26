marks = [[80,70],[60,50],[90,85]]

students = len(marks)
subjects = len(marks[0])

print("Student Results")

totals = []

for i in range(students):
    total = sum(marks[i])
    average = total / subjects
    totals.append(total)

    print("Student", i + 1, "Total:", total,
          "Average:", round(average, 2))

print("\nSubject Averages")

for j in range(subjects):
    total = 0

    for i in range(students):
        total += marks[i][j]

    average = total / students

    print("Subject", j + 1, "Average:",
          round(average, 2))

    if average < 40:
        print("Warning: Low average in Subject", j + 1)

top_index = totals.index(max(totals))

print("\nTop performer: Student", top_index + 1)
print("Highest total:", max(totals))