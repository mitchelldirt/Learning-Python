import datetime
import pytz


class Account:
    """ Simple account class with balance """

    # can be static method instead. Names starting with an _ are non-public.
    # Static methods are useful to group some utility function together with a class
    # Static methods don't need access to any information apart from the parameters provided
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

# Initialize the account class with name and balance attributes
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

# Deposit an amount of money. Print balance afterwards
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))
# Withdraw an amount of money and raise an error if account would go negative. Print balance after.
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            raise ValueError("Amount must be greater than 0 and no more than your account balance")
        self.show_balance()

# Method to show the account balance
    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


# Creating the account object mitchell
if __name__ == '__main__':
    mitchell = Account("Mitchell", 0)
    mitchell.show_balance()

    # Shows balance afterwards because it was added to the deposit method
    mitchell.deposit(2000)
    # Shows balance afterwards because it was added to the withdraw method
    mitchell.withdraw(1000)
    # print the transaction log
    mitchell.show_transactions()
