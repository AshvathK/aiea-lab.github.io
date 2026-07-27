facts = {
    ("parent", "john", "mary"),
    ("parent", "mary", "bob"),
    ("parent", "bob", "alice"),
    ("male", "john"),
    ("female", "mary"),
}


def is_parent(parent, child):
    return ("parent", parent, child) in facts


def is_grandparent(grandparent, grandchild):
    for fact in facts:
        if fact[0] == "parent" and fact[1] == grandparent:
            middle_person = fact[2]

            if is_parent(middle_person, grandchild):
                return True

    return False


def is_father(father, child):
    return (
        is_parent(father, child)
        and ("male", father) in facts
    )


def is_mother(mother, child):
    return (
        is_parent(mother, child)
        and ("female", mother) in facts
    )


print("Logical Inference Results")
print("-------------------------")

print("Parent(john, mary):", is_parent("john", "mary"))
print("Grandparent(john, bob):", is_grandparent("john", "bob"))
print("Grandparent(mary, alice):", is_grandparent("mary", "alice"))
print("Father(john, mary):", is_father("john", "mary"))
print("Mother(mary, bob):", is_mother("mary", "bob"))
print("Grandparent(john, alice):", is_grandparent("john", "alice"))
