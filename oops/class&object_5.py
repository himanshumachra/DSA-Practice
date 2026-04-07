class car:
    color = "black"
    def __init__(self, brand):
        self.brand = brand

class model(car):
    model = 2026
    def __init__(self, brand, features):
        super().__init__(brand)
        self.features = features

class showroom(model):
    totalcarsinshowroom = 30
    def __init__(self, brand, features, clntname):
        super().__init__(brand, features)
        self.clntname = clntname

c1 = showroom("Hyundai", "Sunroof", "Anuj")
print(c1.features)
