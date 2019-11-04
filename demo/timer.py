"""
Write a program to prompt a user for two strings, each representing a time in the format “HH:MM” where “HH” is the two-digit hour and the “MM” is the two-digit minutes. 
Parse your string using string indexing to extract these quantities. 
You may assume that the input is always valid. 
With the two times you take in, calculate the difference (in seconds) between them.
"""
Time1 = str(input("please enter a time (HH:MM) : "))
Time2 = str(input("please enter another time (HH:MM) : "))
Hour1 = int(Time1[0:2])
Min1 = int(Time1[3:5])
Hour2 = int(Time2[0:2])
Min2 = int(Time2[3:5])
difference = abs(Hour1*3600+Min1*60-Hour2*3600+Min2*60)
print("the difference between "+ Time1 + " and "+ Time2 + " is %d seconds" %difference)