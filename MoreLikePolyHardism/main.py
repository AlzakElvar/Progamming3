from datetime import datetime as t

class PaymentMethod:
    def __init__(self, card_code, pin, balance):
        self.card_code = card_code
        self.pin = pin
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def validate(self):
        print("You cannot validate this payment")

    def check_balance(self):
        print(f"You have ${self.balance} in your account")


class CreditCard(PaymentMethod):
    def __init__(self, card_code, pin, balance, cvv, exp_month, exp_yr, holder_name, card_type):
        super().__init__(card_code, pin, balance)
        self.cvv = cvv
        self.exp_month = exp_month
        self.exp_yr = exp_yr
        self.holder_name = holder_name
        self.card_type = card_type

    def validate(self):
        if len(str(self.card_code)) != 16:
            return False, "Card number not long enough"

        if not self.is_not_expired():
            print(self.exp_yr)
            print(t.now().year)
            print(self.is_not_expired())
            return False, "Card has expired"

        if str(self.card_code)[0] == "4":
            return True, "Visa"
        elif str(self.card_code)[0] == "5":
            return True, "MasterCard"
        elif str(self.card_code)[0] == "7":
            return True, "Discover"
        else:
            return False, "We only accept Visa, MasterCard and Discover"

    def pay(self, amount):
        if self.validate()[0]:
            card_num = int(input("Please enter the card number: "))
            if not card_num == self.card_code:
                return False, "Card numbers do not match"

            pin = int(input("Please enter the card pin: "))
            if not pin == self.pin:
                return False, "Incorrect PIN"

            cvv = int(input("Please enter the cvv: "))
            if not cvv == self.cvv:
                return False, "The CVVs do not match"

            self.balance -= amount
            return True, f"${amount} has been removed from your balance"

        else:
            return self.validate()


    def is_not_expired(self):
        if t.now().year == self.exp_yr:
            if t.now().month > self.exp_month:
                return False,
            else:
                return True
        elif int(str(t.now().year)[2:3]) > self.exp_yr:
            return False
        else:
            return True


class PayPal(PaymentMethod):
    def __init__(self, card_code, pin, balance, account_id, is_verified):
        super().__init__(card_code, pin, balance)
        self.account_id = account_id
        self.is_verified = is_verified

    def verify_account(self, account_id):
        if account_id == self.account_id:
            self.is_verified = True

    def validate(self):
        if self.is_verified:
            return True, "This payment has been verified"
        else:
            return False, "You need to verify this payment"

    def pay(self, amount):
        if self.validate()[0]:
            print(self.validate()[1])
        else:
            return self.validate()

        pin = int(input("Please enter PIN: "))
        if pin == self.pin:
            if self.balance >= amount:
                self.balance -= amount
                return True, f"${amount} has been removed from your balance"
            else:
                return False, "Not enough money in your account"
        else:
            return False, "Please enter the correct pin"


class GiftCard(PaymentMethod):

    def reload(self, bal):
        if bal == 0:
            self.balance += bal
        else:
            print("There is still money in the card")

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, f"${amount} has been removed from your balance"
        else:
            return False, "Not enough money in your account"


class Crypto(PaymentMethod):
    def __init__(self, card_code, pin, balance, wallet_address, currency, network):
        super().__init__(card_code, pin, balance)
        self.wallet_address = wallet_address
        self.currency = currency
        self.network = network

    def get_transaction_fee(self):
        if self.currency == "Bitcoin":
            return True, 2.50
        elif self.currency == "Ethereum":
            return True, 1.25
        else:
            return False, "We only accept Bitcoin and Ethereum"

    def validate(self):
        if self.currency == "Ethereum":
            if not len(str(self.wallet_address)) == 42:
                return False, "Wallet address invalid"

        if "192.168" in self.network:
            return False, "You cannot trade over a private network"

        return True, " "

    def pay(self, amount):
        if self.validate()[0]:
            temp = self.get_transaction_fee()[1] + amount
            if self.balance >= temp:
                self.balance -= temp
                return True, f"${temp} has been removed from your account"
            else:
                return False, "Not enough money in your account"
        else:
            return self.validate()


class Venmo(PaymentMethod):
    def __init__(self, card_code, pin, balance, username, phone, linked_account):
        super().__init__(card_code, pin, balance)
        self.username = username
        self.phone = phone
        self.linked_account = linked_account

    def link_bank_account(self, account):
        self.linked_account = account

    def send_payment_request(self, account, amount):
        if account.pay(amount)[0]:
            return True, "Transaction successful"
        else:
            return account.pay(amount)

    def validate(self):
        if len(str(self.phone)) > 13:
            return False, "Phone number invalid"

        return True, ""

    def pay(self, amount):
        pin = int(input("Please enter your pin: "))
        if not pin == self.pin:
            return False, "PIN is invalid"

        if self.validate()[0]:
            if self.balance >= amount:
                self.balance -= amount
                return True, f"${amount} has been removed from your account"
            else:
                return False, "Not enough money in your account"
        else:
            return self.validate()


if __name__ == "__main__":
    MrOrange = CreditCard(5234123412341234, 336, 10000, 633, 10, 32, "Fish F. Orange", "Debit")
    MrFish = PayPal(1111222233334444, 336, 1000, 12, True)
    MrChick = GiftCard(1234123412341234, None, 566556,)
    MrTurtle = Crypto(1234123412341234, None, 50, 848541165565487415458544745, "Bitcoin", "111.111.1.1")
    MrClassy = Venmo(1111111111111111, 336, 120, "Cl@ssY", 8675309000, True)

    MrPharma = [
        MrOrange,
        MrFish,
        MrChick,
        MrTurtle,
        MrClassy
    ]

    for i in MrPharma:
        print(type(i))
#        print(i.validate())
        print(i.pay(25)[1])
        print()