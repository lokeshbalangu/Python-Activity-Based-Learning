capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))
passengers = 0

if capacity <= 0 or stops < 0:
    print("Invalid capacity or stop count")
else:
    for stop in range(1, stops + 1):
        print("\nStop", stop)

        boarding = int(input("Passengers boarding: "))
        alighting = int(input("Passengers alighting: "))

        if boarding < 0 or alighting < 0 or alighting > passengers:
            print("Invalid passenger data")
        else:
            passengers = passengers - alighting + boarding

            print("Passengers on bus:", passengers)

            if passengers > capacity:
                print("Warning: Bus capacity exceeded")
            else:
                print("Occupancy is within capacity")

    print("\nFinal passengers:", passengers)