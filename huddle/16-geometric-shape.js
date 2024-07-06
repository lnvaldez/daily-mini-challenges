/*
16. Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro.
Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.
*/

class GeometricShape {
  constructor(shape) {
    this.shape = shape;
  }

  calculatePerimeter() {
    return 0;
  }

  calculateArea() {
    return 0;
  }
}

class Rectangle extends GeometricShape {
  constructor(shape, length, width) {
    super(shape);
    this.l = length;
    this.w = width;
  }

  calculatePerimeter() {
    let p = 2 * (this.l + this.w);
    return p;
  }

  calculateArea() {
    let a = this.l * this.w;
    return a;
  }
}

class Circle extends GeometricShape {
  constructor(shape, radius) {
    super(shape);
    this.r = radius;
    this.pi = Math.PI;
  }

  calculatePerimeter() {
    let p = 2 * this.pi * this.r;
    return p;
  }

  calculateArea() {
    let a = this.pi * Math.pow(this.r, 2); // Fixed: this.pi instead of pi
    return a;
  }
}

let rectangle = new Rectangle("Rectangle", 5, 10);
let circle = new Circle("Circle", 3);

console.log(`++${rectangle.shape}++`);
console.log(`Perimeter:`, rectangle.calculatePerimeter());
console.log(`Area:`, rectangle.calculateArea());

console.log(`\n++${circle.shape}++`);
console.log(`Perimeter:`, circle.calculatePerimeter());
console.log(`Area:`, circle.calculateArea());
