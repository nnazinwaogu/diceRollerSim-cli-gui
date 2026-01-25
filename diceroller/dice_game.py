import random
import sys
from typing import List

# Check for GUI launch flag
if len(sys.argv) > 1 and sys.argv[1] == "--gui":
    try:
        from dice_gui import main as gui_main
        gui_main()
        sys.exit(0)
    except ImportError as e:
        print(f"GUI not available: {e}")
        sys.exit(1)

def roll_die(sides: int = 6) -> int:
    """Return a random integer from 1 to sides inclusive."""
    if sides < 1:
        raise ValueError("sides must be >= 1")
    return random.randint(1, sides)

def roll_dice(num_dice: int, sides: int = 6) -> List[int]:
    """Roll num_dice dice with the given number of sides and return the results."""
    if num_dice < 1:
        raise ValueError("num_dice must be >= 1")
    return [roll_die(sides) for _ in range(num_dice)]

def _format_roll(results: List[int]) -> str:
    """Format the roll results for printing."""
    if len(results) == 1:
        return f"You rolled: {results[0]}"
    elif len(results) == 2:
        x, y = results
        return f"You rolled: {x} and {y} (total: {x + y})"
    else:
        total = sum(results)
        return f"You rolled: " + ", ".join(map(str, results)) + f" (total: {total})"

def print_banner():
    banner = r"""
===========================================
  Dice Roller CLI - Python Edition
===========================================
"""
    print(banner)

def run_tests():
    print("Running tests...")
    try:
        test_roll_die()
        test_roll_dice()
        test_exceptions()
        print("All tests passed.")
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Test error: {e}")
        sys.exit(1)

def test_roll_die():
    for sides in (1, 4, 6, 20):
        for _ in range(50):
            v = roll_die(sides)
            assert 1 <= v <= sides, f"roll_die out of bounds: {v} for sides {sides}"
    # boundary condition
    try:
        roll_die(0)
        assert False, "Expected ValueError for sides=0"
    except ValueError:
        pass

def test_roll_dice():
    r1 = roll_dice(1, 6)
    assert len(r1) == 1 and 1 <= r1[0] <= 6
    r2 = roll_dice(2, 6)
    assert len(r2) == 2 and all(1 <= v <= 6 for v in r2)
    # multiple dice with different sides
    r3 = roll_dice(3, 8)
    assert len(r3) == 3 and all(1 <= v <= 8 for v in r3)

def test_exceptions():
    try:
        roll_dice(0)
        assert False, "Expected ValueError for num_dice=0"
    except ValueError:
        pass
    try:
        roll_dice(-1)
        assert False, "Expected ValueError for num_dice=-1"
    except ValueError:
        pass
    try:
        roll_die(0)
        assert False, "Expected ValueError for sides=0"
    except ValueError:
        pass

def main_loop():
    print_banner()
    print("Welcome to the Dice Roller!")
    sides = 6  # fixed for this simple game
    num_dice = None
    while True:
        user = input("Choose number of dice to roll (1 or 2) or q to quit: ").strip().lower()
        if user == 'q':
            print("Goodbye!")
            break
        if user not in ('1', '2'):
            print("Invalid input. Please enter 1, 2, or q to quit.")
            continue
        num_dice = int(user)
        results = roll_dice(num_dice, sides)
        print(_format_roll(results))
        # post-roll prompt
        while True:
            cont = input("Roll again with the same number of dice? (Enter to roll again, 'c' to change dice, 'q' to quit): ").strip().lower()
            if cont == 'q':
                print("Goodbye!")
                return
            if cont == 'c':
                break  # outer loop to change dice
            # any other input (including empty) continues rolling with same dice
            results = roll_dice(num_dice, sides)
            print(_format_roll(results))
            # loop again to continue rolling with same dice

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    main_loop()

if __name__ == "__main__":
    main()
