import tkinter as tk
from tkinter import messagebox, scrolledtext
from models import Inventory, StockReport

class InventoryApp:
    def __init__(self, root):
        self.aid_flow = Inventory()
        self.root = root
        self.root.title("PCRF Aid-Flow Inventory System")
        self.root.geometry("600x550")
        self.root.configure(bg="#2c2c2c")

        # --- Title Label ---
        tk.Label(self.root, text="PCRF Aid-Flow Inventory System",
                 font=("Arial", 16, "bold"), bg="#2c2c2c", fg="white").pack(pady=10)

        # --- Add New Item Section ---
        self.frame_add = tk.LabelFrame(self.root, text="Add New Supply", bg="#2c2c2c",
                                        fg="white", font=("Arial", 11))
        self.frame_add.pack(fill="x", padx=20, pady=5)

        tk.Label(self.frame_add, text="Name:", bg="#2c2c2c", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_add, width=20)
        self.entry_name.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_add, text="Category:", bg="#2c2c2c", fg="white").grid(row=0, column=2, padx=5)
        self.entry_category = tk.Entry(self.frame_add, width=20)
        self.entry_category.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_add, text="Quantity:", bg="#2c2c2c", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantity = tk.Entry(self.frame_add, width=20)
        self.entry_quantity.grid(row=1, column=1, padx=5)

        # Updated Add Item Button for Mac visibility
        tk.Button(self.frame_add, text="Add Item", 
                  highlightbackground="#4caf50", fg="black",
                  command=self.add_item).grid(row=1, column=3, padx=5, pady=5)

        # --- Update Quantity Section ---
        self.frame_update = tk.LabelFrame(self.root, text="Update Stock", bg="#2c2c2c",
                                           fg="white", font=("Arial", 11))
        self.frame_update.pack(fill="x", padx=20, pady=5)

        tk.Label(self.frame_update, text="Item Name:", bg="#2c2c2c", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_update_name = tk.Entry(self.frame_update, width=20)
        self.entry_update_name.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_update, text="Amount (+/-):", bg="#2c2c2c", fg="white").grid(row=0, column=2, padx=5)
        self.entry_update_amount = tk.Entry(self.frame_update, width=20)
        self.entry_update_amount.grid(row=0, column=3, padx=5)

        # Updated Update Button for Mac visibility
        tk.Button(self.frame_update, text="Update", 
                  highlightbackground="#2196f3", fg="black",
                  command=self.update_stock).grid(row=0, column=4, padx=5)

        # --- Stock Report Section ---
        self.frame_report = tk.LabelFrame(self.root, text="Stock Report", bg="#2c2c2c",
                                           fg="white", font=("Arial", 11))
        self.frame_report.pack(fill="both", expand=True, padx=20, pady=5)

        self.report_box = scrolledtext.ScrolledText(self.frame_report, height=8, bg="#1e1e1e",
                                                     fg="#00ff99", font=("Courier", 10))
        self.report_box.pack(fill="both", expand=True, padx=5, pady=5)

        # Updated Generate Report Button for Mac visibility
        tk.Button(self.frame_report, text="Generate Report", 
                  highlightbackground="#ff9800", fg="black",
                  command=self.show_report).pack(pady=5)

    def add_item(self):
        name = self.entry_name.get()
        category = self.entry_category.get()
        try:
            quantity = int(self.entry_quantity.get()) 
            if name and category:
                success = self.aid_flow.add_new_item(name, category, quantity)
                if success:
                    messagebox.showinfo("Success", f"{name} added to inventory!")
                    self.clear_add_entries()
                else:
                    messagebox.showerror("Error", f"{name} already exists!")
            else:
                messagebox.showwarning("Missing Info", "Please fill in all fields.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a number.")

    def update_stock(self):
        name = self.entry_update_name.get()
        try:
            amount = int(self.entry_update_amount.get())
            if name:
                success = self.aid_flow.update_quantity(name, amount)
                if success:
                    messagebox.showinfo("Updated", f"{name} stock updated!")
                    self.entry_update_name.delete(0, tk.END)
                    self.entry_update_amount.delete(0, tk.END)
                else:
                    messagebox.showerror("Not Found", f"{name} not found in inventory.")
            else:
                messagebox.showwarning("Missing Info", "Please enter an item name.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")

    def show_report(self):
        self.report_box.delete(1.0, tk.END)
        current_stock = self.aid_flow.get_all_items()
        if not current_stock:
            self.report_box.insert(tk.END, "No items in inventory yet.\n")
            return
        report_gen = StockReport(current_stock)
        summary = report_gen.generate_summary()
        for line in summary:
            self.report_box.insert(tk.END, line + "\n")

    def clear_add_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)