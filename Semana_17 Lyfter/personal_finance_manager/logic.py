from datetime import datetime
from typing import List
from models import Movement

class FinanceLogic:
    """Handles date validations, future-date checks, and date-range filtering."""

    @staticmethod
    def validate_date_format(date_str: str) -> bool:
        """
        Validates that the date string strictly matches 'dd/mm/yyyy' 
        and is a real calendar date.
        """
        try:
            datetime.strptime(date_str.strip(), "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_future_date(date_str: str) -> bool:
        """Checks if a given date string is in the future compared to today."""
        try:
            parsed_date = datetime.strptime(date_str.strip(), "%d/%m/%Y").date()
            current_date = datetime.today().date()
            return parsed_date > current_date
        except ValueError:
            raise ValueError("Invalid date format for future check.")

    @classmethod
    def validate_new_date(cls, date_str: str) -> None:
        """Performs full date validation (format and future check)."""
        if not cls.validate_date_format(date_str):
            raise ValueError("Invalid date format (use dd/mm/yyyy).")
        if cls.is_future_date(date_str):
            raise ValueError("Date cannot be in the future.")

    @staticmethod
    def filter_movements_by_date_range(movements: List[Movement], start_date_str: str, end_date_str: str) -> List[Movement]:
        """Filters a list of movements between a start and end date (inclusive)."""
        try:
            start_date = datetime.strptime(start_date_str.strip(), "%d/%m/%Y").date()
            end_date = datetime.strptime(end_date_str.strip(), "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Invalid filter date format (use dd/mm/yyyy).")

        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        filtered = []
        for m in movements:
            m_date = datetime.strptime(m.date, "%d/%m/%Y").date()
            if start_date <= m_date <= end_date:
                filtered.append(m)

        return filtered