"""This module defines the PartialPaymentStrategy class."""

__author__ = ""
__version__ = ""

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee


class PartialPaymentStrategy(PaymentStrategy):
    """
    """
    def process_payment(self, 
                        account: BillingAccount, 
                        payee: Payee, 
                        amount: float )-> str:
        # Apply a payment to the account:
        account.deduct_balance(payee, amount)

        # Obtain the updated balance of the account:
        balance = account.get_balance(payee)

        if balance <= 0.0:
            message = f"Processed payment of ${amount:,.2f}. New balance: ${balance:,.2f}."
        else:
            message =  f"Partial payment of ${amount:,.2f} accepted. New balance: ${balance:,.2f}."

        return message