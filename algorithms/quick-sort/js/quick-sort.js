/*
 * @author ghostsnstuff
 * worst: O(n^2)
 * best:  O(n logn)
 * avg:   O(n logn);
 * paramater: unsorted list
 * base case: list.size === 0
 * pivot is always the first position in the list
 * organize data based on its relation to the pivot value
 * data that is smaller than the pivot -> gets pushed to the left[]
 * data that is larger than the pivot -> get pushed to the right[]
 * recursive calls are made until the original list is of size zero
 */

function QuickSort(list) {
  var size = list.length, left = [], right = [], pivot;
  if(size === 0) return list;
  pivot = list[0];
  for(var i = 1; i < size; i++) {
    if(list[i] <= pivot) left.push(list[i]);
    else right.push(list[i]);
  }
  left = QuickSort(left);
  right = QuickSort(right);
  return left.concat(pivot,right);
};
  // test       
var numbers = [ 11, 78, 23, 4, 2, 86, 100, 29, 19 ];
console.log(numbers);
console.log(QuickSort(numbers));
