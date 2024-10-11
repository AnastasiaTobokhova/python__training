class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(f'Этаж {new_floor}')
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название: {self.name}\nколичество этажей: {self.number_of_floors}')



h1 = House('ЖК Эльбрус',30)
print(h1.name, h1.number_of_floors)

h1.go_to(2)
h1.go_to(35)

print(len(h1))
print(str(h1))


