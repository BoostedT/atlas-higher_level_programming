#!/usr/bin/node

exports.nb0Occurences = function (list, searchElement) {
  return list.filter(function (element) {
    return element === searchElement;
  }).length;
};
