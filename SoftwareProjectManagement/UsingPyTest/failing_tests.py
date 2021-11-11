import pytest 

from wallet import Wallet, InsufficientAmount, NegativeAmount 

 
# adding 10 to the constructor, means we will not actually be testing the default amount
def test_default_initial_amount(): 
  wallet = Wallet(10) 
  assert wallet.balance == 0 

  
def test_setting_initial_amount(): 
  wallet = Wallet(100) 
  assert wallet.balance == 100 

# Trying to add a negative amount should actually throw an error
def test_wallet_add_cash(): 
  wallet = Wallet(10) 
  wallet.add_cash(-80) 
  assert wallet.balance == -70 

# This should pass, now that the method has been updated to throw errors when adding negative amounts
def test_wallet_add_cash(): 
  wallet = Wallet(10) 
  with pytest.raises(NegativeAmount): 
    wallet.add_cash(-80) 
  
def test_wallet_spend_cash(): 
  wallet = Wallet(20) 
  wallet.spend_cash(10) 
  assert wallet.balance == 10 

# If we don't check that an error is thrown, when one is, the test will fail
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(): 
  wallet = Wallet() 
  wallet.spend_cash(100) 
