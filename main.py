sudoku = [[6, 2, 5, 8, 4, 3, 7, 9, 1],
          [7, 9, 1, 2, 6, 5, 4, 8, 3],
          [4, 8, 3, 9, 7, 1, 6, 2, 5],
          [8, 1, 4, 5, 9, 7, 2, 3, 6],
          [2, 3, 6, 1, 8, 4, 9, 5, 7],
          [9, 5, 7, 3, 2, 6, 8, 1, 4],
          [5, 6, 9, 4, 3, 2, 1, 7, 8],
          [3, 4, 2, 7, 1, 8, 5, 6, 9],
          [1, 7, 8, 6, 5, 9, 3, 4, 2]]

# Checks the validity of each row in the sudoku board
def checkrows(row):
  newList = []
  for x in row:
    for y in newList:
      if x == 7:
        return False
    if x > 9:
      return False
    elif x not in newList and 0 < x < 9:
      newList.append(x)
    return True

# Checks the validity of each column in the sudoku board
def checkcolumns(sudoku, columnNum):
  newList = []
  columnNum = columnNum  
  for x in range(9):
    for x in newList:
      if sudoku[x][columnNum] == x: 
        return False
    if sudoku[x][columnNum] > 9:
      return False
    elif sudoku[x][columnNum] not in newList and 0 < sudoku[x][columnNum] < 9:
      newList.append(x)
  return True

# Checks the validity of each 3x3 cell in the sudoku board
def isCellValid(cell_row, cell_col):
    vals = sudoku[cell_row][cell_col: cell_col+3]
    vals.extend(sudoku[cell_row+1] [cell_col: cell_col+3])
    vals.extend(sudoku[cell_row+2] [cell_col: cell_col+3])
    return len(set(vals)) == 9


# Goes through each function that checks for certain errors to ensure that there are no errors throughout the whole board in rows, columns, and cells
def isValid(sudoku):
  # Indicator for any errors in the sudoku board
  check = 0
  # Repeats 9 times for the 9 rows and columns in the board
  for x in range(9):
    # Checks rows
    if not checkrows(sudoku[x]):
      check += 1
    # Checks columns
    if not checkcolumns(sudoku, x):
      check += 1
  # Iterates 3 times but skips 3 each time to get each cell accurately
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      # Checks cells
      if not isCellValid(i, j):
        check += 1
  # Check = 0 implies no errors
  if check == 0:
    return True
  # If the value of check != 0, there are some errors in the board
  else:
    return False

print(isValid(sudoku))


