#!/usr/bin/node

const numb = parseInt(process.argv[2]);

if (!isNaN(numb)) {
  console.log(`My number: ${numb}`);
} else {
  console.log('Not a number');
}
