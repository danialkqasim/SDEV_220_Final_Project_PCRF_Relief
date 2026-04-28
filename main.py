from models import Inventory, StockReport

def main():
    # Initialize system
    aid_flow = Inventory()

    # --- Step 1: Inventory Registration ---
    # Adding initial medical supplies
    aid_flow.add_new_item("Amoxicillin", "Antibiotics", 500)
    aid_flow.add_new_item("Sterile Bandages", "First Aid", 1200)
    aid_flow.add_new_item("Surgical Kit", "Instruments", 50)

    # --- Step 2: Stock Management ---
    # Update quantities (to simulate received shipment and distribution)
    aid_flow.update_quantity("Amoxicillin", 100) # Received more
    aid_flow.update_quantity("Surgical Kit", -10) # Distributed to field

    # --- Step 3: Reporting ---
    # Pull current data into list for report
    current_stock = aid_flow.get_all_items()
    report_gen = StockReport(current_stock)
    
    final_report = report_gen.generate_summary()

    # Display results
    print("--- PCRF AID-FLOW SYSTEM: CURRENT INVENTORY ---")
    for line in final_report:
        print(line)

if __name__ == "__main__":
    main()