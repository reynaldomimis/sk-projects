num_weeks = int(input("Enter number of weeks: "))

for week_number in range(1, num_weeks + 1):
    print(f"Week #{week_number}")
  
    for day_number in range(1, 8):
        print(f"  Day {day_number}")
    print()
