

def find_value(sdict: dict, word: str, deep=0, parent=None):
    for key, current_value in sdict.items():
        parent = key
        if isinstance(current_value, dict):
            out = find_value(current_value, word, deep+1, parent)
            if out is not None:
                return out
        elif isinstance(current_value, list):
            for i in current_value:
                if isinstance(i, dict):
                    out = find_value(i, word, deep+1, parent)
                    if out is not None:
                        return out
                else:
                    if i == word:
                        return i, deep, parent
        else:
            if current_value == word:
                return current_value, deep, parent


def get_source_dict():
    return {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Ann',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark', 'Alex']  # deep 6
                                    }
                                ],
                                "key11": "Louisa",  # deep 5
                            }
                        },
                        "Alex",  # deep 3
                    ]
                },
            },
            'key12': 'Robert'  # deep 1
        },
        "key13": "Ronaldo"  # deep 0
    }


result = find_value(get_source_dict(), input('Enter a name: '))
if result:
    value, deep, parent = result
    print(f'Значение {value} найдено на глубине {deep}, {parent}')
else:
    print(f'Значение не найдено')

