#!/usr/bin/node

const firstArgInt = parseInt(process.argv[2]);

if (firstArgInt) {
  console.log(`My number: ${firstArgInt}`);
} else {
  console.log('Not a number');
}
