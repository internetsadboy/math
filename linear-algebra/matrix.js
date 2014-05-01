exports.addVectors = function(s, t, print) {
  var result = [];
  for(var i = 0; i < s.length; i++) result[i] = s[i] + t[i];
  if(print === 'print') console.log(result);
  return result;
}

exports.scalarMult = function(m, s, print) {
  if(!s) 
  var result = [];
  for(var i = 0; i < m.length; i++) result[i] = s * m[i];
  if(print === 'print') console.log(result);
  return result;
}

exports.dot = function(s, t, print) {
  var temp = [], result = 0;
  for(var i = 0; i < s.length; i++) temp[i] = s[i] * t[i];
  for(var i = 0; i < temp.length; i++) result += temp[i];
  if(print === 'print') console.log(result);
  return result;
}

exports.getRow = function(m, r, print) {
  if(!r && r != 0) throw new Error('row is undefined');
  if(!print) return m[r];
  if(print.toLowerCase() === 'print') {
    console.log(m[r]);
    return m[r];
  }
}

exports.getCol = function(m, col, print) {
  if(!col) throw new Error('column is undefined');
  var result = [];
  for(var i = 0; i < m.length; i++) result[i] = m[i][col];
  if(print === 'print') console.log(result);
  return result;
}

// not finished
exports.scalarMatrixMult = function(m, s, print) {
  if(!s) throw new Error('scalar is undefined');
  var result = [];
  if(print === 'print') console.log(result);
  return result;
}

exports.transpose(m) {
  var result = [];
  if(!m) throw new Error('m is undefined');
  var numRows = m.length;
  var numCols = m[0].length;
  for(var i = 0; i < numRows; i++) {
    for(var j = 0; j < numCols; j++) {
      
    }
  }

}
