#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const dataLst = JSON.parse(body);

    const summaryObj = {};

    for (const todo of dataLst) {
      if (todo.completed === true) {
        const strId = todo.userId.toString();
        if (summaryObj[strId]) {
          summaryObj[strId] += 1;
        } else {
          summaryObj[strId] = 1;
        }
      }
    }
    console.log(summaryObj);
  }
});
