class obj(object):
    def __init__(self, d):
        for x, y in d.items():
            setattr(self, x, obj(y) if isinstance(y, dict) else y)
data = {'a':1,'b':{'c':9}}
ob = obj(data)
print(ob)