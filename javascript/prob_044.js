#!/usr/local/bin/node

var _ = require('./underscore');

function checkPentagonal(x) {
    var n = (Math.sqrt(24 * x + 1) + 1) / 6;
    return n == Math.round(n);
}

function getPentagonal(x) {
    return x * (3*x - 1) / 2;
}

var notFound = true;
var k = 0;
while (notFound)
{
    ++k;
    for (var j = k - 1; j > 0; j--)
    {
	a = getPentagonal(j);
	b = getPentagonal(k);
	//console.log("j = " + j);
	if (checkPentagonal(b + a) && checkPentagonal(b - a)) {
	    console.log(j + ", " + k + ", " + Math.abs(b - a));
	    notFound = false;
	    break;
	}
    }
}
