#!/usr/bin/node

// processa.argv.slice(2) get args from index 2
// .map(arg => parseInt(arg)) convert ars to integer
const values = process.argv.slice(2).map(arg => parseInt(arg));

if (values.length <= 1) {
  console.log(0);
} else {
  values.sort((a, b) => b - a); // sort arrays of int in desc order
  console.log(values[1]);
}
