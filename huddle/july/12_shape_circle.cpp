/*
12. Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase 
derivada Círculo que extienda Figura y sobreescriba el método imprimir.
*/

#include <iostream>

class Shape{
	public:
		int x, y;
		std::string color;
		
	Shape(int x, int y, std::string color) : x(x), y(y), color(color){}
	
	virtual void print() const {
		std::cout << "Shape at (" << x << ", " << y << ") with a " << color << " color." << std::endl;
	}
	
	virtual ~Shape() {}
};

class Circle : public Shape{
	public:
		float radius;
		
	Circle(int x, int y, std::string color, float radius) : Shape(x, y, color), radius(radius) {}
	
	void print() const override {
		std::cout << "Circle at (" << x << ", " << y << ") with a " << color 
		<< " color and " << radius << "cm radius." << std::endl;
	}
};

int main(){
	Shape shape(3, 3, "red");
	Circle circle(5, 5, "blue", 15.8);
	
	shape.print();
	circle.print();
	
	return 0;
}