# 创建一个变量名字符串
variable_name = "my_variable"

# 创建一个值
variable_value = 42

# 使用globals()函数创建一个全局变量
globals()[variable_name] = variable_value

# 现在可以直接访问变量名my_variable
print(my_variable)  # 输出: 42
