my = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def RotateImage(a):
    """
    You are given an n x n 2D matrix that represents an image. 
    Rotate the image by 90 degrees (clockwise).
    
    For

    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    the output should be

    rotateImage(a) =
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    """
    result = []
    for x in range(len(a)):
        result.append([])
    a.reverse()

    for i in range(len(a)):
        for x in a:
            result[i].append(x[i])            
               
    return result

# def rotateImage(a):
#     return list(zip(*reversed(a)))

# def rotateImage(a):
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(i):
#             a[i][j], a[j][i] = a[j][i], a[i][j]
#     return a
