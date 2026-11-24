import csv
import json
from pathlib import Path
from typing import Optional, Union
from models import Category, FinanceManager, Movement

BASE_DIR = Path(__file__).resolve().parent  # <<<< AQUÍ [carpeta real del proyecto basada en __file__]
DEFAULT_DATA_FILE = BASE_DIR / "finance_data.json"  # <<<< AQUÍ [ruta confiable del JSON]
DEFAULT_CSV_FILE = BASE_DIR / "financial_report.csv"  # <<<< AQUÍ [ruta confiable del CSV]


class DataPersistence:
    """Handles saving and loading finance data in JSON and exporting reports to CSV."""

    @staticmethod
    def save_data(manager: FinanceManager, file_path: Optional[Union[str, Path]] = None) -> Path:  # <<<< AQUÍ [acepta ruta opcional, ideal para tests con tmp_path]
        target_path = Path(file_path) if file_path is not None else DEFAULT_DATA_FILE  # <<<< AQUÍ
        target_path.parent.mkdir(parents=True, exist_ok=True)  # <<<< AQUÍ

        payload = {
            "categories": [cat.to_dict() for cat in manager.categories.values()],  # <<<< AQUÍ [guarda objetos Category como dict]
            "movements": [mov.to_dict() for mov in manager.movements],
        }

        with target_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4, ensure_ascii=False)

        return target_path

    @staticmethod
    def load_data(manager: FinanceManager, file_path: Optional[Union[str, Path]] = None) -> bool:  # <<<< AQUÍ
        target_path = Path(file_path) if file_path is not None else DEFAULT_DATA_FILE  # <<<< AQUÍ

        if not target_path.exists():
            return False

        try:
            with target_path.open("r", encoding="utf-8") as f:
                raw_data = json.load(f)
        except json.JSONDecodeError as exc:  # <<<< AQUÍ [JSON corrupto]
            raise ValueError(f"Corrupted JSON file '{target_path.name}': {exc}") from exc  # <<<< AQUÍ

        if not isinstance(raw_data, dict):  # <<<< AQUÍ [estructura raíz inválida]
            raise ValueError("Invalid data format in JSON file: expected an object.")  # <<<< AQUÍ

        try:
            loaded_categories = {}
            raw_categories = raw_data.get("categories", [])

            if isinstance(raw_categories, dict):  # <<<< AQUÍ [compatibilidad con formato anterior {"Food": "#fff"}]
                for cat_name, cat_color in raw_categories.items():
                    cat = Category(name=str(cat_name), color=str(cat_color))
                    loaded_categories[cat.name] = cat
            elif isinstance(raw_categories, list):  # <<<< AQUÍ [formato con lista de dicts de Category]
                for item in raw_categories:
                    if isinstance(item, dict):
                        cat = Category.from_dict(item)
                    else:
                        cat = Category(name=str(item))
                    loaded_categories[cat.name] = cat
            else:
                raise ValueError("Invalid 'categories' format in JSON file.")

            loaded_movements = []
            raw_movements = raw_data.get("movements", [])
            if not isinstance(raw_movements, list):
                raise ValueError("Invalid 'movements' format in JSON file.")

            for item in raw_movements:
                if not isinstance(item, dict):
                    raise ValueError("Each movement must be a JSON object.")
                # Verifica llaves obligatorias antes de construir Movement
                for required_key in ("title", "amount", "category", "movement_type", "date"):  # <<<< AQUÍ [valida llaves obligatorias]
                    if required_key not in item:  # <<<< AQUÍ
                        raise ValueError(f"Missing required field '{required_key}' in movement data.")  # <<<< AQUÍ
                loaded_movements.append(Movement.from_dict(item))

        except (KeyError, TypeError, ValueError) as exc:  # <<<< AQUÍ [captura llaves faltantes o tipos inválidos]
            raise ValueError(f"Invalid movement or category data: {exc}") from exc  # <<<< AQUÍ

        manager.categories = loaded_categories
        manager.movements = loaded_movements
        return True

    @staticmethod
    def export_to_csv(manager: FinanceManager, csv_path: Optional[Union[str, Path]] = None) -> Path:  # <<<< AQUÍ
        target_csv = Path(csv_path) if csv_path is not None else DEFAULT_CSV_FILE  # <<<< AQUÍ
        target_csv.parent.mkdir(parents=True, exist_ok=True)

        with target_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Title", "Amount", "Category", "Type"])
            for m in manager.movements:
                writer.writerow([m.date, m.title, m.amount, m.category, m.movement_type])

        return target_csv