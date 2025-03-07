"""This module defines the Payment class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee

class Payment:
    """
    Maintains the payment strategy

    """

    def __init__ (self, 
                  strategy: PaymentStrategy):
        """
        Initializes the class attributes with arguements values.
        
        Args:
            strategy (PaymentStrategy): Payment strategy 
                used to process payments.
        
        Raises:
            ValueError: for invalid strategy.

        """

        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy")

    def pay_bill(self, 
                 account: BillingAccount, 
                 payee: Payee, 
                 amount: float) -> str:
        """
        Processes a payment using the payment strategy.
        
        Args:
            account (BillingAccount): The billing account for payment.
            payee (Payee): The payee to which the amount applies.
            amount (float): The amount to be paid.
        Returns:
             The result of strategy attribute' process payment method.

        """
        return self.__strategy.process_payment(account, 
                                               payee, 
                                               amount)
