/*
 * @author ghostsnstuff
 * params: sorted list and value to be searched for
 * while loop = search behavior
 * break loop if value found or if startIndex = stopIndex
 * if value is < current middle -> reduce the list search content to the lower half 
 * if value is > current middle -> reduce the list search content to the upper half
 * update middle after if else if
 * return middle if value == list[middle] else return -1
 */

module.exports = function(array, value) {  
  var startIndex = 0
    , stopIndex = array.length - 1
    , middle = ~~((startIndex + stopIndex)/2);      
  while(array[middle] !== value && startIndex < stopIndex) {
    if(value < array[middle]) stopIndex = middle - 1;
    else if(value > array[middle]) startIndex = middle + 1;
    middle = ~~((startIndex + stopIndex)/2);
  }
  return (array[middle] === value) ? middle : -1;
}
