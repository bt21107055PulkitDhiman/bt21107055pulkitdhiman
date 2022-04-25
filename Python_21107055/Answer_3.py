seconds = int(input("Enter the total number of seconds: "))

#For minutes, floor division operator is used.
minutes = seconds//60  

#For minute _seconds, Modulus operator is used.
minute_seconds = seconds%60  

print("Entered", seconds,"seconds", "=" , minutes,  "minutes" , minute_seconds,"seconds")
