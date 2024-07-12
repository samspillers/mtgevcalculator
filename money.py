from dataclasses import dataclass

# Immutable money class
@dataclass(frozen=True)
class Money:
    __currency: str
    __amount: float

    def get_currency(self) -> str:
        return self.__currency
    
    def get_amount(self) -> float:
        return self.__amount

    def combine(self, other: 'Money') -> 'Money':
        assert self.__currency == other.__currency
        return Money(self.__currency, self.__amount + other.__amount)
    
    def add(self, addAmount: float) -> 'Money':
        return Money(self.__currency, self.__amount + addAmount)

    def scale(self, factor: float) -> 'Money':
        return Money(self.__currency, self.__amount * factor)
    
    def copy(self, amount: float) -> 'Money':
        return Money(self.__currency, amount)
    
    def __str__(self) -> str:
        return str((self.__currency, self.__amount))
        

# Wrapper for collection of money
class Wallet:
    __wallet: dict[str, Money]

    def __init__(self, initial_pool: list[Money] = []) -> None:
        self.__wallet = {}
        for money in initial_pool:
            self.add(money)
    
    def get(self, currency: str) -> Money:
        return self.__wallet[currency]
    
    def set(self, money: Money):
        self.__wallet[money.get_currency()] = money
    
    def add(self, money: Money):
        if money.get_currency() in self.__wallet:
            self.__wallet[money.get_currency()] = self.__wallet[money.get_currency()].combine(money)
        else:
            self.__wallet[money.get_currency()] = money

    def scaleWallet(self, factor: float):
        for currency in self.__wallet.keys():
            self.__wallet[currency] = self.__wallet[currency].scale(factor)

    def addWallet(self, other: 'Wallet'):
        for money in other.__wallet.values():
            self.add(money)
    
    def copy(self) -> 'Wallet':
        return Wallet(self.__wallet.values())

    def __str__(self) -> str:
        output = "["
        for money in self.__wallet.values():
            output += str(money) + ", "
        output = output[:-2] + "]"
        return output