"""This module defines the PartialPaymentStrategy class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee


class PartialPaymentStrategy(PaymentStrategy):
    """
    A payment strategy for partial payments. 

    """
    def process_payment(self, 
                        account: BillingAccount, 
                        payee: Payee, 
                        amount: float )-> str:
        """
        Initializes the class attributes with argument values.
       
        Args:
            account (BillingAccount): The billing account 
                from which the payment will get deducted.
            payee (Payee): The payee to which the process 
                payment applies.
            amount (float): The amount to be deducted 
                from the billing account.
        
        Returns:
            str: The message  string.

        """
        # Apply a payment to the account:
        account.deduct_balance(payee, amount)

        # Obtain the updated balance of the account:
        balance = account.get_balance(payee)

        if balance <= 0.0:
            message = f"Processed payment of ${amount:,.2f}."\
                     + f" New balance: ${balance:,.2f}."
        else:
            message =  f"Partial payment of ${amount:,.2f} accepted." \
                     + f" New balance: ${balance:,.2f}."

        return message