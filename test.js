// test mean
var mean = require('./stats').mean;
var m = [1,3,5,6,843,2324,62];
console.log('mean    '+mean(m,4));

// test median
var median = require('./stats').median;
var n = [3,5,7,9,11]; // -> 4,6,33,111
console.log('median  '+median(n));

// test mode
var mode = require('./stats').mode;
var l = [3,1,3,7,102,55,32,32,102];
var j = [1,2,3,4,5];
console.log('n modes '+JSON.stringify(mode(l)));
console.log('0 modes '+mode(j));
