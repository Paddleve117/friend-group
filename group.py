"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [{}, {}, {}, {}]  # Replace with actual dictionaries representing acquaintances
my_group[0] = {
    "name": "Jill",
    "age": 26,
    "job": "biologist",
    "friends": {"friend" : ["Zalika"], "partner" : ["John"]}
}
my_group[1] = {
    "name": "Zalika",
    "age": 28,
    "job": "artist",
    "friends": {
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

