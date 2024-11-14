# 11. Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas.

class Point
    def initialize(x, y)
        @x = x 
        @y = y 
    end
    def print_point()
        puts "x = #{@x}, y = #{@y}"
    end 
end 

point = Point.new(5, 5)
point.print_point