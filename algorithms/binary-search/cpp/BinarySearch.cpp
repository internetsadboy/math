#include <iostream>
#include <array>
using namespace std;

// params: sorted list and value to be searched for
// while loop = search behavior
// break loop if value found or if startIndex = stopIndex
// if value is < current middle -> reduce the list search content to the lower half 
// if value is > current middle -> reduce the list search content to the upper half
// update middle after if else if
// return middle if value == list[middle] else return -1

int binarySearch(array<int,20> list, int value)
{
    int startIndex = 0;
    int stopIndex = list.size() - 1;
    int middle = ((startIndex + stopIndex)/2);

    while(list[middle] != value && startIndex < stopIndex) 
    {	
        if(value < list[middle]) {
            stopIndex = middle - 1;
        } else if(value > list[middle]) {
            startIndex = middle + 1;
        }
        middle = ((startIndex + stopIndex)/2);
    }

    return (list[middle] == value) ? middle : -1;

}

int main() 
{	
    array<int,20> data = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    int value = 14;
    cout << "result: " << binarySearch(data, value) << endl;
    return 0;
}
