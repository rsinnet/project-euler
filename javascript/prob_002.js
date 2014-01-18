#!/usr/local/bin/node

var _ = require('./underscore');
var fib1 = 1;
var fib2 = 2;

var cSum = 2;

while ( true )
{
    var foo = fib1 + fib2;

    if (foo >= 4000000)
	break;

    fib1 = fib2;
    fib2 = foo;

    if (foo % 2 == 0)
	cSum += foo;
}

console.log(cSum);
