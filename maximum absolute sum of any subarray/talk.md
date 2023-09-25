### Maximum Absolute Sum of Any Subarray

So this is problem no. 1749 and its one the easier problems out there. The absolute part kind of throws everyone for a spin. But there is one trick to make this problem easy. That is the Kadane's Algorithm.

Its an algorithm that can compute the lagrest/smallest subarray sum in **linear** time complexity. The basic structure of this algorithm is:

```
for a in array:
 int current=0;
 int max=0;
 current+= array[a];
 if(current<0){
    current=0;
 }
 if(current>max){
    max=current;
 } 
 return max;
```
So, to solve this problem, simply do run this twice, once counting max sum, once counting min sum.
and then find the max of these two numbers in absolute.
```
max(abs(ms),abs(mins));
```