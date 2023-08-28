class Toy:
    def __init__(self,color,name):
        self.color = color
        self.name = name
        self.dict = {"color":self.color,"name":self.name}

    def __getitem__(self, item):
        return self.dict[item]

toy = Toy(3,"dracula")
print(toy["name"])

class CustomList:

    def __init__(self):
        self.dict = dict()
        self.counter = -1

    def append(self, new_item):
        self.counter = self.counter+1
        self.dict[self.counter] = new_item

    def __getitem__(self, item):
        return str(self.dict[item])

    def __str__(self):
        print(self.dict)


myList = CustomList()
myList.append(3)
print(myList.dict)