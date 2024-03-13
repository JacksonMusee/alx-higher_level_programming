#!/usr/bin/node

const arr = process.argv.slice(2);
let preMax = 0;
let currMax = 0;
let tmp = 0;
let i = 0;

while (parseInt(arr[i])) {
  tmp = parseInt(arr[i]);

  if (tmp > currMax) {
    preMax = currMax;
    currMax = tmp;
  }
  i++;
}

console.log(preMax);
