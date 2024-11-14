// 15. Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor con un método para describir el motor.

class Engine {
  constructor(type, horsepower, cylinders) {
    this.type = type;
    this.hp = horsepower;
    this.c = cylinders;
  }

  describe() {
    console.log(
      `Engine type: ${this.type}\nHorsepower: ${this.hp}\nCylinders: ${this.c}`
    );
  }
}

class Car {
  constructor(make, model, year, engineType, engineHp, engineC) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.engine = new Engine(engineType, engineHp, engineC);
  }

  describeCar() {
    console.log(
      `My car is a ${this.year} ${this.make} ${this.model}. Below are the engine specs.`
    );
  }

  describeEngine() {
    this.engine.describe();
  }
}

let car = new Car("Kia", "Optima", 2020, "Inline 4-cylinder", 185, 4);

car.describeCar();
car.describeEngine();
