# Sudoku Solver and Player with GUI

Welcome to the Sudoku Solver and Player project! This repository contains a simple GUI-based Sudoku game where users can either play by filling in the board and receiving feedback on their answers or use an automatic solver to complete the board instantly. The solver uses backtracking and recursion to efficiently find a solution.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [GUI Example](#GUI-example)
- [Future Directions](#future-directions)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive Sudoku Board**: Users can fill in each cell to solve the board on their own.
- **Instant Feedback**: The application provides feedback if the user's input is correct for each cell.
- **Solver Functionality**: For those looking to skip the challenge, the `Solver.py` script can solve the entire board instantly.

## How It Works

1. **Interactive Gameplay**:
   - The GUI (`GUI.py`) provides a playable Sudoku board where the user can enter numbers into each cell.
   - As users input values, the program will check if the entry is correct for that specific cell.
   - Incorrect entries prompt immediate feedback, allowing users to adjust their answers as they go.

2. **Automated Solver**:
   - If a user prefers not to play manually, the `Solver.py` script is available to complete the board instantly.
   - This solver utilizes backtracking and recursion to fill the board, ensuring a solution is provided if one exists.
   - After solving, the GUI will display the completed board for the user.

## Getting Started

To get a local copy of this project up and running, follow these simple steps.

## Dependencies

The project relies on the following library:

- **pygame**: `pygame` is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries to create engaging applications, making it ideal for creating interactive GUIs like the Sudoku game interface. For more information, refer to the [official `pygame` documentation](https://www.pygame.org/docs/).

### Installation

1. Download all project files into a single folder on your computer: `GUI.py` `solver.py`.

2. Install dependencies (pygame):
```bash
  pip install pygame 
  ```

## Usage

Run the `GUI.py` file to start the Sudoku game interface:
`python GUI.py`

- **Playing Manually**: Enter values into each cell to solve the board. If an entry is incorrect, you will be alerted.
- **Using the Solver**: If you want the board solved automatically, use the solver function in the GUI or run `Solver.py` directly:
  `python solver.py`
  
This will output a completed board if a solution exists, displaying it in the GUI for easy viewing.


## GUI Example
<img src="https://github.com/user-attachments/assets/eef21af7-e350-44bd-b367-f16f052f1d09" width="300" alt="image">


## Future Directions

- **Random Board Generation**: The board will be automatically randomized, allowing for a new challenge each time the program is launched.
  
AND/OR
- **User-Generated Board**: The GUI will be updated so that users can input their own custom board, which the program will verify and solve if desired.

## Contributing

Contributions are welcome! If you'd like to add a feature, fix a bug, or make improvements, please fork the repository and submit a pull request.


