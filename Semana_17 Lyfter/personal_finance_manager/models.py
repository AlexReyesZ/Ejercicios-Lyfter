from datetime import datetime
from typing import Dict, List, Union

class Category:
    """Represents a financial category with an optional custom color."""
    def __init__(self, name: str, color: str = "#FFFFFF"):
        self.name = name
        self.color = color

    def to_dict(self) -> dict:
        return {"name": self.name, "color": self.color}


class Movement:
    """Represents an income or an expense movement."""
    def __init__(self, title: str, amount: float, category: str, movement_type: str, date: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.movement_type = movement_type  # "Income" or "Expense"
        self.date = date  # Format: "dd/mm/yyyy"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "movement_type": self.movement_type,
            "date": self.date
        }


class FinanceManager:
    """Core controller that manages categories, movements, and financial calculations."""
    def __init__(self):
        self.categories: Dict[str, str] = {}  # Format: {"CategoryName": "#HEXCOLOR"}
        self.movements: List[Movement] = []

    def add_category(self, name: str, color: str = "#FFFFFF") -> bool:
        """Adds a new category if it doesn't already exist."""
        clean_name = name.strip()
        if not clean_name:
            raise ValueError("Category name cannot be empty.")
        if clean_name in self.categories:
            raise ValueError("Category already exists.")
        
        self.categories[clean_name] = color
        return True

    def add_movement(self, title: str, amount: float, category: str, movement_type: str, date: str) -> bool:
        """Adds a new movement after validating categories and parameters."""
        if not self.categories:
            raise ValueError("Cannot add movements without available categories.")
        if category not in self.categories:
            raise ValueError("Selected category does not exist.")
        if not title.strip():
            raise ValueError("Movement title cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Adjust amount sign based on type
        final_amount = -abs(amount) if movement_type == "Expense" else abs(amount)

        new_movement = Movement(
            title=title.strip(),
            amount=final_amount,
            category=category,
            movement_type=movement_type,
            date=date
        )
        self.movements.append(new_movement)
        return True

    def calculate_totals(self) -> dict:
        """Calculates total incomes, total expenses, and net balance."""
        total_income = sum(m.amount for m in self.movements if m.movement_type == "Income")
        total_expense = sum(abs(m.amount) for m in self.movements if m.movement_type == "Expense")
        net_balance = total_income - total_expense
        return {
            "income": total_income,
            "expense": total_expense,
            "balance": net_balance
        }