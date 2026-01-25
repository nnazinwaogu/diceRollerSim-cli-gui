"""
Author: Nnazirim Nwaogu, Big Pickle (OpenZen)

"""

# Imports
import tkinter as tk
from tkinter import ttk, scrolledtext, font
import random
from typing import List

# Import dice functions to avoid circular import
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

# GUI Application
class DiceRollerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.num_dice = tk.IntVar(value=1)
        
        # Setup UI
        self.setup_ui()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        # Title
        title_font = font.Font(family="Arial", size=16, weight="bold")
        title_label = ttk.Label(self.root, text="Dice Roller", font=title_font)
        title_label.pack(pady=10)
        
        # Dice selection frame
        selection_frame = ttk.Frame(self.root)
        selection_frame.pack(pady=10)
        
        ttk.Label(selection_frame, text="Select dice count:").pack()
        
        # Radio buttons
        radio_frame = ttk.Frame(selection_frame)
        radio_frame.pack(pady=5)
        
        ttk.Radiobutton(radio_frame, text="1 die", variable=self.num_dice, 
                       value=1).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(radio_frame, text="2 dice", variable=self.num_dice, 
                       value=2).pack(side=tk.LEFT, padx=10)
        
        # Result display
        result_frame = ttk.Frame(self.root)
        result_frame.pack(pady=20, padx=20, fill=tk.X)
        
        result_font = font.Font(family="Arial", size=14)
        self.result_label = ttk.Label(result_frame, text="Click 'Roll' to start!", 
                                     font=result_font, foreground="blue")
        self.result_label.pack()
        
        # Buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.roll_button = ttk.Button(button_frame, text="Roll", 
                                     command=self.roll_dice, width=15)
        self.roll_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = ttk.Button(button_frame, text="Quit", 
                                     command=self.quit_app, width=15)
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        # History section
        history_frame = ttk.Frame(self.root)
        history_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        ttk.Label(history_frame, text="Roll History:").pack(anchor=tk.W)
        
        # Scrollable text widget for history
        self.history_text = scrolledtext.ScrolledText(history_frame, 
                                                     height=8, width=45,
                                                     wrap=tk.WORD,
                                                     state=tk.DISABLED)
        self.history_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Configure text tags for better formatting
        self.history_text.tag_config("roll", foreground="black")
    
    def roll_dice(self):
        """Handle roll button click."""
        try:
            # Get number of dice from radio selection
            num = self.num_dice.get()
            
            # Roll the dice using backend function
            results = roll_dice(num, 6)
            
            # Format result using backend function
            result_text = _format_roll(results)
            
            # Update result label
            self.result_label.config(text=result_text, foreground="black")
            
            # Print to console
            print(result_text)
            
            # Add to history
            self.add_to_history(result_text)
            
        except Exception as e:
            error_text = f"Error: {e}"
            self.result_label.config(text=error_text, foreground="red")
            print(error_text)
    
    def add_to_history(self, text):
        """Add roll result to history."""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, text + "\n", "roll")
        self.history_text.see(tk.END)  # Auto-scroll to bottom
        self.history_text.config(state=tk.DISABLED)
    
    def quit_app(self):
        """Handle quit button click."""
        print("Goodbye!")
        self.root.quit()
        self.root.destroy()
    
    def on_closing(self):
        """Handle window close (X button)."""
        self.quit_app()

# Main Function
def main():
    """Main function to launch the GUI."""
    root = tk.Tk()
    app = DiceRollerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()