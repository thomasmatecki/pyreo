from pyreo.decorators import pipelined
from pyreo.redis_object import ReObject


class Foo(ReObject):
    s = "bar"

    def __init__(self) -> None:
        self.bar = "baz"
        self.i = 1

    @pipelined
    def roo(self):
        self.bar = "bar"
        self.baz = "foo"


def test_new():
    f0 = Foo()

    assert 1 == 1


def test_call():
    f0 = Foo()

    f0.roo()

    yaz = f0.baz


def test_incr():
    f0 = Foo()
    f0.i += 3
