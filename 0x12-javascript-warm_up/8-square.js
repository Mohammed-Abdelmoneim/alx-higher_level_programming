#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0] || !Number(args[0])) {
  console.log('Missing size');
} else if (args[0]) {
  for (let i = 0; i < args[0]; i++) {
    console.log('X'.repeat(args[0]));
  }
}
