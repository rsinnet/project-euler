#!/usr/local/bin/node

// Project Euler
// Problem 74
// Digit factorial chains

var _ = require('./underscore');

function factorial(x)
{
    if (x == 0)
	return 1

    return _.reduce(_.range(1,x+1), function(memo, num) { return memo * num; }, 1);
}

function fSum(x) {
    return _.reduce(x.toString().split(""),
		    function(memo, num) { return memo + factorial(parseInt(num)); }, 0);
}

var count = 0;
var chains = {1: 1, 2: 1, 169: 3, 363601: 3, 1454: 3, 871: 2, 872: 2, 45361: 2, 45362:2, 145: 1};
_.each(_.range(1000000), function (x) {
    var seq = [];
    seq.push(x);
    console.log('----' + x + '----');
    while (true) {

	if (typeof(chains[_.last(seq)]) != 'undefined')
	    break;

	bar = fSum(_.last(seq));

	if (bar == _.last(seq))
	{
	    chains[bar] = 1;
	    break;
	}

	seq.push(bar);
    }

    var baz = chains[_.last(seq)];
    _.each(_.initial(seq), function(x, k) {
	chains[x] = (seq.length - k) + baz - 1;
    });

    if (seq.length-1+baz == 60)
	count++;

    console.log(x + ":  " + (seq.length-1+baz));

});
console.log(count + " numbers containing 60 non-repeating terms!");