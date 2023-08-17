#!/usr/bin/node

const fs = require('fs');
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

fs.readFile(sourceFile1, 'utf-8', (err1, data1) => {
  if (err1) {
    console.error(err1);
    return;
  }

  fs.readFile(sourceFile2, 'utf-8', (err2, data2) => {
    if (err2) {
      console.error(err2);
      return;
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf-8', (err3) => {
      if (err3) {
        console.error(err3);
        return;
      }

      //console.log(`Concatenated data saved to ${destinationFile}`);
    });
  });
});
