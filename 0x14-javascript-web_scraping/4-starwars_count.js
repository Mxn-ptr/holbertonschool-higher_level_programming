#!/usr/bin/node
const axios = require('axios');
let count = 0;

axios.get('https://swapi-api.hbtn.io/api/films')
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      if (response.data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  });
