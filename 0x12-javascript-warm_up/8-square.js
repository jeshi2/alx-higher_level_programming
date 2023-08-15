#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size) || size <= 0) {
  if (size < 0) {
    // Nothing
  } else {
    console.log('Missing size');
  }
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
