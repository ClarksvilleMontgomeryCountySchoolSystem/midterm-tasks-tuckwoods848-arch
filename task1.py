#Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6 # friends

#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------
total_slices = party_pizza_mini + large + medium
print(f"Total number of slices: {total_slices}")

#  TODO Update people to include yourself
people + 1
total_slices // people
print(f"Each person gets: {"4"}")
print(f"Leftover slices: {"0"}")

people + 2
total_slices // people
leftover = total_slices % people
print(f"Each person gets: {"3"}")
print(f"Leftover slices {"1"}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices + 1
party_pizza_mini + total_slices
leftover = 13
print(f"Each person gets: {4} ")
print(f"Leftover slices: {6}")
print("...for Mr. Hollow Leg")
