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

def test_eliminate_zero(coins_fixture):
    assert eliminate_zero(coins_fixture)=={1:10, 2:20}
    

def test_load_coins(capfd):
    #Verifies valid coin
    result=load_coins(5, 0.20)
    captured=capfd.readouterr()
    assert result is None
    assert captured.out.strip()=='= 5 0.2£'

    #Verifies invalid coin
    assert load_coins(20, 0.25)=='INVALID COIN'

def test_calculate_coins():

    
    expected_result = {}
    result = calculate_coins(20)
    assert result == expected_result


    







