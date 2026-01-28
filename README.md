# Dice Roller

A Python dice roller application with both CLI and GUI interfaces.

## Features

- **CLI Interface**: Interactive command-line dice rolling
- **GUI Interface**: User-friendly Tkinter graphical interface
- **Multiple Dice**: Support for rolling 1 or 2 dice
- **Roll History**: GUI maintains a scrollable history of all rolls
- **Built-in Testing**: Comprehensive test suite included
- **Zero Dependencies**: Uses only Python standard library

## Installation

This project requires Python 3.7 or higher. No additional packages need to be installed - it uses only the Python standard library.

```bash
# Clone or download the repository
cd CLI DiceRoller/diceroller
```

## Usage

### CLI Interface

Start the interactive CLI:

```bash
python dice_game.py
```

The CLI will prompt you to:
1. Choose number of dice (1 or 2)
2. Roll multiple times with the same dice count
3. Change dice count or quit

### GUI Interface

Two launch methods are available:

**Method 1: Using the GUI flag**
```bash
python dice_game.py --gui
```

**Method 2: Direct execution**
```bash
python dice_gui.py
```

The GUI features:
- Radio buttons to select 1 or 2 dice
- Roll button to generate random dice rolls
- Large result display showing individual dice and totals
- Scrollable history showing all previous rolls
- Quit button to exit the application

### Running Tests

Run the built-in test suite:

```bash
python dice_game.py test
```

The application will exit with code 1 if any tests fail.

## Project Structure

```
CLI DiceRoller/
├── diceroller/           # Main application directory
│   ├── dice_game.py      # CLI interface and core logic
│   ├── dice_gui.py       # Tkinter GUI interface
│   └── __pycache__/      # Python bytecode cache
├── AGENTS.md             # Development guidelines for agents
└── README.md             # This file
```

## Development

### Code Style

This project follows specific conventions such as:

- Type hints for all function parameters and return values
- Consistent `snake_case` naming conventions
- Simple triple-quoted docstrings
- Input validation with descriptive error messages

### Testing

The project uses custom test functions rather than a testing framework. To run individual tests, modify the `run_tests()` function in `dice_game.py` to call specific test functions:
- `test_roll_die()` - Tests single die rolling
- `test_roll_dice()` - Tests multiple dice rolling  
- `test_exceptions()` - Tests error conditions

### Contributing

When contributing to this project:
1. Follow existing code patterns and conventions
2. Add corresponding test functions for new functionality
3. Update the `run_tests()` function to include new tests
4. Maintain backward compatibility with existing interfaces

## License

This project is open source and available under the MIT License.

## Version

1.0.0 - Initial release with CLI and GUI interfaces
