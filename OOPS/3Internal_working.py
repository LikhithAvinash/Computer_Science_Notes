class working:
    def __init__(som):
        som.name = "Likhith"

obj = working() ## obj is created here itself
print(obj.name)

'''
1) object is created
2) class_name.__init__(object) = working.__init__(obj)
3) working.__init__(obj) --> som = obj
4) obj.name = "Likhith' -->Printed

'''