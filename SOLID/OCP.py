from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def processPayment(self,amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing credit card payment of {amount}")
    
class PayPalPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing PayPal payment {amount}")
        
def processPayment(processor, amount):
    processor.processPayment(amount)

def main():
    creditCardProcessor=CreditCardPaymentProcessor()
    payPalProcessor=PayPalPaymentProcessor()
    processPayment(payPalProcessor,100)
    
    processPayment(creditCardProcessor,200)

if __name__=="__main__":
    main()