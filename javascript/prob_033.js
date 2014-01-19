#!/usr/local/bin/node

var _ = require('./underscore');

var i = 49;
var j = 98;

for (var j = 11; j <= 99; j++)
{
    if (j % 10 == 0)
	continue;
    for (var i = 11; i < j; i++)
    {
	if (i % 10 == 0)
	    continue;

	var short_digits = removeCommonDigit(i, j);
	if (typeof(short_digits) == 'undefined')
	    continue;

	var exp_val = i / j;
	if (i / j == short_digits[0] / short_digits[1])
	    console.log(i + "/" + j + ", " +
			short_digits[0] + "/" + short_digits[1]);

   }
}


function removeCommonDigit(i, j)
{
    var a = i.toString().split("");
    var b = j.toString().split("");

    var cdigit = _.find(a, function(val, key) {
	return _.find(b, function (y) {
	    return y == val;
	});
    });

    if (typeof(cdigit) == 'undefined')
	return;

    return _.flatten(_.map([a, b], function(y) {
	return _.map(_.reject(y, function(x) {
	    return x == cdigit;
	}), function (z) {
	    return parseInt(z);
	});
    }));
}