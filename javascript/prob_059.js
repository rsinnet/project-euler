#!/usr/local/bin/node

var _ = require('./underscore');
var fs = require('fs');

var stream = fs.createReadStream('../cipher1.txt');
var chars = [];
stream.addListener('data',
		   function(data) {
		       var chars = data.toString().replace(/\n/g, '').split(',');
		       doLoop(chars);
		   });

function doLoop(chars)
{
    _.each(cartProd(_.map(_.range(3), function() { return _.range(97,123,1); })),
	   function(x) {
	       var schars = _.map(chars,
				  function(c, i) {
				      return String.fromCharCode(parseInt(c) ^ x[i % 3]);
				  });
	       var msg = schars.join("");	
	       
	       if (checkMessage(msg))
	       {
		   var pass = _.map(x, function(y) { return String.fromCharCode(y); }).join("");
		   console.log("Password: " + pass);
		   console.log("Message: ");
		   console.log(msg);
	       }
	   });
}

function checkMessage(msg)
{
    if (msg.search(" the ") > 0)
	return true;
    return false;
}

function cartProd(z) {
    return _.reduce(z, function(a, b) {
	return _.flatten(_.map(a, function(x) {
	    return _.map(b, function(y) {
		return x.concat([y]);
	    });
	}), true);
    }, [ [] ]);
}