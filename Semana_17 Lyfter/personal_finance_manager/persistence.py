import csv
import json
import os
from typing import List
from models import Category, FinanceManager, Movement

DATA_FILE = "finance_data.json"

class DataPersistence:
    """Handles saving and loading data to/from JSON and exporting to CSV."""

    @staticmethod
    def save_data(manager: FinanceManager, filename: str = DATA_FILE) -> None:
        """Saves current categories and movements to a JSON file."""
        data = {
            "categories": manager.categories,
            "movements": [movement.to_dict() for movement in manager.movements]
        }
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    @staticmethod
    def load_data(manager: FinanceManager, filename: str = DATA_FILE) -> None:
        """Loads categories and movements from a JSON file if it exists."""
        if not os.path.exists(filename):
            return  # If file doesn't exist yet, start empty

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                
                # Load categories
                manager.categories = data.get("categories", {})
                
                # Load movements
                manager.movements = []
                for m_data in data.get("movements", []):
                    movement = Movement(
                        title=m_data["title"],
                        amount=m_data["amount"],
                        category=m_data["category"],
                        movement_type=m_data["movement_type"],
                        date=m_data["date"]
                    )
                    manager.movements.append(movement)
        except (json.JSONDecodeError, IOError) as e:
            raise ValueError(f"Error reading data file: {e}")

    @staticmethod
    def export_to_csv(manager: FinanceManager, filename: str = "financial_report.csv") -> None:
        """Exports all movements and final totals to a CSV file."""
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # Write headers
                writer.writerow(["Date", "Title", "Amount", "Category", "Type"])
                
                # Write movements
                for m in manager.movements:
                    writer.writerow([m.date, m.title, m.amount, m.category, m.movement_type])
                
                # Calculate and write totals summary at the end
                totals = manager.calculate_totals()
                writer.writerow([])
                writer.writerow(["Totals Summary"])
                writer.writerow([f"Incomes: ₡{totals['income']}"])
                writer.writerow([f"Expenses: ₡{totals['expense']}"])
                writer.writerow([f"Net Balance: ₡{totals['balance']}"])
        except IOError as e:
            raise IOError(f"Error exporting to CSV: {e}")