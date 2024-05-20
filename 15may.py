# # объявление класса
# class FirstClass:
#     firs_var = 1
#     "Мой первый класс"
#     def init(self):
#         print(self)
#         pass
#     pass
# #print(FirstClass.firs_var)
# # способ создания экземпляра класса (объекта)
# first_expl = FirstClass()
# #print(first_expl.dict)
# #first_expl.color = 'red'
# #print(first_expl.color)
# second_expl = FirstClass()
# #second_expl.color = 'black'
# #print(second_expl.color)
# print(first_expl, first_expl.init)

# class Cats:
#     def init(self):
#         self.name = input('Введите имя котёнка')
#         self.age = input('Введите возраст')
# my_cat = Cats()
# print(my_cat.name)
# print(Cats.dict)

class Geo:
    child = 2
    def __init__(self):
        self.corn = input()
tr = Geo()
print(tr.__dict__, Geo.__dict__)