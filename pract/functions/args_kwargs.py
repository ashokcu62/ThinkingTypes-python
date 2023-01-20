# -----------------unpacking-----------
from typing import Any
fname, lname = ("meena", "teena")
print(f"{type(fname)} {fname} {lname}")

# in a big tupple

one, *rest = ("one", "two", "three", "four", "five")
print(one)
print(f"{rest}")

# dic
jj = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
all = {"hundred": 100, **jj}
print(rest)
print(f" dic {all}")


# -----------Varibale argument
def unknownArgument(*args: str):
    for name in args:
        print(f"unknown arguments{type(name)}")


unknownArgument("jani", "jaanu", "meenu", "teena")  # unlimited argument case

# ----------------------------keyword--Argument----------------------
# keyword arguments
#  **arg   varriable keyword argument  its have a form of  dic


def unwnargs(**args: Any) -> None:
    for k, v in args.items():
        print(k, " : ", v)


# jj = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

unwnargs(one=1, two=2, three=3, four=4, five=5)

# ------------togather------------


# ----------------------------------------------
                # perfect sort
# ----------------------------------------------

def togather_args(d: dict[str, int | str], *arg, **kwargs):
    print(d)
    print(arg)
    print(type(kwargs))

    for x in arg:
            print(f" for list like args{x}")
    for k, v in kwargs.items():
            print(f" kyargs{k} :: {v}")

togather_args({"one":1,"dic":3,"john":"lopz"},"ramu","somu","rajan","dasan","viji",subin=10,ratheesh=6,saju=40,vipin=5)