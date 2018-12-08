test = {
    "value": "blabla",
    "synonyms": [
        "coucou",
        "delamerde",
        "caca"
    ]
}

try:
    a = test["truc"]
    print(a)
except KeyError:
    print("oups")

