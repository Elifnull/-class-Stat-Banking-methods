class Bankaccount:
    all_accounts = []
    def __init__(self, user_name, int_rate = .07, balance = 0):
        #instance level parameters
        self.user_name = user_name
        self.int_rate = int_rate
        self.balance = balance

        #class level parameters
        Bankaccount.all_accounts.append(self) #singular not plural.... append() not push()

        #Assertions & validations
        assert balance >= 0
        assert int_rate >= 0
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        assert amount > 0
        if amount > self.balance:
            self.balance -= 5
            print(f'Insufficient funds, $5 charge. Current Balance: $ {self.balance}')
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Account Name: {self.user_name}\nCurrent Balance: $ {self.balance}')
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance *= (1 + (self.int_rate))
        else:
            print(f"Current Balance: $ {self.balance} yields no intrest")
        return self
    @classmethod
    def see_all(cls):
        ##print(f'the eye that sees all sees: {cls.all_accounts}')
        for account in cls.all_accounts:
            account.display_account_info()


olga = Bankaccount("olga", .07, 1000).deposit(750).deposit(5).deposit(75).withdrawl(775).yield_intrest().display_account_info()

serge = Bankaccount("serge")

serge.deposit(100).deposit(98).withdrawl(20).withdrawl(20).withdrawl(35).withdrawl(40).yield_intrest().display_account_info()

Bankaccount.see_all()