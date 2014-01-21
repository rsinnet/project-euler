#!/usr/local/bin/node

// Project Euler
// Problem 95
// Amicable chains

var _ = require('./underscore');

var maxChain = 0;
var maxList = [];
const N = 1000000;

for (var j = 2; j <= N; j++) {
    var amilist = [j];

    if (j % 1000 == 0)
	console.log(j);

    while (true)
    {
	var foo = _.reduce(getFactors(_.last(amilist)),
			   function(x, y) { return y + x; });
	if (foo > 1000000)
	    break;

	if (_.contains(amilist, foo)) {
	    if (amilist.length > maxChain) {
		console.log(maxChain);
		maxChain = amilist.length;
		maxList = amilist;
	    }
	    break;
	}
	amilist.push(foo);
    }
}

console.log("Answer: " + _.min(maxList) + ",  " + maxChain);

function getFactors(x) {
    var factor_list = [];
    _.each(_.range(1, x/2+1, 1), function(y) {
	if (x % y == 0)
	    factor_list.push(y);
    });
    return factor_list;
}
