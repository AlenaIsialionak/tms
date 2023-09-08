data_base1 = [{'id': 1, 'name': 'Kate', 'age': 23, 'job_id': 1},
             {'id': 2, 'name': 'Jerry', 'age': 31, 'job_id': 3},
             {'id': 3, 'name': 'Tom', 'age': 23, 'job_id': 1},
             {'id': 4, 'name': 'Ann', 'age': 21},
             {'id': 5, 'name': 'Mark', 'age': 33, 'job_id': 2},
             {'id': 6, 'name': 'Helena', 'age': 29}
             ]
data_job1 = [{'id_': 1, 'job': 'doctor'},
            {'id_': 2, 'job': 'engineer'},
            {'id_': 3, 'job': 'programmer'},
            {'id_': 4, 'job': 'designer'}
            ]


def inner_join(data_base: dict, data_job: dict):
    new_date = []
    for i in data_base:
        for j in data_job:
            if i.get('job_id') == j.get('id_'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)

    return new_date


for i in inner_join(data_base1, data_job1):
    print(i)

print(30*'*')


def left_outer_join(data_base: dict, data_job: dict):
    count = 0
    new_date = []
    for i in data_base:
        for j in data_job:
            if i.get('job_id') == j.get('id_'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)
                break

            count += 1
            if count == len(data_job):
                data_join = dict(list(i.items()) + [('job_id', None), ('id_', None), ('job', None)])
                new_date.append(data_join)
                count = 0

    return new_date


for i in left_outer_join(data_base1, data_job1):
    print(i)


print(31*'*')


def right_outer_join(data_base: dict, data_job: dict):
    count = 0
    new_date = []
    for j in data_job:
        for i in data_base:
            if i.get('job_id') == j.get('id_'):
                data_join = dict(list(i.items())+list(j.items()))
                new_date.append(data_join)
                break

            count += 1
            if count == len(data_base):
                data_join = dict([('id', None), ('name', None), ('age', 'None'), ('job_id', None)] + list(j.items()))
                new_date.append(data_join)
                count = 0
                break

    return new_date

for i in right_outer_join(data_base1, data_job1):
    print(i)