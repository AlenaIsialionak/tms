from datetime import datetime


def dec_time(func):
    def wrapper(*args, **kwargs):
        st_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        delta = (end_time - st_time).total_seconds()*10**3
        print(f'{delta} ms is function operation time')
    return wrapper


@dec_time
def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


print(f'For function matrix: ')
matrix(500, 500, 9)


@dec_time
def simple_number(num):
    str_ = [i for i in range(1, num//2+1) if num % i == 0] + [num]
#    print(str_)
    if len(str_) == 2:
        return True
    return False


print(f'For function simple_number: ')
simple_number(111111)
