from functools import wraps
from typing import Any


def pipelined(func):
    @wraps(func)
    def inner(instance, *args: Any, **kwargs: Any) -> Any:

        from pyreo.transactional import ReObjectTransaction

        with ReObjectTransaction(instance._rdict_):
            return func(instance, *args, **kwargs)

    return inner