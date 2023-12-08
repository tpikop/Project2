# project2_main.py

from tkinter import messagebox
from project2_gui import BankAccountGUI
from typing import Union

class Account:
    def __init__(self, name: str, balance: float = 0.0) -> None:
        """
        Initialize an Account.

        :param name: The account name.
        :param balance: The initial account balance (default is 0.0).
        """
        self.__account_name: str = name
        self.__account_balance: float = balance

    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into the account.

        :param amount: The amount to deposit.
        :return: True if the deposit is successful, False otherwise.
        """
        if self.__validate_name():
            if amount > 0:
                self.__account_balance += amount
                return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the account.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal is successful, False otherwise.
        """
        if self.__validate_name():
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
        return False

    def get_balance(self) -> float:
        """
        Get the account balance.

        :return: The account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the account name.

        :return: The account name.
        """
        return self.__account_name

    def set_balance(self, value: float) -> None:
        """
        Set the account balance.

        :param value: The new balance value.
        """
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value: str) -> None:
        """
        Set the account name.

        :param value: The new name.
        """
        self.__account_name = value

    def __str__(self) -> str:
        """
        Return a string representation of the account.

        :return: A string representation of the account.
        """
        return f"Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}"

    def __validate_name(self) -> bool:
        """
        Validate the account name.

        :return: True if the account name is valid, False otherwise.
        """
        if not self.__account_name:
            messagebox.showerror("Error", "Please enter an account name")
            return False
        return True

class SavingAccount(Account):
    MINIMUM: float = 100.0
    RATE: float = 0.02

    def __init__(self, name: str) -> None:
        """
        Initialize a SavingAccount.

        :param name: The account name.
        """
        super().__init__(name, balance=self.MINIMUM)
        self.__deposit_count: int = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into the saving account with interest calculation.

        :param amount: The amount to deposit.
        :return: True if the deposit is successful, False otherwise.
        """
        if super().deposit(amount):
            self.__deposit_count += 1
            if self.__deposit_count % 5 == 0:
                self.apply_interest()
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the saving account.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal is successful, False otherwise.
        """
        if super().withdraw(amount):
            return True
        return False

    def apply_interest(self) -> None:
        """
        Apply interest to the saving account balance.
        """
        interest: float = self.get_balance() * self.RATE
        self.set_balance(self.get_balance() + interest)

    def __str__(self) -> str:
        """
        Return a string representation of the saving account.

        :return: A string representation of the saving account.
        """
        return f"SAVING ACCOUNT: Account name = {self.get_name()}, Account balance = ${self.get_balance():.2f}"

class BankApp:
    def __init__(self) -> None:
        """
        Initialize the BankApp.
        """
        # Creating an instance of SavingAccount
        self.account: SavingAccount = SavingAccount("John Doe")

    def deposit(self, amount: Union[str, float]) -> None:
        """
        Deposit funds into the account.

        :param amount: The amount to deposit.
        """
        try:
            amount = float(amount)
            if self.account.deposit(amount):
                messagebox.showinfo("Deposit", f"Successfully deposited ${amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the deposit amount")

    def withdraw(self, amount: Union[str, float]) -> None:
        """
        Withdraw funds from the account.

        :param amount: The amount to withdraw.
        """
        try:
            amount = float(amount)
            if self.account.withdraw(amount):
                messagebox.showinfo("Withdraw", f"Successfully withdrew ${amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the withdrawal amount")

    def display_info(self) -> None:
        """
        Display account information.
        """
        info: str = str(self.account)
        messagebox.showinfo("Account Info", info)

if __name__ == "__main__":
    app: BankApp = BankApp()
    gui: BankAccountGUI = BankAccountGUI(app)
    gui.root.mainloop()
# DocuSign: End of Code
