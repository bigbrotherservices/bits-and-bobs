// Our first solution to Fizz Buzz
for (var i = 1; <= 100; i++) {
  if ((i%3 == 0) && (i%5 != 0) ) {
  console.log('Fizz');
 }
 if ((i%3 != 0) && (i%5 == 0) ) {
  console.log('Buzz');
 } 
 if ((i%3 == 0) && (i%5 == 0) ) {
  console.log('FizzBuzz');
 }
 if ((i%3 != 0) && (i%5 != 0) ) {
  console.log(i);
 }
}
