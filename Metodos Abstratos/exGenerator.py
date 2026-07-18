from typing import Generator


def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return "Done"


generator = echo_round()
print(next(generator))
print(generator.send(3.7))
print(generator.send(8.2))
print(generator.send(1.5))

try:
    generator.send(-1)
except StopIteration as error:
    print(error.value)
