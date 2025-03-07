"""This module defines the PenaltyStrategy class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee

class PenaltyStrategy(PaymentStrategy):
    """
    """
    def process_payment(self, 
                        account:BillingAccount, 
                        payee: Payee, 
                        amount: float)-> str:
        # Apply a payment to the account:
        account.deduct_balance(payee, amount)

        # Obtain the updated balance of the account:   
        balance = account.get_balance(payee)

        if balance <= 0.0:
            message = f"Processed payment of ${amount:,.2f}." \
                    + f" New balance: ${balance:,.2f}."
        else:
            penalty_fee = 10.00
            account.add_balance(payee, penalty_fee)
            updated_balance = account.get_balance(payee)

            message = f"Insufficient payment." \
                    + f" Added penalty fee of ${penalty_fee:,.2f}." \
                    + f" New balance: ${updated_balance:,.2f}."

        return message 
