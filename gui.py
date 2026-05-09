import tkinter as tk
from tkinter import messagebox, scrolledtext
from models import Inventory, StockReport

# Initialize inventory
aid_flow = Inventory()

# --- Main Window Setup ---
root = tk.Tk()
root.title("PCRF Aid-Flow Inventory System")
root.geometry("600x500")
root.configure(bg="#2c2c2c")

# --- Title Label ---
title = tk.Label(root, text="PCRF Aid-Flow Inventory System",
                 font=("Arial", 16, "bold"), bg="#2c2c2c", fg="white")
title.pack(pady=10)

# --- Add New Item Section ---
frame_add = tk.LabelFrame(root, text="Add New Supply", bg="#2c2c2c",
                           fg="white", font=("Arial", 11))
frame_add.pack(fill="x", padx=20, pady=5)

tk.Label(frame_add, text="Name:", bg="#2c2c2c", fg="white").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_add, width=20)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame_add, text="Category:", bg="#2c2c2c", fg="white").grid(row=0, column=2, padx=5)
entry_category = tk.Entry(frame_add, width=20)
entry_category.grid(row=0, column=3, padx=5)

tk.Label(frame_add, text="Quantity:", bg="#2c2c2c", fg="white").grid(row=1, column=0, padx=5, pady=5)
entry_quantity = tk.Entry(frame_add, width=20)
entry_quantity.grid(row=1, column=1, padx=5)

def add_item():
    name = entry_name.get()
    category = entry_category.get()
    quantity = entry_quantity.get()
    if name and category and quantity:
        success = aid_flow.add_new_item(name, category, quantity)
        if success:
            messagebox.showinfo("Success", f"{name} added to inventory!")
            entry_name.delete(0, tk.END)
            entry_category.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"{name} already exists!")
    else:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")

tk.Button(frame_add, text="Add Item", bg="#4caf50", fg="white",
          command=add_item).grid(row=1, column=3, padx=5, pady=5)

# --- Update Quantity Section ---
frame_update = tk.LabelFrame(root, text="Update Stock", bg="#2c2c2c",
                              fg="white", font=("Arial", 11))
frame_update.pack(fill="x", padx=20, pady=5)

tk.Label(frame_update, text="Item Name:", bg="#2c2c2c", fg="white").grid(row=0, column=0, padx=5, pady=5)
entry_update_name = tk.Entry(frame_update, width=20)
entry_update_name.grid(row=0, column=1, padx=5)

tk.Label(frame_update, text="Amount (+/-):", bg="#2c2c2c", fg="white").grid(row=0, column=2, padx=5)
entry_update_amount = tk.Entry(frame_update, width=20)
entry_update_amount.grid(row=0, column=3, padx=5)

def update_stock():
    name = entry_update_name.get()
    amount = entry_update_amount.get()
    if name and amount:
        success = aid_flow.update_quantity(name, amount)
        if success:
            messagebox.showinfo("Updated", f"{name} stock updated!")
            entry_update_name.delete(0, tk.END)
            entry_update_amount.delete(0, tk.END)
        else:
            messagebox.showerror("Not Found", f"{name} not found in inventory.")
    else:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")

tk.Button(frame_update, text="Update", bg="#2196f3", fg="white",
          command=update_stock).grid(row=0, column=4, padx=5)

# --- Stock Report Section ---
frame_report = tk.LabelFrame(root, text="Stock Report", bg="#2c2c2c",
                              fg="white", font=("Arial", 11))
frame_report.pack(fill="both", expand=True, padx=20, pady=5)

report_box = scrolledtext.ScrolledText(frame_report, height=8, bg="#1e1e1e",
                                        fg="#00ff99", font=("Courier", 10))
report_box.pack(fill="both", expand=True, padx=5, pady=5)

def show_report():
    report_box.delete(1.0, tk.END)
    current_stock = aid_flow.get_all_items()
    if not current_stock:
        report_box.insert(tk.END, "No items in inventory yet.\n")
        return
    report_gen = StockReport(current_stock)
    summary = report_gen.generate_summary()
    for line in summary:
        report_box.insert(tk.END, line + "\n")

tk.Button(frame_report, text="Generate Report", bg="#ff9800", fg="white",
          command=show_report).pack(pady=5)

root.mainloop()