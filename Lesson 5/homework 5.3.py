from random import randrange


def count(sp: list):
    print('List:', sp)
    result = {}
    for i in sp:
        result[i] = result.get(i, 0) + 1
    return result


print(f'Result: {count([randrange(0,10) for _ in range( int(input(" enter an integer of elem the list will make up: ")))])} ')
