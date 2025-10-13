"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

def _relations_obj(person):
    return person.get("relations") or {}

def _relation_count(person):
    return len(_relations_obj(person))

def _has_friend(person):
    # for r in _relations_obj(person).values():
    #     if r == "friend":
    #         return True
    # return False
    return len([r for r in _relations_obj(person).values() if r == "friend"]) > 0

def max_age(group_dict):
    return max(p.get("age", 0) for p in group_dict.values())

def average_age_relations(group_dict):
    total_age = 0
    count = 0
    for p in group_dict.values():
        if len(p.get("relations")) > 0:
            total_age += p.get("age", 0)
            count += 1

    if total_age == 0:
        return 0
    return total_age / count

def max_age_with_relation(group_dict):
    return max((p.get("age", 0) for p in group_dict.values() if _relation_count(p) > 0), default=0)

def average_age_with_friend(group_dict):
    total_age = 0
    count = 0
    for p in group_dict.values():
        if len(p.get("relations")) > 0 and _has_friend(p):
            total_age += p.get("age", 0)
            count += 1

    if total_age == 0:
        return 0
    return total_age / count

def max_age_with_friend(group_dict):
    return max((p.get("age", 0) for p in group_dict.values() if _has_friend(p)), default=0)

if __name__ == "__main__":
    print("maximum age:", max_age(group))
    print("maximum age of relations:", max_age_with_relation(group))
    print("maximum age (has at least one friend):", max_age_with_friend(group))