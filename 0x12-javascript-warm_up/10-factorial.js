#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0]) {
  console.log('1');
} else {
  function factorialize (num) {
    if (num < 0) {
      return -1;
    } else if (num === 0) {
      return 1;
    } else {
      return (num * factorialize(num - 1));
    }
  }
  console.log(factorialize(Number(args[0])));
}
