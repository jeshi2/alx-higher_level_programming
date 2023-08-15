#!/usr/bin/node

function factorial (i) {
  if (isNaN(i) || i === 0) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
const namba = parseInt(process.argv[2]); // parse convert argv to integer
const output1 = factorial(namba);
console.log(output1);
