from typing import Dict, List
from typing_inspect import is_generic_type


FIELD = "field"

t = Dict
t3 = List[str]

test1 = 3
test2 = {
    FIELD: "value"
}
test3 = [
    "a",
    "b"
]

print(isinstance(test2, t))
print(isinstance(test3, t3))
