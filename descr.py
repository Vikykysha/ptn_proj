class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value
    
    @staticmethod
    def _prepare_value(value, com):
        return int(value * (1 - com))

    def __set__(self, obj, value):
        self.value = self._prepare_value(value, obj.commission)

'''Для проверки
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)
'''

