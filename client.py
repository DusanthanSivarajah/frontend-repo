class client:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = client("John", 36)
print(p1.name, p1.age)