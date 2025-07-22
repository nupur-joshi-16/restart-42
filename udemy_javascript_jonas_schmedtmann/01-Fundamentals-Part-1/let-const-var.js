const currentYear = 2037;
const ageJonas = currentYear - 1991;
const ageSarah = currentYear - 2018;
console.log(ageJonas, ageSarah); // we can add multiple values using comma)

const firstName = "Nupur";
const lastName = "J.";
console.log(firstName + " " + lastName);

// typeof also operator

let x = 10 + 5;
x += 10; // x = x + 10 = 25
x *= 4; // 100
x++; // x = x + 1
console.log(x);
x--;

// comparison operator
console.log(ageJonas > ageSarah);

// Operator precedance
console.log(currentYear - 1991 > currentYear - 2018);
