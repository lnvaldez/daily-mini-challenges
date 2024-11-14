const dice = ["1", "2", "3", "4", "5", "6"];

const random = Math.floor(Math.random() * dice.length);
console.log(`You rolled a ${dice[random]}`);
