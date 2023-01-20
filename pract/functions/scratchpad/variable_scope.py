num = 10


def print_glob_num():
    print(num)


def print_num():
    num = 20  # only inside that spec fn is local var
    print(f"my local number is {num}")


def incnum():
    #  to tell its global
    global num
    num += 1

def newnum():
    newnumber=num+10
    print(f"{newnumber}")

print_glob_num()

print_num()

print(num)
incnum()
print(num)
newnum()
