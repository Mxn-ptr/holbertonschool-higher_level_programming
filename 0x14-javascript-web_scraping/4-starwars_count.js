#!/usr/bin/node
const axios = require('axios');
let count = 0;

axios.get('https://swapi-api.hbtn.io/api/films')
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      for (let j = 0; j < response.data.results[i].characters.length; j++) {
        if (response.data.results[i].characters[j].includes('/18/') === true) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
