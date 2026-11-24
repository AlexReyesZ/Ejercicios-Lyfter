from models import FinanceManager
from interfaces import FinanceGUI

def main():
    """Main application entry point."""
    manager = FinanceManager()
    app = FinanceGUI(manager)
    app.run()

if __name__ == "__main__":
    main()