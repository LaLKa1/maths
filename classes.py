from decimal import Decimal
from abc import ABC


class Expression:
    def __init__(self, left, right=None, operand=None):
        assert operand in (None, '=', '>', '>=', '<', '<=')
        self.left = left
        self.right = right
        self.operand = operand


class MathFunc(ABC):
    def is_define(self) -> bool:
        pass
    def calc_numeric_value(self):
        pass


class Number(Decimal, MathFunc):
    def is_define():
        return True
    def calc_numeric_value(self):
        return self


class Variable(MathFunc):
    def __init__(self, symbol:str='x'):
        self.symbol = symbol
    def is_define(self) -> bool:
        return False


class Addition(MathFunc):
    def __init__(self, values:list):
        assert len(values) > 1
        self.values:list = values
        
    def is_define(self) -> bool:
        return all(i.is_define() for i in self.values)
    
    def calc_numeric_value(self) -> Number:
        assert self.is_define()
        return sum(i.calc_numeric_value for i in self.values)


class Multiplication(MathFunc):
    def __init__(self, values:list):
        assert len(values) > 1
        self.values:list = values
        
    def is_define(self) -> bool:
        return all(i.is_define() for i in self.values)
    
    def calc_numeric_value(self) -> Number:
        assert self.is_define()
        accum = 1
        for i in self.values:
            accum *= i.calc_numeric_value()
        return accum
        
        
class Logarithm(MathFunc):
    def __init__(self, base:MathFunc, body:MathFunc):
        self.base = base
        self.body = body
    def is_define(self) -> bool:
        return self.base.is_define() and self.body.is_define()


class Sin(MathFunc):
    def __init__(self, value:MathFunc):
        self.value:MathFunc = value
    def is_define(self) -> bool:
        return self.value.is_define()