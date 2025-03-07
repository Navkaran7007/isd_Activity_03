"""This module defines the Payment class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee

class Payment:
    """
    """

    def __init__ (self, 
                  strategy: PaymentStrategy):

        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy")

    def pay_bill(self, 
                 account: BillingAccount, 
                 payee: Payee, 
                 amount: float) -> str:
        return self.__strategy.process_payment(account, 
                                               payee, 
                                               amount)
