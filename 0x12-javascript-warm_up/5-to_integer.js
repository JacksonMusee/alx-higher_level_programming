#!/usr/bin/node

const firstArgInt = parseInt(process.argv[2]);

if (firstArgInt) {
  console.log(firstArgInt);
} else {
  console.log('Not a number');
}
