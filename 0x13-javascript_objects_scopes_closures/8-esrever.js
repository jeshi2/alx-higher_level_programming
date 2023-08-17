#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  // let i = list.legth -1;
  while (list.legth > 0) {
    reverseList.push(list.pop());
    // i--;
  }
  return reverseList;
};
