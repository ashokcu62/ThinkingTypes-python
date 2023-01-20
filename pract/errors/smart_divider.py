def smart_divider(x:int,y:int):
    try:
        num=x/y
        print(num)
    except ZeroDivisionError:
        print("Cand divide  by zero ! use some other number")
    except TypeError:
        print("Both x and y is to be numbers")
    # dont know which error is comming so tacking exception class 
    except Exception as E:
        print(f"Oops Something went wrong {E}")


#testing 

#1
# smart_divider(50,20)
# #2
# smart_divider(0,20)
# #3 worked
smart_divider(20,0)
smart_divider("a",41)

smart_divider("a","b")


