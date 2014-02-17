exports.mean = function(data, decimals) {
	var sum = 0;
	for(var i = 0; i < data.length; i++) sum += data[i];
	if(decimals !== undefined) return (sum/data.length).toFixed(decimals);
	else return (sum/data.length).toFixed(2);	
}

exports.median = function(data) {
   var median = 0;
   data = data.sort(function (a, b) { return a - b });
   if(data.length % 2 === 0) return (data[(data.length/2)-1] + data[(data.length/2)])/2;
   else return data[~~(data.length/2)];
}

exports.mode = function(data) {
  var ram = {}, res = {}, modes = [], max = 0, tempMax = 0;
  for(var i = 0; i < data.length; i++) {
    if(ram[data[i]]) ram[data[i]] += 1;
    else ram[data[i]] = 1;
  }
  for(var i in ram) {
    tempMax = ram[i];
    if(max < tempMax) max = tempMax;
  }
  res.frequency = max;
  for(var i in ram) if(ram[i] === max) modes.push(i);
  res.values = modes;
  if(max === 1) return 'no mode(s) in sample';
  else return res;
}


