def triangle(height):
    finalLineHeight = 2 * height - 1
    for n in range (0, finalLineHeight, 2):
        padding = ' ' * ((finalLineHeight - n) // 2)
        print("%s%s" %(padding, "*" * (n + 1)))
