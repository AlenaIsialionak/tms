class VerifyRange(Exception):

    def __init__(self):
        self.message = 'Value must belong to the range [1;1000]'
        super().__init__(self.message)

    def __str__(self):
        return f" The value doesn't belong to the specified range. You need to check your value."


value = int(input())
try:
    if not 1 <= value <= 1000:
        raise VerifyRange
except VerifyRange as err:
    print(err)
else:
    print('The check was successful')

