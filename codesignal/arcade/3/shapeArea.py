def shapeArea(n):
    if n == 1:
        return 1
    else:
        return 4 * (n - 1) + shapeArea(n - 1) 

# def shapeArea(n):
#     return n**2 + (n-1)**2
