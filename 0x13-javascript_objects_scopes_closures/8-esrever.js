#!/usr/bin/node

exports.esrever = function (list) {
  let i = 1;
  const len = list.length;
  const myArr = [];

  while (i <= len) {
    myArr.push(list[len - i]);
    i++;
  }

  return (myArr);
};
