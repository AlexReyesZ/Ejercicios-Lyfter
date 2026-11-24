from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Category:
    """Represents a movement category with an associated display color."""
    name: str
    color: str = "#FFFFFF"

    def __post_init__(self) -> None:
        cleaned_name = self.name.strip()
        if not cleaned_name:
            raise ValueError("Category name cannot be empty.")
        self.name = cleaned_name
        self.color = self.color.strip() if self.color else "#FFFFFF"

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "color": self.color,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Category":  # <<<< AQUÍ [Paso 2: reconstrucción de Category]
        return cls(
            name=data["name"],
            color=data.get("color", "#FFFFFF"),
        )


@dataclass
class Movement:
    """Represents a financial movement (Income or Expense)."""
    title: str
    amount: float
    category: str
    movement_type: str
    date: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "movement_type": self.movement_type,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "Movement":
        return cls(
            title=str(data["title"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            movement_type=str(data["movement_type"]),
            date=str(data["date"]),
        )


class FinanceManager:
    """Coordinates categories, movements, and financial calculations."""

    VALID_MOVEMENT_TYPES = ("Income", "Expense")  # <<<< AQUÍ [Paso 3: tipos válidos en el modelo]

    def __init__(self) -> None:
        self.categories: Dict[str, Category] = {}  # <<<< AQUÍ [Paso 2: diccionario de objetos Category]
        self.movements: List[Movement] = []

    def add_category(self, name: str, color: str = "#FFFFFF") -> bool:
        category = Category(name=name, color=color)  # <<<< AQUÍ [Paso 2: instancia objeto Category]
        if category.name in self.categories:
            raise ValueError("Category already exists.")
        self.categories[category.name] = category  # <<<< AQUÍ [Paso 2: guarda objeto Category]
        return True

    def get_category_color(self, category_name: str, default: str = "#FFFFFF") -> str:  # <<<< AQUÍ [Paso 2: obtiene color desde Category]
        category = self.categories.get(category_name)
        return category.color if category else default

    def add_movement(
        self,
        title: str,
        amount: float,
        category: str,
        movement_type: str,
        date: str,
    ) -> bool:
        from logic import FinanceLogic  # <<<< AQUÍ [Paso 3: importación local para evitar ciclos]

        cleaned_title = title.strip()  # <<<< AQUÍ [Paso 3: limpia título]
        if not cleaned_title:  # <<<< AQUÍ [Paso 3: valida título no vacío]
            raise ValueError("Movement title cannot be empty.")  # <<<< AQUÍ [Paso 3]

        if isinstance(amount, bool) or not isinstance(amount, (int, float)):  # <<<< AQUÍ [Paso 3: valida tipo numérico]
            raise ValueError("Amount must be a valid number.")  # <<<< AQUÍ [Paso 3]

        numeric_amount = float(amount)  # <<<< AQUÍ [Paso 3: convierte a float]
        if numeric_amount <= 0:  # <<<< AQUÍ [Paso 3: rechaza 0 y negativos]
            raise ValueError("Amount must be greater than zero.")  # <<<< AQUÍ [Paso 3]

        cleaned_type = movement_type.strip()  # <<<< AQUÍ [Paso 3: limpia tipo]
        if cleaned_type not in self.VALID_MOVEMENT_TYPES:  # <<<< AQUÍ [Paso 3: valida Income/Expense]
            raise ValueError("Movement type must be 'Income' or 'Expense'.")  # <<<< AQUÍ [Paso 3]

        cleaned_category = category.strip()
        if not self.categories:
            raise ValueError("Cannot add movements without available categories.")
        if cleaned_category not in self.categories:
            raise ValueError("Selected category does not exist.")

        cleaned_date = date.strip()  # <<<< AQUÍ [Paso 3: limpia fecha]
        FinanceLogic.validate_new_date(cleaned_date)  # <<<< AQUÍ [Paso 3: valida formato y fecha no futura]

        movement = Movement(
            title=cleaned_title,  # <<<< AQUÍ [Paso 3]
            amount=numeric_amount,  # <<<< AQUÍ [Paso 3]
            category=cleaned_category,
            movement_type=cleaned_type,  # <<<< AQUÍ [Paso 3]
            date=cleaned_date,  # <<<< AQUÍ [Paso 3]
        )
        self.movements.append(movement)
        return True

    def calculate_totals(self) -> Dict[str, float]:
        income = 0.0
        expense = 0.0
        for m in self.movements:
            if m.movement_type == "Expense":
                expense += m.amount
            else:
                income += m.amount
        return {
            "income": income,
            "expense": expense,
            "balance": income - expense,
        }