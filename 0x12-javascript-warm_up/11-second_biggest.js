#!/usr/bin/node

const arr = process.argv.slice(2);
let secMax = 0;
let Max = 0;
let tmp = 0;
let i = 0;

while (parseInt(arr[i])) {
  tmp = parseInt(arr[i]);

  if (tmp > Max) {
    secMax = Max;
    Max = tmp;
  } else if (tmp > secMax) {
    secMax = tmp;
  }
  i++;
}

console.log(secMax);
