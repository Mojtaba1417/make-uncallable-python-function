
class MakeUncallable:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwds) :
        return self.func()

def make_uncallable(func):
    def inner():
        a = MakeUncallable(func)
        return a()
    return inner()
@make_uncallable
def hello():
    return f"Hello Hello"

print(hello)