'''Task 35
You are developing a system to handle different payment methods. Implement an
abstract class called PaymentMethod with an abstract method processPayment().
The processPayment() method should be implemented by the concrete classes
that inherit from PaymentMethod and should simulate the payment processing
for each specific payment method.
Create two concrete classes CreditCardPayment and PayPalPayment that
extend the PaymentMethod class. Implement the processPayment() method in
both classes to display a message indicating the payment method being
processed.
Write the abstract class PaymentMethod, the concrete classes CreditCardPayment
and PayPalPayment, and the code to demonstrate polymorphism.
'''

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass

class CreditCardPayment(PaymentMethod):
    def processPayment(self):
        print("Processing credit card payment...")

class PayPalPayment(PaymentMethod):
    def processPayment(self):
        print("Processing PayPal payment...")

def processPayment(payment_method):
    payment_method.processPayment()

credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.processPayment()
paypal.processPayment()