class InsufficientAmount(Exception): 
  pass 

class NegativeAmount(Exception):
  pass
   
class Wallet(object): 
  def __init__(self, initial_amount=0): 
    self.balance = initial_amount 

  def spend_cash(self, amount): 
    if self.balance < amount: 
      raise InsufficientAmount(f'Not enough available to spend {amount}') 
    self.balance -= amount 

  def add_cash(self, amount): 
    if amount < 0:
      raise NegativeAmount(f"Can't add a negative amount")
    self.balance += amount 
