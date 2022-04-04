#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let count = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      count += 'X';
    }
    console.log(count);
  }
}
