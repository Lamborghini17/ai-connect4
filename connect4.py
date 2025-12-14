from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from baml_client import b

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

def aiMove(board, color):
  print("AI is thinking...")
  try:
    # Call the BAML MakeMove function
    move = b.MakeMove(board=board, player=color)
    print(f"AI chose column {move}")
    
    # Validate the move
    if move < 1 or move > 7:
      print(f"AI made an invalid move ({move}), choosing column 4 as fallback")
      move = 4
    
    # Check if column is full
    if board[0][move-1] != 'o':
      print(f"AI chose a full column ({move}), choosing first available column")
      for col in range(7):
        if board[0][col] == 'o':
          move = col + 1
          break
    
    # Place the token
    for row in range(6):
      if board[5-row][move-1] == 'o':
        board[5-row][move-1] = str(color)
        return board
  except Exception as e:
    print(f"AI error: {e}")
    print("AI will make a random valid move")
    # Fallback: find first available column
    for col in range(7):
      if board[0][col] == 'o':
        for row in range(6):
          if board[5-row][col] == 'o':
            board[5-row][col] = str(color)
            return board
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

print("Welcome to Connect 4! You are Red ('r'), AI is Yellow ('y')")
show_board(the_board)
for i in range(21):
  # Human player's turn (Red)
  the_board = playerMove(the_board, 'r')
  print(the_board)
  show_board(the_board)
  if determine_winner(the_board):
    print("Red won!!!!")
    break
  
  # AI player's turn (Yellow)
  the_board = aiMove(the_board, 'y')
  show_board(the_board)
  if determine_winner(the_board):
    print("Yellow won!!!!")
    break

if not determine_winner(the_board):
  print("There has been a draw")