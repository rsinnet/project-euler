#!/usr/local/bin/node

var _ = require('./underscore');
var comp_nums = _.map(_.range(10000), function() { return false; });

var i = 1;
while (2 * i < comp_nums.length) {
    ++i;
    if (!comp_nums[i-1])
	_.each(_.range(2*i, comp_nums.length+1, i), function(x) {
	    comp_nums[x-1] = true;
	});
}

for (var i = 1000; i < 10000; i++)
{
    if (comp_nums[i-1])
	continue;

    if (comp_nums[i-1 + 3330] || comp_nums[i-1 + 6660])
	continue;

    if (isPerm(i, i+3330) && isPerm(i, i+6660))
	console.log("" + i + (i+3330) + (i+6660));
}

function isPerm(a, b)
{
    return _.isEqual(_.sortBy(a.toString().split(""), function(x) { return parseInt(x); }),
		     _.sortBy(b.toString().split(""), function(x) { return parseInt(x); }))
}