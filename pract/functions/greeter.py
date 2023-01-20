# --------------------------------------
# alt 1
# --------------------------------------
# def welcome(friend):

#     print(f"hello {friend} wecome to zortan")
# def main():
#     friends:list=["one","two","three","four"]
#     for friend in friends:
#         welcome(friend)


# main()


# --------------------------------------
# alt 2
# --------------------------------------

def welcome(friend: str) -> str:
    return f"hello {friend} how are you"

def main() -> None:
    friends=["one","two","three","four"]
    for friend in friends:
        if "four" in welcome(friend):
            print(f"{welcome(friend)} u are also cute")
        else:
            print(welcome(friend))
main()

