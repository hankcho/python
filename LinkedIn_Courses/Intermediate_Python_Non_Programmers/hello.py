import random

# class Dog:
#     info = "A furry little creature like MoHawk"

#     def __init__(self, name):
#         print("I'm alive")
#         self.lucky_number = random.randint(1,10)
#         self.name = name


# # print(Dog.info)


# dog1 = Dog()
# dog2 = Dog()


# print(dog1.lucky_number)
# print(dog2.lucky_number)


# dog1.name = "Fido"

# print(dog1.name)


class Guitar:
    info = "6 string musical instrument"
    # type = "acoustic or electric"

    def __init__(self, type, cost):
        self.type = type
        self.cost = cost

guitar1 = Guitar("electric", "$299.00")
guitar2 = Guitar("acoustic", "$199.00")

# print(Guitar.info, ";" , Guitar.type)
print(Guitar.info)
print(guitar1.type, guitar1.cost)
print(guitar2.type, guitar2.cost)
