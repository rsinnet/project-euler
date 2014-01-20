#!/usr/local/bin/node

// Project Euler
// Problem 62
// Cubic permutations

var _ = require('./underscore');

var i = 100;

var nums = {};
var bnums = {};

while (true) {
    i++;
    var foo = _.sortBy(Math.pow(i, 3).toString().split("")).join("");
    if (typeof(nums[foo]) == 'undefined') {
	nums[foo] = 1;
	bnums[foo] = [];
    }
    else
	nums[foo] += 1;
    bnums[foo].push(i);

    if (nums[foo] >= 5) {
	console.log(_.first(bnums[foo]) + ", " + Math.pow(_.first(bnums[foo]), 3));
	console.log(bnums[foo]);
	break;
    }
}