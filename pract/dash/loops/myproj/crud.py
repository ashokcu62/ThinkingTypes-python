WELCOME="""
WELCOME TO CRUD APP
--------------------
CHO0SEE 
1: TO CONTINUE WITH CRUD APP
2:EXIT FROM THE PROGRAM
"""
END="""
THANK YOU FOR USING MY APP
GOOD BYE !!!!!!
"""

OPTIONS="""
------------------------------------------------
1 : READ FILE
2 : EDIT FILE
4 : UPDATE FILE
5 : DELETE FILE
------------------------------------------------

"""




def read(data):
    if len(data)!=0:
        for x in data:
             print(x)
        return
    print("nothing in this list")

l1:tuple[str,str,str]=["maths","science","eng"]
l2=[]
read(l2)