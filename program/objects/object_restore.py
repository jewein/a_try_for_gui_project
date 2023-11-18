import dill

# 从文件中加载对象
with open("serialized_object.xyz", "rb") as file:
    loaded_obj = dill.load(file)

# 调用对象的方法
loaded_obj.display()





