import pytest
from models import FinanceManager, Category, Movement
from logic import FinanceLogic

def test_add_category_success():
    """Test 1: Successfully adds a category with color."""
    manager = FinanceManager()
    assert manager.add_category("Food", "#FFA500") is True
    assert "Food" in manager.categories
    assert manager.categories["Food"] == "#FFA500"

def test_add_duplicate_category_raises_error():
    """Test 2: Adding a duplicate category raises ValueError."""
    manager = FinanceManager()
    manager.add_category("Transport")
    with pytest.raises(ValueError, match="Category already exists."):
        manager.add_category("Transport")

def test_add_movement_without_categories_raises_error():
    """Test 3: Adding movement without categories raises ValueError."""
    manager = FinanceManager()
    with pytest.raises(ValueError, match="Cannot add movements without available categories."):
        manager.add_movement("Salary", 1000, "Work", "Income", "01/07/2025")

def test_add_movement_success():
    """Test 4: Successfully adds an income movement and adjusts values."""
    manager = FinanceManager()
    manager.add_category("Salary")
    assert manager.add_movement("Monthly Pay", 1500, "Salary", "Income", "01/07/2025") is True
    assert len(manager.movements) == 1
    assert manager.movements[0].amount == 1500

def test_calculate_totals():
    """Test 5: Calculates total incomes, expenses, and net balance correctly."""
    manager = FinanceManager()
    manager.add_category("Work")
    manager.add_category("Food")
    manager.add_movement("Salary", 2000, "Work", "Income", "01/07/2025")
    manager.add_movement("Groceries", 500, "Food", "Expense", "02/07/2025")
    
    totals = manager.calculate_totals()
    assert totals["income"] == 2000
    assert totals["expense"] == 500
    assert totals["balance"] == 1500

def test_validate_date_format():
    """Test 6: Validates correct and incorrect date formats (dd/mm/yyyy)."""
    assert FinanceLogic.validate_date_format("15/08/2025") is True
    assert FinanceLogic.validate_date_format("2025-08-15") is False
    assert FinanceLogic.validate_date_format("invalid-date") is False

def test_is_future_date():
    """Test 7: Detects future dates correctly."""
    # Future year will always return True for is_future_date
    assert FinanceLogic.is_future_date("31/12/2035") is True

def test_filter_movements_by_date_range():
    """Test 8: Filters movements accurately by a specific date range."""
    m1 = Movement("Job", 1000, "Work", "Income", "01/07/2025")
    m2 = Movement("Pizza", 20, "Food", "Expense", "05/07/2025")
    m3 = Movement("Trip", 500, "Leisure", "Expense", "20/07/2025")
    
    movements = [m1, m2, m3]
    filtered = FinanceLogic.filter_movements_by_date_range(movements, "01/07/2025", "10/07/2025")
    
    assert len(filtered) == 2
    assert m1 in filtered
    assert m2 in filtered
    assert m3 not in filtered