"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [{}, {}, {}, {}]  # Replace with actual dictionaries representing acquaintances
my_group[0] = {
    "name": "Jill",
    "age": 26,
    "job": "biologist",
    "relations": {"friend" : ["Zalika"], "partner" : ["John"]}
}
my_group[1] = {
    "name": "Zalika",
    "age": 28,
    "job": "artist",
    "relations": {
        "friend": ["Jill"],
        "landlord": ["Nash"]
    }
}
my_group[2] = {
    "name": "John",
    "age": 27,
    "job": "writer",
    "relations": {
        "partner": ["Jill"],
        "cousin": ["Nash"]
    }
}
my_group[3] = {
    "name": "Nash",
    "age": 34,
    "job": "chef",
    "relations": {
        "cousin": ["John"],
        "tenant": ["Zalika"]
    }
}

def _find_person(Name):
    for person in my_group:
        if person.get("name") == Name:
            return person
    return None

def forget(person1, person2):
    p1 = _find_person(person1)
    p2 = _find_person(person2)
    if not p1 or not p2:
        return False
    
    removed = False
    for relation, names in p1["relations"].items():
        if person2 in names:
            names.remove(person2)
            removed = True
            if not names:
                del p1["relations"][relation]
            break

    for relation, names in p2["relations"].items():
        if person1 in names:
            names.remove(person1)
            removed = True
            if not names:
                del p2["relations"][relation]
            break

    return removed

def add_person(name, age, job, **relations):
    if _find_person(name):
        return False  # Person already exists

    new_person = {
        "name": name,
        "age": age,
        "job": job,
        "relations": relations
    }
    my_group.append(new_person)
    return True

def average_age():
    if not my_group:
        return 0
    
    total_age = sum(person["age"] for person in my_group)
    return total_age / len(my_group)