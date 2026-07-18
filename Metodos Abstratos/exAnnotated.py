from dataclasses import dataclass
from typing import Annotated, get_type_hints


@dataclass
class ValueRange:
    lo: int
    hi: int


T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]


@dataclass
class ctype:
    kind: str


a1 = Annotated[int, ValueRange(3, 10), ctype("char")]
a2 = Annotated[int, ctype("char"), ValueRange(3, 10)]

assert a1 != a2  # a ordem importa


@dataclass
class MaxLen:
    value: int


type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]

# Quando usado em uma anotação de tipo, um verificador de tipos tratará "V" da mesma forma que
# ``Annotated[list[tuple[int, int]], MaxLen(10)]``:
type V = Vec[int]


def func(x: Annotated[int, "metadata"]) -> None:
    pass


print(get_type_hints(func))

print(get_type_hints(func, include_extras=True))
