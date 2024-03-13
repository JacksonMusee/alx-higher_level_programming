#!/usr/bin/node

const num = parseInt(process.argv[2]);
let ans;

function factorial (num) {
  if (num === 1) {
    return (1);
  }

  return (num * factorial(num - 1));
}

if (!num) {
  ans = 1;
} else {
  ans = factorial(num);
}

console.log(ans);
