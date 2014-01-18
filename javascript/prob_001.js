#!/usr/local/bin/node

var _ = require('./underscore');
console.log(_.reduce((_.union(_.range(0, 1000, 3), _.range(0, 1000, 5))), function(memo, num) { return memo + num; }));