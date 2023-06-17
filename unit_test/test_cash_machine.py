import pytest 
from cash_machine import load_coins, exchange, eliminate_zero,calculate_coins

@pytest.fixture
def coins_fixture():
    coins={0.20:0, 0.50:0, 1:10, 2:20}
    return coins

@pytest.fixture
def notes_fixture():
    notes={5:0, 10:0,20:0}
    return notes

def test_eliminate_zero(coins_fixture,notes_fixture):
    assert eliminate_zero(coins_fixture)=={1:10, 2:20}
    assert eliminate_zero(notes_fixture)=={}
    

def test_load_coins(capfd):
    #Verifies valid coin, this updates the coin dictionary
    result=load_coins(50, 0.20)
    captured=capfd.readouterr()
    assert result is None
    assert captured.out.strip()=='= 50 0.2£'

    #Verifies invalid coin
    assert load_coins(20, 0.25)=='INVALID COIN'

def test_calculate_coins():
    #Verifies invalid coin converstion
    result = calculate_coins(20)
    expected_result = None
    assert result == expected_result

    #Verifies valid coin converstion
    assert calculate_coins(5)=={0.2:25}

def test_invalid_exchange(capfd):
    result=exchange(20)
    captured=capfd.readouterr()
    assert result is None
    assert captured.out.strip()=='<CANNOT EXCHANGE\n=50 0.2£,'

def test_valid_exchange(capfd):
    #Verifies a valid exchange of bank note and updates coin and banknote dictionary
    result=exchange(5)
    captured=capfd.readouterr()
    assert result is None
    assert captured.out.strip()=='<25 0.2£\n=25 0.2£, 1 5£'
    

   

   
    







