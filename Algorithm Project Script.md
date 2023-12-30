# Intro
Hello, my name is Kamal Mohamed and this is the Analysis and Design of Algorithms course project where I will be going over how to solve the maximum subarray problem by applying Dynamic Programming Technique

# Problem
Let us go over the problem definition. The problem tasks us find a contiguous subarray with the largest sum
A subarray is a contiguous subset of an array. (Talk about the contiguous subarray example) 
Contiguous subarray is a subarray with a condition that the it's elements should be in exact sequence as the sequence of the elements in the array


# Brute-force approach
We have 2 approaches, one with 3 nested for loops to determine all the possible subarray sums and return the maximum among them. 
The 2nd approach which is an optimized version of what we just discussed The idea is to start at all positions in the array and calculate running sums. The outer loop picks the beginning element, the inner loop finds the maximum possible sum with the first element picked by the outer loop and compares this maximum with the overall maximum.


# Dynamic Programming
Enter Dp, in it's essence;  it is a technique for solving problems with overlapping subproblem, rather than solving overlapping subproblems again and again, dynamic programming suggests solving each of the smaller subproblems only once and recording the results in a table from which a solution to the original problem can then be obtained. Now, for our case we don't need a table instead we can use an auxiliary array that holds the maximum subarray sum ending at a particular index. 


# Kadane's Algorithm
the current element or the current element combined with the previous maximum subarray 

# Algorithm
$$
\sum_{i=1}^n 1 = n-1+1 = n\in O(n)
$$