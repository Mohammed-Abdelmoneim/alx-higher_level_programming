#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0] || args[0] === 1) {
  console.log('0');
} else {
  let num = 0;
  let sec = 0;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > num) {
      num = args[i];
    }
  }
  for (let i = 0; i < args.length; i++) {
    if (args[i] > sec && args[i] < num) {
      sec = args[i];
    }
  }
  console.log(sec);
}
