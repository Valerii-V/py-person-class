class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = [Person(p["name"], p["age"]) for p in people]
    for person_dict in people:
        real_person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            real_person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            real_person.husband = Person.people[person_dict["husband"]]
    return person_objects
