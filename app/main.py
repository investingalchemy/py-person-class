class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    person_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        person = Person.people[name]

        person_list.append(person)

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

    return person_list
