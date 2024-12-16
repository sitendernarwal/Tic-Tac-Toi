# Tic Tac Toe Game

Welcome to the Tic Tac Toe game implemented using Python and tkinter! This project provides a simple graphical interface for playing the classic game.

## Features

- Two-player mode (Player X and Player O).
- Restart the game at any time.
- Automatically detects and announces the winner or a tie.
- Highlights the winning combination.

## Installation

1. Make sure you have Python installed on your machine.
2. Install tkinter if it's not already installed. You can do this using pip:
   ```
   pip install python-tk
   ```
3. Clone this repository or download the ZIP file.

## Usage

1. Navigate to the project directory.
2. Run the `tic_tac_toe.py` file to start the game:
   ```
   python tic_tac_toe.py
   ```

## Game Instructions

- Players take turns to mark a tile on the 3x3 grid.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- If all tiles are filled without a winner, the game ends in a tie.
- Click the "Restart" button to start a new game.

## Code Overview

- **set_tile(row, column)**: Marks the board with the current player's symbol and switches turns.
- **chekc_winner()**: Checks for a winning combination or a tie.
- **new_game()**: Resets the board for a new game.
- **Game Setup**: Initializes players, colors, and the game board.
- **Window Setup**: Creates the game window and centers it on the screen.

## Dependencies

- Python
- tkinter

## License

This project is licensed under the MIT License.

## Author

- GitHub: [sitendernarwal](https://github.com/sitendernarwal)
