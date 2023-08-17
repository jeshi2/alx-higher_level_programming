#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let i = list.length; i > 0; i--) {
    reverseList.push(list[i - 1]);
  }
  return reverseList;
};
