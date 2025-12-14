
// Define the MakeMove function that takes the board state and the player's color
// and returns the column number (1-7) to play in.
function MakeMove(board: string[][], player: string) -> int {
  // We specify the client here. This allows us to "insert" a specific model 
  // (like CustomGPT5, CustomHaiku, etc.) into the function.
  // You can change 'CustomGPT5' to any other client defined in clients.baml.
  client CustomGPT5

  prompt #"
    You are an expert Connect 4 player.
    You are playing as {{ player }} ('r' for Red, 'y' for Yellow).
    The opponent is the other color.
    'o' represents an empty slot.

    The board is 6 rows (top to bottom) by 7 columns (left to right).
    Columns are numbered 1 to 7.

    Current Board State:
    {{ board }}

    Your goal is to win by connecting 4 tokens of your color horizontally, vertically, or diagonally.
    If you cannot win immediately, block the opponent from winning.
    Otherwise, make a strategic move to build a winning line.

    Think deeply and make a strategic move.
    Ensure the column is not full (a column is full if the top row, index 0, is not 'o').
    {{ctx.output_format}}
  "#
}

// Test case to verify the function works with the inserted model
test TestMakeMove {
  functions [MakeMove]
  args {
    board [
      ["o", "o", "o", "o", "o", "o", "o"],
      ["o", "o", "o", "o", "o", "o", "o"],
      ["o", "o", "o", "o", "o", "o", "o"],
      ["o", "o", "o", "o", "o", "o", "o"],
      ["o", "o", "o", "o", "o", "o", "o"],
      ["o", "o", "o", "o", "o", "o", "o"]
    ]
    player "r"
  }
}
