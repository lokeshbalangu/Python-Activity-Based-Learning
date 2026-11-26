total = int(input())
attended = int(input())
required = 75

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100

print("Current attendance:", round(percentage, 2), "%")

needed = 0

while percentage < required:
    total += 1
    attended += 1
    needed += 1
    percentage = attended / total * 100

if needed == 0:
    print("You are already eligible.")
else:
    print("Attend the next", needed, "classes continuously.")
    print("Attendance after recovery:", round(percentage, 2), "%")