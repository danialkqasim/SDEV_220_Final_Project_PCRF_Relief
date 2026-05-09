import tkinter as tk
from gui import InventoryApp

def main():
    # Initialize Tkinter root (main window)
    root = tk.Tk()
    
    # Pass root to the InventoryApp class - about to update in gui.py
    app = InventoryApp(root)
    
    # Start application loop
    root.mainloop()

if __name__ == "__main__":
    main()