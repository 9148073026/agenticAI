class Account():
    def __init__(self, account_number: str, balance: float, status: str):
        self.account_number = account_number
        self.balance = balance
        self.status = status

     def get_account_info(self):
        return {
            "account_number": self.account_number,
            "balance": self.balance,
            "status": self.status
        }
    def quickBal(account_number: str, balance: float):
        return {
            "account_number": account_number,
            "balance": balance
        }
    