# Exercise 2: Check time against 10 minutes (600 seconds)

time_in_seconds=int(input("Enter time in seconds: "))
limit=600  #10 minutes in seconds

if time_in_seconds < limit:
    remaining=limit-time_in_seconds
    print("The time is less than 10 minutes")
    print("Remaining",remaining,"seconds to reach 10 minutes")
    print("Result: Less")
elif time_in_seconds>limit:
    print( "The time is More than 10 minutes")
    print("result: More")
else:
    print("The time is equal to 10 minutes")
    print("Result: Equal")



