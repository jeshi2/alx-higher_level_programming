#!/usr/bin/node

exports.callMeMoby = function (x, infintExc) {
  for (let i = 0; i < x; i++) {
    infintExc();
  }
};
