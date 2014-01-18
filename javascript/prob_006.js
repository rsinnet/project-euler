#!/usr/local/bin/node

var _ = require('./underscore');
var N = 101;
console.log(Math.pow(_.reduce(_.range(N), function(memo, num) { return memo + num; }, 0), 2) - _.reduce(_.map(_.range(N), function(x) { return x*x; }), function(memo, num) { return memo + num; }, 0));
