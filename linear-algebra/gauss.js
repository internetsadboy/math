var a = [[1,2,3],
         [4,5,6],
         [7,8,9]];

function getRow(m, r) {
  return m[r];
}

//console.log(getRow(a,0));

function getCol(m, c) {
  var result = [];
  for(var i = 0; i < m.length; i++) result.push(m[i][c]);
  return result;
}

//console.log(getCol(a, 0));

function changeRow(m) {
  return m[0][0] === 0;
}

//console.log(changeRow(a));

function generateMultiplier(s, t) {
  
}
