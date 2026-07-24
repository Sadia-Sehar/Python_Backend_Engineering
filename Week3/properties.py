# class Temperature:
#     def __init__(self,c):
#         self.celsius=c
#     @property
#     def fahrenheit(self):
#         return self.celsius*9/5+32
# t=Temperature(20)
# print(t.fahrenheit)

# class Temperature:
#     def __init__(self,value):
#             self.celsius=value # use the propery, not the internal variable
#     @property #getter-read-only
#     def celsius(self):
#         return self._celsius # Read the iternal variable
#     @celsius.setter
#     def celsius(self,value):
#          if value<-273.15:
#               raise ValueError("Impossible temperature")
#          self._celsius=value # store in the internal variable
#     @celsius.deleter
#     def celsius(self):
#          print("Deleting Temperature")
#          del self._celsius    
# t=Temperature(-200)
# print(t.celsius)
# # t.celsius=-300
# # print(t.celsius)
# del t.celsius
# # t.age=21
# # A Python object's attributes are stored in a dictionary called  __dict__
# print(t.__dict__)