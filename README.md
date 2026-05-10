# PCRF Aid-Flow Inventory System

> **A mission-critical logistics engine designed to streamline the intake and distribution of humanitarian aid for the Palestine Children's Relief Fund (PCRF).**

## 🌐 Overview
In high-pressure humanitarian environments, tracking life-saving supplies requires speed and precision. The **Aid-Flow Inventory System** is a resilient Python-based solution built to make certain that medical supplies, fluids, and PPE are accounted for from the moment they arrive until they reach the field.

## 🚀 Core Features
* **Dynamic Inventory Registration:** Real-time logging of aid supplies using optimized dictionary collections for instant lookup.
* **Strategic Stock Management:** Seamlessly update quantities to reflect incoming shipments or field distributions.
* **Automated Reporting:** Instant generation of color-coded stock alerts and inventory summaries for logistics coordinators.
* **Resilient Architecture:** Implemented with strict error-handling to maintain data integrity during rapid data entry.

## 🛠 Technical Stack
* **Language:** Python 3.x
* **Interface:** Tkinter GUI (Custom Dark-Themed UI)
* **Architecture:** Object-Oriented Programming (OOP) utilizing 4 specialized classes:
    * `SupplyItem`: The core data model for humanitarian aid.
    * `Inventory`: The backend engine managing the primary data collections.
    * `StockReport`: The logic layer for formatting and distribution alerts.
    * `InventoryApp`: The interactive frontend connecting the user to the logic.

## 📋 How to Run
1. Ensure you have Python installed.
2. Clone the repository.
3. Run the main launcher:
   ```bash
   python main.py

## 👥 Contributors
* **Danial Qasim:** Project Lead & Backend Architect
* **Aleeba Ghazanfar:** Frontend Engineering & UI Design
