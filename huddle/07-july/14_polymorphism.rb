'''
14. Polimorfismo: Crea una clase base Animal con un método hacerSonido y 
una clase derivada Perro que sobrescriba este método.
'''

class Animal
    def initialize
      @animal = "Animal"
      @sound = "Hey"
    end
  
    def make_sound
      puts "The #{@animal} makes the sound #{@sound}"
    end
end
  
class Dog < Animal
    def initialize
      super  
      @animal = "Dog"
      @sound = "Woof!"
    end
end
  
animal = Animal.new
animal.make_sound  

dog = Dog.new
dog.make_sound  
