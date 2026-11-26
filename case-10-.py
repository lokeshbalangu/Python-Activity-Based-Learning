days = int(input("Enter number of days: "))
limit = 10

prepared_total = 0
served_total = 0
leftover_total = 0

for day in range(1, days + 1):
    print("\nDay", day)

    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))
    leftover = int(input("Leftover meals: "))

    if prepared <= 0 or served < 0 or leftover < 0 or served + leftover > prepared:
        print("Invalid meal details")
    else:
        waste = leftover / prepared * 100

        prepared_total += prepared
        served_total += served
        leftover_total += leftover

        print("Food waste:", round(waste, 2), "%")

        if waste > limit:
            print("Warning: Waste exceeds 10%")
        else:
            print("Waste is within the acceptable limit")

print("\nOverall Summary")
print("Total prepared:", prepared_total)
print("Total served:", served_total)
print("Total leftovers:", leftover_total)

if prepared_total > 0:
    overall_waste = leftover_total / prepared_total * 100
    print("Overall waste percentage:", round(overall_waste, 2), "%")