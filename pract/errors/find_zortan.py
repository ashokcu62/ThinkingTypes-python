def find_rathi(name: str) -> None:
    friends = ["ramu", "somu", "raju", "jeenu", "rathi"]
    if name not in friends:
        raise ValueError(f"{name} not found")
    else:
        print(f" Found {name}")


find_rathi("somu")
find_rathi("vi")



                # errverson
# def find_rathi(name: str) -> None:
#     friends = ["ramu", "somu", "raju", "jeenu", "rathi"]
#     try:
#         assert name in friends
#     except AssertionError:
#         print(f"{name} not found")
#     else:
#         print(f"{name}  found in the freind list")
#     finally:
#         print(f"good bye   {name}")
