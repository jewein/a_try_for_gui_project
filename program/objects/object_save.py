import dill

# 创建一个示例对象
class ExampleClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print("Data:", self.data)

obj = ExampleClass("Hello, world!")

# 将对象保存到文件
with open("serialized_object.xyz", "wb") as file:
    dill.dump(obj, file)

print("Object has been serialized and saved.")
