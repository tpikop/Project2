# project2_gui.py

import tkinter as tk
from typing import Optional

class BankAccount:
    """
    Represents a bank account.

    Attributes:
        _name (str): The account name.
        _balance (float): The account balance.
    """

    def __init__(self, name: str, balance: float = 0.0):
        """
        Initializes a BankAccount instance.

        Args:
            name (str): The initial account name.
            balance (float, optional): The initial account balance. Defaults to 0.0.
        """
        self._name = name
        self._balance = balance

    def get_name(self) -> str:
        """
        Returns the account name.

        Returns:
            str: The account name.
        """
        return self._name

    def set_name(self, new_name: str) -> None:
        """
        Sets the account name.

        Args:
            new_name (str): The new account name.
        """
        self._name = new_name

    def get_balance(self) -> float:
        """
        Returns the account balance.

        Returns:
            float: The account balance.
        """
        return self._balance

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account, if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= self._balance:
            self._balance -= amount

class BankAccountGUI:
    """
    Represents the GUI for interacting with a BankAccount.

    Attributes:
        bank_app (BankAccount): The BankAccount instance associated with the GUI.
        root (tk.Tk): The main Tkinter window.
        account_name_var (tk.StringVar): The Tkinter StringVar for the account name.
        name_label (tk.Label): The label for the account name.
        balance_label (tk.Label): The label for the account balance.
        name_entry (tk.Entry): The entry widget for the account name.
        balance_entry (tk.Entry): The entry widget for the account balance.
        deposit_button (tk.Button): The button for depositing funds.
        withdraw_button (tk.Button): The button for withdrawing funds.
        display_button (tk.Button): The button for displaying account information.
    """

    def __init__(self, bank_app: BankAccount):
        """
        Initializes a BankAccountGUI instance.

        Args:
            bank_app (BankAccount): The BankAccount instance to associate with the GUI.
        """
        self.bank_app = bank_app

        self.root = tk.Tk()
        self.root.title("Bank Account GUI")

        # StringVar to store the account name
        self.account_name_var: tk.StringVar = tk.StringVar()
        self.account_name_var.set(self.bank_app.get_name())  # Set initial value

        # Labels
        self.name_label: tk.Label = tk.Label(self.root, text="Account Name:")

        self.balance_label: tk.Label = tk.Label(self.root, text="Account Balance:")

        # Entry Widgets
        self.name_entry: tk.Entry = tk.Entry(self.root, textvariable=self.account_name_var)  # Use StringVar

        self.balance_entry: tk.Entry = tk.Entry(self.root)

        # Buttons
        self.deposit_button: tk.Button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.withdraw_button: tk.Button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.display_button: tk.Button = tk.Button(self.root, text="Display Account Info", command=self.bank_app.display_info)

        # Layout
        self.name_label.grid(row=0, column=0)
        self.balance_label.grid(row=1, column=0)
        self.name_entry.grid(row=0, column=1)
        self.balance_entry.grid(row=1, column=1)
        self.deposit_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.withdraw_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Disable buttons initially if the name is empty
        self.update_button_state()

    def deposit(self) -> None:
        """
        Deposits funds into the associated BankAccount based on the input amount.
        """
        amount: float = float(self.balance_entry.get())
        self.bank_app.deposit(amount)

    def withdraw(self) -> None:
        """
        Withdraws funds from the associated BankAccount based on the input amount.
        """
        amount: float = float(self.balance_entry.get())
        self.bank_app.withdraw(amount)

    def update_account_name(self) -> None:
        """
        Updates the account name in the associated BankAccount based on the input from the GUI.
        """
        new_name: str = self.name_entry.get()
        self.bank_app.set_name(new_name)
        self.account_name_var.set(new_name)

        # Enable/disable buttons based on the name
        self.update_button_state()

    def clear_balance_entry(self) -> None:
        """
        Clears the content of the balance entry widget.
        """
        self.balance_entry.delete(0, tk.END)  # Clear the content of the entry widget

    def update_button_state(self) -> None:
        """
        Updates the state of deposit and withdraw buttons based on whether the account name is empty.
        """
        # Disable buttons if the name is empty
        is_name_empty: bool = not bool(self.name_entry.get())
        self.deposit_button["state"] = tk.NORMAL if not is_name_empty else tk.DISABLED
        self.withdraw_button["state"] = tk.NORMAL if not is_name_empty else tk.DISABLED
