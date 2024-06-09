data_base1 = [{'id': 1, 'name': 'Kate', 'age': 23, 'job_id': 1},
             {'id': 2, 'name': 'Jerry', 'age': 31, 'job_id': 3},
             {'id': 3, 'name': 'Tom', 'age': 23, 'job_id': 1},
             {'id': 4, 'name': 'Ann', 'age': 21},
             {'id': 5, 'name': 'Mark', 'age': 33, 'job_id': 2},
             {'id': 6, 'name': 'Helena', 'age': 29}
             ]
data_job1 = [{'id': 1, 'job': 'doctor'},
            {'id': 2, 'job': 'engineer'},
            {'id': 3, 'job': 'programmer'},
            {'id': 4, 'job': 'designer'}
            ]
NAME1 = 'data_job1'


def checkout_keys(data_base, data_job, name):
    common = {i for j in data_base for i in j.keys()}&{i for j in data_job for i in j.keys()}
    for i in common:
        for j in data_job:
            elem = j.get(i)
            del j[i]
            j[i + "_" + name] = elem
    return data_job


def inner_join(data_base: dict, data_job: dict):
    checkout_keys(data_base, data_job, NAME1)
    new_date = []
    for i in data_base:
        for j in data_job:
            if i.get('job_id') == j.get('id_data_job1'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)

    return new_date


for i in inner_join(data_base1, data_job1):
    print(i)

print(30*'*')


def left_outer_join(data_base: dict, data_job: dict):
    checkout_keys(data_base, data_job, NAME1)
    new_date = []
    for i in data_base:
        count = 0
        for j in data_job:
            if i.get('job_id') == j.get('id_data_job1'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)
                break
            count += 1
            if count == len(data_job):
                keys = [key for key in j.keys()]
                data_join = dict([(key, None) for key in keys] + list(j.items()))
                data_join = dict(list(i.items()) + [(key, None) for key in keys])
                new_date.append(data_join)

    return new_date


for i in left_outer_join(data_base1, data_job1):
    print(i)

print(31*'*')


def right_outer_join(data_base: dict, data_job: dict):
    checkout_keys(data_base, data_job, NAME1)
    new_date = []
    for j in data_job:
        count = 0
        for i in data_base:
            if i.get('job_id') == j.get('id_data_job1'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)
                break
            count += 1
            if count == len(data_base):
                keys = [key for key in i.keys()]
                data_join = dict([(key, None) for key in keys] + list(j.items()))
                new_date.append(data_join)
                break

    return new_date

for i in right_outer_join(data_base1, data_job1):
    print(i)
