#!/usr/local/bin/node

// Project Euler
// Problem 92
// Square digit chains

var _ = require('./underscore');

function sdc(x)
{
    return _.reduce(x.toString(), function(memo, num) { return memo + Math.pow(num,2); }, 0)
}


var count = 0;
for (var y = 1; y < 10000000; y++)
{
    if (y % 100000 == 0)
	console.log(y);
    x = y;
    while (true)
    {
	x = sdc(x);
	if (x == 89)
	    count++;

	if (x == 89 || x == 1)
	    break;
    }
}

console.log(count);