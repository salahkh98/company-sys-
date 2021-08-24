class Person:

    def __init__(self , id , name , phone , gender):

        self.id = id
        self.name = name
        self.phone = phone
        self.gender = gender



class Client(Person):

    def __init__(self, id, name, phone, gender , email):
        super().__init__(id, name, phone, gender)
        self.email = email



class Employee(Person):
    def __init__(self, id, name, phone, gender , salary , working_time):
        super().__init__(id, name, phone, gender)
        self.salary = salary
        self.working_time = working_time


