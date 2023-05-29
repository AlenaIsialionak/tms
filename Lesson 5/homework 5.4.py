import datetime
TODAY = datetime.datetime.now()


def time(delt):
    return (TODAY - datetime.timedelta(seconds=delt)).strftime('%Y-%m-%d %H:%M:%S')


print([time(i) for i in range(int(input('enter an integer of elements: ')))])
