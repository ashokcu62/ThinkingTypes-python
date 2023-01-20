def divider(x:int,y:int):
    try:
        num=x/y
       
    except ZeroDivisionError:
        print("Cant divide  by zero ! use some other number")
    except TypeError:
        print("Both x and y is to be numbers")
    # dont know which error is comming so tacking exception class 
    except Exception as E:
        print(f"Oops Something went wrong {E}")
    else:
        print("Else is executed only when try succeeds")
        print(num)
    finally:
        print("finally always executes  irrespective of success or exception")

divider(20,10)
divider(30,0)