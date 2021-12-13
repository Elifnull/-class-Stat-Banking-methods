class Bankaccount:
    def __init__(self, user_name: str, int_rate = .07, balance = 0):
        self.user_name = user_name
        self.int_rate = int_rate
        self.balance = balance
        
        #Assertions & validations
        assert int_rate > 0
        assert balance > 0
    
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
        print(f'Current Balance: $ {self.balance}')
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance *= (1 + (self.balance * self.int_rate))
        else:
            print(f"Current Balance: $ {self.balance} yields no intrest")
        return self


serge = Bankaccount("Serge", .05, 1000)

serge.display_account_info() ###the brackets SERGE THE BRACKETSSSS!!!!