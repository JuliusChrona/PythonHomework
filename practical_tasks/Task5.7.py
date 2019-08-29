class Human(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Citizen(Human):
    country_name = 'Belarus'

    def __init__(self, age, name):
        super().__init__(age, name)

    @classmethod
    def change_country_name(cls, country_name):
        cls.country_name = country_name

    @classmethod
    def create_citizen_from_human(cls):
        return Citizen(cls.age, cls.name)

    @staticmethod
    def calculate_average_age_of_given_citizens(list_of_citizens):
        total_age = sum([citizen.age for citizen in list_of_citizens])
        return total_age / len(list_of_citizens)


inst_g = Citizen(24, "Gennady")
inst_d = Citizen(25, "Dmitry")
print(inst_g.country_name)
print(inst_d.country_name)
inst_g.country_name = "Russia"
print(inst_g.country_name)
print(inst_d.country_name)
Citizen.change_country_name("USA")
print(inst_g.country_name)
print(inst_d.country_name)
print(Citizen.calculate_average_age_of_given_citizens([inst_d, inst_g]))
