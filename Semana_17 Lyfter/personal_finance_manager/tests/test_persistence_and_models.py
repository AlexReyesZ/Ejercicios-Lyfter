from datetime import datetime
import pytest
from models import Category, FinanceManager
from persistence import DataPersistence


def test_add_movement_model_validations():
    manager = FinanceManager()
    manager.add_category("Food", "#80ffff")
    assert isinstance(manager.categories["Food"], Category)

    today = datetime.today().strftime("%d/%m/%Y")

    with pytest.raises(ValueError):
        manager.add_movement("Lunch", 0, "Food", "Expense", today)

    with pytest.raises(ValueError):
        manager.add_movement("Lunch", -1500, "Food", "Expense", today)

    with pytest.raises(ValueError):
        manager.add_movement("Lunch", 2500, "Food", "Expense", "hola")

    with pytest.raises(ValueError):
        manager.add_movement("Lunch", 2500, "Food", "Transfer", today)

    assert manager.add_movement("Lunch", 2500, "Food", "Expense", today) is True
    assert len(manager.movements) == 1


def test_persistence_save_and_load_with_tmp_path(tmp_path):
    temp_file = tmp_path / "test_finance_data.json"

    manager_to_save = FinanceManager()
    manager_to_save.add_category("Salary", "#00ff00")
    manager_to_save.add_category("Food", "#ffaa00")

    today = datetime.today().strftime("%d/%m/%Y")
    manager_to_save.add_movement("Monthly Pay", 500000, "Salary", "Income", today)
    manager_to_save.add_movement("Groceries", 12000, "Food", "Expense", today)

    DataPersistence.save_data(manager_to_save, file_path=temp_file)

    loaded_manager = FinanceManager()
    loaded = DataPersistence.load_data(loaded_manager, file_path=temp_file)

    assert loaded is True
    assert list(loaded_manager.categories.keys()) == ["Salary", "Food"]
    assert loaded_manager.categories["Food"].color == "#ffaa00"
    assert len(loaded_manager.movements) == 2
    assert loaded_manager.movements[0].title == "Monthly Pay"
    assert loaded_manager.movements[1].amount == 12000.0
    assert loaded_manager.calculate_totals() == {
        "income": 500000.0,
        "expense": 12000.0,
        "balance": 488000.0,
    }


def test_persistence_corrupted_json_and_missing_key(tmp_path):
    corrupted_file = tmp_path / "corrupted.json"
    corrupted_file.write_text("{not valid json", encoding="utf-8")

    manager = FinanceManager()
    with pytest.raises(ValueError):
        DataPersistence.load_data(manager, file_path=corrupted_file)

    missing_key_file = tmp_path / "missing_key.json"
    missing_key_file.write_text(
        """
        {
            "categories": [{"name": "Food", "color": "#FFFFFF"}],
            "movements": [
                {
                    "title": "Coffee",
                    "amount": 1500,
                    "category": "Food",
                    "movement_type": "Expense"
                }
            ]
        }
        """,
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        DataPersistence.load_data(manager, file_path=missing_key_file)