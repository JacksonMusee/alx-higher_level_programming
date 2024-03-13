#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  let count = 1;

  while (count <= num) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
