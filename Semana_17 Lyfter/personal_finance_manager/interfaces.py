from datetime import datetime
import FreeSimpleGUI as sg
from logic import FinanceLogic
from models import FinanceManager
from persistence import DataPersistence


class FinanceGUI:
    """Manages the graphical user interface using FreeSimpleGUI."""

    def __init__(self, manager: FinanceManager):
        self.manager = manager
        sg.theme("LightBlue2")

    def _get_table_data(self, movements_list=None):
        """Prepares movement data for the Table element and assigns category row colors."""
        target_movements = movements_list if movements_list is not None else self.manager.movements
        table_rows = []
        row_colors = []

        for idx, m in enumerate(target_movements):
            table_rows.append([m.date, m.title, f"₡{m.amount}", m.category, m.movement_type])
            
            # Get category color or default to white/light grey
            cat_color = self.manager.categories.get(m.category, "#FFFFFF")
            # row_colors format: (index, text_color, background_color)
            row_colors.append((idx, "black", cat_color))

        return table_rows, row_colors

    def run(self):
        """Launches the main application window and event loop."""
        # Initial data load
        DataPersistence.load_data(self.manager)

        initial_rows, initial_colors = self._get_table_data()

        # Layout for Main Window
        layout = [
            [sg.Text("Personal Finance Manager", font=("Helvetica", 16, "bold"))],
            [sg.HorizontalSeparator()],
            # Filter Frame
            [sg.Frame("Filter by Date Range", [
                [sg.Text("Start Date (dd/mm/yyyy):"), sg.Input(key="-START_DATE-", size=(12, 1)),
                 sg.Text("End Date (dd/mm/yyyy):"), sg.Input(key="-END_DATE-", size=(12, 1)),
                 sg.Button("Filter"), sg.Button("Clear Filter")]
            ])],
            [sg.HorizontalSeparator()],
            # Table of movements
            [sg.Table(
                values=initial_rows,
                headings=["Date", "Title", "Amount", "Category", "Type"],
                auto_size_columns=False,
                col_widths=[12, 20, 10, 15, 10],
                justification="center",
                key="-TABLE-",
                row_height=25,
                row_colors=initial_colors,
                enable_events=True
            )],
            # Totals display
            [sg.Text("Totals -> ", font=("Helvetica", 11, "bold")),
             sg.Text(self._get_totals_string(), key="-TOTALS-", font=("Helvetica", 11))],
            [sg.HorizontalSeparator()],
            # Action Buttons
            [sg.Button("Add Category", button_color=("white", "forestgreen")),
             sg.Button("Add Income", button_color=("white", "navy")),
             sg.Button("Add Expense", button_color=("white", "firebrick4")),
             sg.Button("Export to CSV", button_color=("white", "teal")),
             sg.Button("Exit", button_color=("white", "gray40"))]
        ]

        window = sg.Window("Personal Finance Manager", layout, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Exit":
                break

            elif event == "Add Category":
                self._open_category_window(window)

            elif event == "Add Income":
                self._open_movement_window(window, "Income")

            elif event == "Add Expense":
                self._open_movement_window(window, "Expense")

            elif event == "Filter":
                try:
                    start_str = values["-START_DATE-"]
                    end_str = values["-END_DATE-"]
                    filtered = FinanceLogic.filter_movements_by_date_range(
                        self.manager.movements, start_str, end_str
                    )
                    rows, colors = self._get_table_data(filtered)
                    window["-TABLE-"].update(values=rows, row_colors=colors)
                except ValueError as e:
                    sg.popup_error(str(e), title="Filter Error")

            elif event == "Clear Filter":
                window["-START_DATE-"].update("")
                window["-END_DATE-"].update("")
                rows, colors = self._get_table_data()
                window["-TABLE-"].update(values=rows, row_colors=colors)

            elif event == "Export to CSV":
                try:
                    DataPersistence.export_to_csv(self.manager)
                    sg.popup("Data successfully exported to 'financial_report.csv'!", title="Export Success")
                except Exception as e:
                    sg.popup_error(f"Error exporting file: {e}", title="Export Error")

        window.close()

    def _get_totals_string(self) -> str:
        """Helper to format totals string."""
        totals = self.manager.calculate_totals()
        return f"Incomes: ₡{totals['income']} | Expenses: ₡{totals['expense']} | Net Balance: ₡{totals['balance']}"

    def _refresh_main_window(self, window):
        """Updates table rows, colors, and totals on the main window."""
        rows, colors = self._get_table_data()
        window["-TABLE-"].update(values=rows, row_colors=colors)
        window["-TOTALS-"].update(self._get_totals_string())
        DataPersistence.save_data(self.manager)

    def _open_category_window(self, main_window):
        """Opens a secondary window to add a new category with color selection."""
        layout = [
            [sg.Text("Category Name:"), sg.Input(key="-CAT_NAME-", size=(20, 1))],
            [sg.Text("Choose Color:"), sg.Input("#FFFFFF", key="-COLOR_HEX-", size=(10, 1), disabled=True),
             sg.ColorChooserButton("Select Color", target="-COLOR_HEX-")],
            [sg.Button("Save Category"), sg.Button("Cancel")]
        ]
        cat_window = sg.Window("Add Category", layout, modal=True)

        while True:
            event, values = cat_window.read()
            if event == sg.WIN_CLOSED or event == "Cancel":
                break
            if event == "Save Category":
                try:
                    name = values["-CAT_NAME-"]
                    color = values["-COLOR_HEX-"]
                    self.manager.add_category(name, color)
                    sg.popup("Category added successfully!", title="Success")
                    cat_window.close()
                    break
                except ValueError as e:
                    sg.popup_error(str(e), title="Validation Error")

        cat_window.close()

    def _open_movement_window(self, main_window, movement_type: str):
        """Opens a secondary window to add an Income or an Expense."""
        if not self.manager.categories:
            sg.popup_error("You must create at least one category before adding movements.", title="Error")
            return

        category_list = list(self.manager.categories.keys())
        today_str = datetime.today().strftime("%d/%m/%Y")

        layout = [
            [sg.Text(f"Add New {movement_type}", font=("Helvetica", 12, "bold"))],
            [sg.Text("Title:"), sg.Input(key="-TITLE-", size=(25, 1))],
            [sg.Text("Amount:"), sg.Input(key="-AMOUNT-", size=(15, 1))],
            [sg.Text("Category:"), sg.Combo(category_list, key="-CATEGORY-", readonly=True, size=(22, 1))],
            [sg.Text("Date (dd/mm/yyyy):"), sg.Input(today_str, key="-DATE-", size=(15, 1))],
            [sg.Button("Save Movement"), sg.Button("Cancel")]
        ]
        mov_window = sg.Window(f"Add {movement_type}", layout, modal=True)

        while True:
            event, values = mov_window.read()
            if event == sg.WIN_CLOSED or event == "Cancel":
                break
            if event == "Save Movement":
                try:
                    title = values["-TITLE-"]
                    raw_amount = values["-AMOUNT-"]
                    category = values["-CATEGORY-"]
                    date_str = values["-DATE-"]

                    if not raw_amount.replace('.', '', 1).isdigit():
                        raise ValueError("Amount must be a valid number.")
                    
                    amount = float(raw_amount)

                    # Validate date using logic module
                    FinanceLogic.validate_new_date(date_str)

                    self.manager.add_movement(title, amount, category, movement_type, date_str)
                    self._refresh_main_window(main_window)
                    
                    sg.popup(f"New {movement_type.lower()} added successfully!", title="Success")
                    mov_window.close()
                    break
                except ValueError as e:
                    sg.popup_error(str(e), title="Validation Error")

        mov_window.close()