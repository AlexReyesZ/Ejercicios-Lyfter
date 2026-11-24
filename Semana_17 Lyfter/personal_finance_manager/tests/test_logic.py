from datetime import datetime, timedelta
import pytest
from logic import FinanceLogic


def test_is_future_date_today_past_and_future():
    today = datetime.today().strftime("%d/%m/%Y")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")

    assert FinanceLogic.is_future_date(today) is False
    assert FinanceLogic.is_future_date(yesterday) is False
    assert FinanceLogic.is_future_date(tomorrow) is True


def test_validate_new_date():
    today = datetime.today().strftime("%d/%m/%Y")
    past = (datetime.today() - timedelta(days=3)).strftime("%d/%m/%Y")
    future = (datetime.today() + timedelta(days=2)).strftime("%d/%m/%Y")

    FinanceLogic.validate_new_date(today) 
    FinanceLogic.validate_new_date(past) 

    with pytest.raises(ValueError):
        FinanceLogic.validate_new_date("hola")

    with pytest.raises(ValueError):
        FinanceLogic.validate_new_date(future)