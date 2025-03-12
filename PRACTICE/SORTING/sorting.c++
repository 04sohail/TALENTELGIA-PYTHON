#include <bits/stdc++.h>
using namespace std;

void insertion_sort(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        int minNum = i;
        for (int j = i; j < n; j++)
        {
            if (arr[j] < arr[minNum])
            {
                minNum = j;
            };
        };
        int temp = arr[0];
        arr[0] = arr[minNum];
        arr[minNum] = temp;
    };
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << endl;
    };
};

int main()
{
    int arr[] = {23, 65, 78, 26, 56, 67, 12};
    int n = 7;
    insertion_sort(arr, n);
    return 0;
};

// # lst = [23, 65, 78, 26, 56, 67, 12]

// # SELECTION SORTING
// # ASCENDING ORDER
// # def getMin(lst):
// #     minNum = lst[0]
// #     for i in lst:
// #         if i<minNum:
// #             minNum = i
// #     return minNum

// # def sorting(lst):
// #     for i in range(0, len(lst)-2):
// #         minNum = getMin(lst[i:])
// #         minIndex = lst.index(minNum)
// #         lst[i], lst[minIndex] = minNum, lst[i]
// #     return lst

// # print(sorting(lst))

// # DESCENDING ORDER
// # def getMax(lst):
// #     maxNum = lst[0]
// #     for i in lst:
// #         if i>maxNum:
// #             maxNum = i
// #     return maxNum

// # def sorting(lst):
// #     for i in range(0, len(lst)-1):
// #         maxnum = getMax(lst[i:])
// #         maxnumindex = lst.index(maxnum)
// #         lst[i], lst[maxnumindex] = maxnum, lst[i]
// #     return lst

// # print(sorting(lst))

// # BUBBLE SORTING
// # ASCENDING ORDER

// lst = [23, 65, 78, 26, 56, 67, 12]

// def sorting(lst):
//     for i in range(len(lst)-1, -1, -1):
//         for j in range(i, 0, -1):
//             if lst[j] < lst[j+1]:
//                 lst[j], lst[j+1] = lst[j+1], lst[j]
//     return lst
// print(sorting(lst))