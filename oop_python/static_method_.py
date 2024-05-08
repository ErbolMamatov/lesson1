"""
Управление банковскими счетами:
Создайте класс BankAccount, который представляет банковский счет. Каждый счет должен содержать следующую информацию:
Номер счета
Баланс счета
Имя владельца счета
Добавьте методы для пополнения счета, снятия средств со счета, проверки баланса счета и отображения информации о счете.
"""

# class BankAccount:
#
#     def __init__(self, number_account, owner, balance=0):
#         self.number_account = number_account
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def take_off(self, amount):
#         if amount > self.balance:
#             print('недостаточно средвст')
#
#         else:
#             self.balance -= amount
#
#     def check_balance(self):
#         print(f'owner {self.owner}:  balance {self.balance}')
#
#
# account = BankAccount(1, 'Erbol', 100)
# account.check_balance()
# account.deposit(100)
# account.check_balance()
# account.take_off(200)
# account.check_balance()




class Terminal:

    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def take_off(self, amount):
        if amount > self.balance:
            print('недостаточно средвст')

        else:
            self.balance -= amount
            self.balance -= 5

    def prover(self, amount):
        percentage = amount / 100

        # Вычисление суммы для снятия
        amount_to_withdraw = self.balance * percentage

        if amount_to_withdraw > self.balance:
            print("Недостаточно средств на счете!")
        else:
            self.balance -= amount_to_withdraw
            print(
                f"{self.balance}")

    def __str__(self):
        return f'number- {self.number}: name- {self.name}: balance- {self.balance}сом:'


terminal = Terminal(552388038, 'Erbol', 500)
terminal.deposit(500)
terminal.take_off(200)
terminal.prover(5)
print(terminal)



# class Megacom:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def overflow(self, amount):
#         self.balance += amount
#
#     def take_off(self, amount):
#         if amount >= self.balance:
#             print('не достаточно средств для обновления тарифа'
#                   ' пожайлуста пополните баланс до 200 сом !')
#
#         else:
#             self.balance -= 200
#             print('ваш тариф обновлен спасибо что выбераете нас:)')
#
#     def check_balance(self):
#         print(f'имя {self.name} на вашем балансе: {self.balance}')
#
#
# mega = Megacom('Erbol', 100)
# mega.check_balance()
#
# mega.overflow(500)
# mega.check_balance()
#
# mega.take_off(200)
# mega.check_balance()





