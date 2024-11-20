#!/usr/bin/node

function converter() {
  var results = [];
  for (var i = 0; i < arguments.length; i++) {
    results.push(function() {
      return arguments[i];
    });
  }
  return results;
}
