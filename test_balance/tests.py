import pytest

from main import User, MiniVenmo


@pytest.fixture
def user_a():
    user = {
        "username": "Patreze",
        "credit_card_number": "4242424242424242",
        "balance": 10000.00
    }
    return user

@pytest.fixture
def user_b():
    user = {
        "username": "Antonio",
        "credit_card_number": "4111111111111111",
        "balance": 20000.00
    }
    return user


@pytest.fixture
def created_user_a(user_a):
    user = User(user_a.get('username'))
    user.credit_card_number = None
    user.add_credit_card(user_a.get('credit_card_number'))
    user.balance = user_a.get('balance')
    return user


@pytest.fixture
def created_user_b(user_b):
    user = User(user_a.get('username'))
    user.credit_card_number = None
    user.add_credit_card(user_a.get('credit_card_number'))
    user.balance = user_a.get('balance')
    return user


def test_create_user(user_a):
    user = User(user_a.get('username'))
    user.balance = user_a.get('balance')
    assert type(user) is User
    assert user.username == "Patreze"
    assert user.balance == 10000.00


def test_minivenmo_create_user(created_user_a):
    mini_venmo = MiniVenmo()
    mv_user = mini_venmo.create_user(username="Patreze", balance=10000.00, credit_card_number="4242424242424242")
    assert type(mv_user) is User
    assert mv_user.username == created_user_a.username
    assert mv_user.balance == created_user_a.balance
    assert mv_user.credit_card_number == created_user_a.credit_card_number



