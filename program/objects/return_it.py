import dill



# 反序列化对象
with open('my_object.pkl', 'rb') as file:
    Alice = dill.load(file)

Alice.show_friends()