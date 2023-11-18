class BaseClass:
    def __init__(self):
        print("BaseClass constructor")

    def __del__(self):
        print("BaseClass destructor")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("DerivedClass constructor")

    def __del__(self):
        print("DerivedClass destructor")

# 创建派生类对象
obj = DerivedClass()
# 输出：
# BaseClass constructor
# DerivedClass constructor

del obj
# 输出：
# DerivedClass destructor
# BaseClass destructor
