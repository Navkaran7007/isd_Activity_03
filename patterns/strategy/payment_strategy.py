"""This module defines the PaymentStrategy class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee


class PaymentStrategy(ABC):
    """
    class PaymentStrategy: Maintains the payments.

    """
    @abstractmethod
    def process_payment(self, 
                        account: BillingAccount, 
                        payee: Payee, 
                        amount: float)-> str:
        """
        An abstract method for a payment from a billing account.
        
        Args:
            account (BillingAccount): The billing 
                account for payment.
            payee (Payee): The payee to which the process 
                payment applies.
            amount (float): The amount to be paid.

        """
        pass
