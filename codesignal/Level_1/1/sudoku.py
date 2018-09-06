# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that 
# each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers 
# from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according 
# to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

# For

# grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# the output should be
# sudoku2(grid) = true;

# For

# grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
# the output should be
# sudoku2(grid) = false.

# def sudoku2(grid):
#     def unique(G):
#         G = [x for x in G if x != '.']
#         return len(set(G)) == len(G)
#     def groups(A):
#         B = zip(*A)
#         for v in xrange(9):
#             yield A[v]
#             yield B[v]
#             yield [A[v/3*3 + r][v%3*3 +c] 
#                    for r in xrange(3) for c in xrange(3)]
    
#     return all(unique(grp) for grp in groups(grid))

# def check_unique(nums):
#     s = set()
#     for num in nums:
#         if num == '.':
#             continue 
            
#         if num in s:
#             return False
#         s.add(num)
#     return True
        

# def sudoku2(grid):
#     for line in grid:
#         if not check_unique(line):
#             return False
    
#     for i in range(9):
#         if not check_unique([line[i] for line in grid]):
#             return False
        
#     for i in range(0,9,3):
#         for j in range(0, 9, 3):
#             if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
#                 return False
            
#     return True


# //Basic idea: This is a stupid problem that anyone can do.
# //  If I were given this in an interview, I'd reconsider the company.



# //Turn columns into rows
# var transpose = grid =>
#     grid[0].map(
#         (_,c) => grid.map(
#             row => row[c]
#         )
#     )

# //Turn sub-grids into rows
# var expandSubGrids = grid => {
#     var three = Math.sqrt(grid.length);
#     return grid[0].map(
#         (_,i) => grid[0].map(
#             (_,j) => grid[(i/three|0)*three+j/three|0][i%three*three+j%three]
#         )
#     )
# }

# //Check a given row for duplicates
# var checkRow = row => {
#     var count = [];
#     for(var cell of row) {
#         if(cell != '.') {
#             if(count[cell])
#                 return false;
#             count[cell] = 1;
#         }
#     }
#     return true;
# }

# var sudoku2 = grid =>
#     grid.every(checkRow) &&
#     transpose(grid).every(checkRow) &&
#     expandSubGrids(grid).every(checkRow)
