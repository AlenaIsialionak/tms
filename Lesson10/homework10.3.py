class Person1:
    person = 'Sophia'

    @classmethod
    def get_person_name(cls, name):
        if cls.person == name:
            print(f'Attribute {cls.person} found in Instance Class: {Person1.__name__}')
        else:
            Person2.get_person_name(name)


class Person2:
    person = 'Amy'

    @classmethod
    def get_person_name(cls, name):
        if cls.person == name:
            print(f'Attribute {cls.person} found in Instance Class: {Person2.__name__}')
        else:
            Person3.get_person_name(name)


class Person3:
    person = 'Olivia'

    @classmethod
    def get_person_name(cls, name):
        if cls.person == name:
            print(f'Attribute {cls.person} found in Instance Class: {Person3.__name__}')
        else:
            raise AttributeError


class Child(Person1, Person2, Person3):
    person = 'Ruby'

    def __init__(self, name='Ruby'):
        self.person = 'Ruby'
        self.name = {'name': name}

    def __getitem__(self, item):
        return self.name[item]

    def __setitem__(self, item, value):
        self.name[item] = value

    def get_person_name(self, name):
        if name == self.person:
            print(f'Attribute {self.person} found in Instance Class: {Child.__name__}')
        else:
            print(name)
            Person1.get_person_name(name)


# print(Person3.__dict__)
p = Child()
p['name'] = 'Helen'
print(p['name'])
# p.get_person_name('Olivia')
mro = p.__class__.mro()
print(mro)
print("'param' value is " + p.person)
assert p.person == "Ruby"

del p.person
print("'param' value is " + p.person)
assert p.person == p.__class__.person

del p.__class__.person
first_parent = mro[1]
print(f"First parent is {first_parent}")
print("'param' value is " + p.person)
assert p.person == first_parent.person

del first_parent.person
second_parent = mro[2]
print(f"Second parent is {second_parent}")
print("'param' value is " + p.person)
assert p.person == second_parent.person
