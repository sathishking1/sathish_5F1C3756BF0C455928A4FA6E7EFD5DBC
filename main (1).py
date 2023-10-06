class BankAccount():
  def _init_(self,account_number,account_holder_name,initial_balance=0.0):
   self.__account_number=account_number  
   self.__account_holder_name=account_holder_name
   self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposit ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print("Withdraw ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print ("Account balance for {} (Account #{}): ₹{}".format(
        self._account_holder_name,self._account_number,
      self.__account_balance))

account=BankAccount(account_number="9344868020", account_holder_name="Amith Babu",     initial_balance=50000.0)

account.display_balance()
account.deposit(1000.0)
account.withdraw(500.0)
account.display_balance()