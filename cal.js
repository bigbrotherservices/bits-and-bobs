ar rs = require('readline-sync');

var numOne = rs.question('Please enter a number');
var numTwo = rs.question('Please enter anoter number');
var operator = rs.question('Please enter an operator');

var operation = numOne + operator + numTwo

var result = eval(operation);

console.log(result);
