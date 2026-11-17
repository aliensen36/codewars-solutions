import pytest
from solution import User


@pytest.fixture
def jeff():
    return User('Jeff', 70, True)


@pytest.fixture
def joe():
    return User('Joe', 70, True)


def test_withdraw_success(jeff):
    assert jeff.withdraw(2) == 'Jeff has 68.'


def test_withdraw_overdraw(jeff):
    with pytest.raises(ValueError):
        jeff.withdraw(100)
    # баланс не изменился
    assert jeff.balance == 70


def test_check_success(jeff, joe):
    # Joe получает 50 от Jeff: Joe 70→120, Jeff 70→20
    assert joe.check(jeff, 50) == 'Joe has 120 and Jeff has 20.'
    assert jeff.balance == 20
    assert joe.balance == 120


def test_check_non_checking_account(jeff):
    mia = User('Mia', 1000, False)
    with pytest.raises(ValueError):
        jeff.check(mia, 5)  # Mia — issuer, у неё checking_account=False


def test_check_bad_check(jeff, joe):
    # Joe пытается выписать чек на 100, а у него 70
    with pytest.raises(ValueError):
        jeff.check(joe, 100)
    # балансы не изменились
    assert joe.balance == 70
    assert jeff.balance == 70


def test_add_cash_int(jeff):
    assert jeff.add_cash(20) == 'Jeff has 90.'
    assert isinstance(jeff.balance, int)


def test_add_cash_float_stays_int(jeff):
    # 70 + 20.00 = 90, но не 90.0
    assert jeff.add_cash(20.00) == 'Jeff has 90.'
    assert isinstance(jeff.balance, int)
    assert jeff.balance == 90


def test_checking_account_attribute():
    assert User('Mia', 1000, False).checking_account is False
    assert User('Mia', 1000, True).checking_account is True
