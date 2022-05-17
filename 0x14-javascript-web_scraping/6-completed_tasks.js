#!/usr/bin/node
const axios = require('axios');

axios.get('https://jsonplaceholder.typicode.com/todos')
  .then(function (response) {
    const user = {};
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed) {
        if (!(response.data[i].userId in user)) {
          user[response.data[i].userId] = 0;
        }
        user[response.data[i].userId] += 1;
      }
    }
    console.log(user);
  });
