#!/usr/bin/node

const { dict } = require('./101-data.js');

const invertDic = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in invertDic) {
    invertDic[occurrences].push(userId);
  } else {
    invertDic[occurrences] = [userId];
  }
}
console.log(invertDic);
