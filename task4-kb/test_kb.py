from pathlib import Path
from pyswip import Prolog


def main() -> None:
    prolog = Prolog()

    kb_path = Path(__file__).with_name("family.pl")
    prolog.consult(str(kb_path))

    tests = [
        ("Is John David's grandparent?", "grandparent(john, david)"),
        ("Who are Kevin's grandparents?", "grandparent(X, kevin)"),
        ("Are Mike and Lisa siblings?", "sibling(mike, lisa)"),
        ("Who are Emma's parents?", "parent(X, emma)"),
    ]

    for description, query in tests:
        results = list(prolog.query(query))
        print(description)
        print(f"Query: {query}")
        print(f"Results: {results}")
        print("-" * 40)


if __name__ == "__main__":
    main()
