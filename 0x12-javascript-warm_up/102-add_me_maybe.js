#!/usr/bin/node

exports.addMeMaybe = function (number, incremCall) {
  incremCall(number + 1);
};
