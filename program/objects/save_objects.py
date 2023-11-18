import dill

class Person:
    def __init__(self,name):
        self.name=name
        self.friends=[]

    def __repr__(self):
        return 'Person({!r})'.format(self.name)

    def add_friend(self,friend):
        self.friends.append(friend)

    def show_friends(self):
        print(self.name+'\'s friends:',self.friends)


if __name__ == '__main__':
    # 创建一个变量名字符串
    names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl', 'Ginger', 'Holly', 'Iris', 'Jenny', 'Kevin', 'Linda', 'Mike',
             'Nina', 'Olive', 'Patty', 'Queen', 'Ruby', 'Sue', 'Tony', 'Vera', 'Will', 'Xavier', 'Yvonne', 'Zoey']
    # 创建一个空列表
    for name in names:
        locals()[name] = Person(name)

    Alice.add_friend(Beth)
    Alice.add_friend(Cecil)
    Alice.show_friends()
# 序列化对象
with open('my_object.pkl', 'wb') as file:
    dill.dump(Alice, file)


