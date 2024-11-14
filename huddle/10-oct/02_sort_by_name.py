class Person():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

p1 = Person("Lucas", "Valdez")
p2 = Person("Trinidad", "Rojas")
p3 = Person("Cynthia", "Funes")
p4 = Person("Elias", "Vera")
p5 = Person("Olaf", "Pedersen")

obj_array = [p1, p2, p3 , p4, p5]
sorted_array = []

for p in obj_array:
    sorted_array.append(p.lastname)

sorted_array = sorted(sorted_array)

print(sorted_array)