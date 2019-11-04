"""
Calculate the constant PI (π) to 20 decimal places using the mathematical formula below. 
4/1-4/3+4/5-4/7+4/9-4/11.......


(-1)**(n+1)*4/(2*n-1)
"""

PI = 0
for n in range(10000):
    increase = (-1)**(n)*4/(2*(n+1)-1)
    PI += increase
print("%.20lf" %PI) 