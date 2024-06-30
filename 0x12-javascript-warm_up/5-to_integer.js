#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0]) {
  console.log('Not a number');
} else if (!Number(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(parseFloat(args[0])));
}
