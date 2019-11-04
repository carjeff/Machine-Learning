#in this program, we will caculate the US letter size. 
#in advance, I know the US letter size is 11*8.5 inches
width = 8.5
length = 11
inchToMillimeter = 25.399999961392
width = width * inchToMillimeter
length = length * inchToMillimeter
print("The US letter's width is : %.2f" %width + " millimeters")
print("The US letter's length is : %.2f" %length + " millimeters")