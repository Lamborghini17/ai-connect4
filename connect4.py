the_board=[
[ "o","o","o","o","o","o","o"],
[ "o","o","o","o","o","o","o"],
[ "o","o","o","o","o","o","o"],
[ "o","o","o","o","o","o","o"],
[ "o","o","o","o","o","o","o"],
[ "o","o","o","o","o","o","o"]
]

def playerMove(board, color):
  move = int(input("What column do you want to put your token in: "))
  if move < 1 or move > 7:
    print("Your move in invalid, please enter a different value")
    move = int(input("What column do you want to put your token in: "))
  for row in range(6):
    if board[5-row][move-1] == 'o':
      board[5-row][move-1] = str(color)
      return board

def show_board(board):
  for row in board:
    print(row)

def determine_winner(board):

  #Check horizontals
  for a in range(len(board)):
    for i in range(4):
      if board[a][i] == board [a][i+1] == board[a][i+2] == board[a][i+3] != 'o':
        return board[a][i]

  #Check columns
  for k in range(7):
    for j in range(3):
      if board[j][k] == board[j+1][k] == board [j+2][k] == board[j+3][k] != 'o':
        return board[j][k]

  #Check Diagonals (starting from top left)
  for column in range(4):
    for row in range(3):
      if board[row][column] == board[row+1][column+1] == board [row+2][column+2] == board[row+3][column+3] != 'o':
        return board[row][column]

  #Check Diagonals (starting from top right)
  for row in range(3):
    for column in range(3,7):
      if board[row][column] == board[row+1][column-1] == board[row+2][column-2] == board [row+3][column-3] != 'o':
        return board[row][column]
  return False

show_board(the_board)
for i in range(21):
  the_board = playerMove(the_board, 'r')
  print(the_board)
  show_board(the_board)
  determine_winner(the_board)
  if determine_winner:
    print("Red won!!!!")
    break
  the_board = playerMove(the_board, 'y')
  show_board(the_board)
  determine_winner(the_board)
  if determine_winner:
    print("yellow won!!!!")
    break

if not determine_winner(the_board):
  print("There has been a draw")