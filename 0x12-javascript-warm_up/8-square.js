#!/usr/bin/node
let pstr = '';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let j = 0; j < process.argv[2]; j++) {
    for (let i = 0; i < process.argv[2]; i++) {
      pstr += 'X';
    }
	  console.log(pstr);
	  pstr=''
  }
}
