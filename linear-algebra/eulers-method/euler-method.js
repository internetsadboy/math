// Euler's Method
// http://en.wikipedia.org/wiki/Euler_method
// user input: n, d, x, and poly 
// poly: dx/dt == f(t,x)
// n: # of steps 
// d: domain a <= t <= b
// x: initial value 
// h: step size
// t: the delta of current steps taken

var n = 4
var d = [0,2];
var x = 0.5;
var h = d[0]+d[1]/n; 
var t = 0;

function poly(x,t) {
  return x - Math.pow(t,2) + 1;
}

function EulersMethod() {
  for(var k = 0; k < n; k++) {
    t = k*h;
    x = h*poly(x,t)+x;
  } 
  return x;
}

<<<<<<< HEAD
console.log(EulersMethod()); // 4.4375
=======
EulersMethod(); // 4.4375
>>>>>>> a5dc3a37c9a875271f663cd24880858dc873e6d7
