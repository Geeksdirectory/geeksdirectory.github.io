	

> [!NOTE]
> we use binary search in sorted arrays.
> if we get problem statement with sorted array try binary search first.

### Q.1 ceiling of a given number 

ceiling of no is smallest ele in arr greater ot == target
arr = [2,3,4,5,9,14,16,18], target = 14
if target = 14 then ceiling = 14
ceiling(arr,target=15) = 16 

![[Pasted image 20241202175529.png]]


![[Pasted image 20241203070828.png]]

### Q.2 Floor of a number

![[WhatsApp Image 2024-12-03 at 06.47.31_98d7e648.jpg]]

### Code 

![[Pasted image 20241203070809.png]]


### Q.3 Find Smallest letter greater than target [ leetcode : 744 ]


1. Exact same approach for cieling of the number
2. ignore the target = what are looking for.
3. wrapping of later eg: arr = ['c','d','f','j'] , target = 'j' output = c we will use modulo (%) 
4. condition violeted : start = end + 1 ==> length of array = N   

![[Pasted image 20241204144936.png]]



### 4. Find First and Last Position of Element in Sorted Array

**Example 1:**
**Input:** nums = [5,7,7,8,8,10], target = 8
**Output:** [3,4]

**Example 2:**
**Input:** nums = [5,7,7,8,8,10], target = 6
**Output:** [-1,-1]

**Example 3:**
**Input:** nums = [], target = 0
**Output:** [-1,-1]

![[Pasted image 20241204114845.png]]

---

### 5. Find position of an element in a sorted array of infiniate numbers. (amazon interview question)

> try not to use array.length in infinite array 

https://youtu.be/W9QJ8HaRvJQ?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&t=6656

traverse through chunks
![[Pasted image 20241215122615.png]]

![[Pasted image 20241215121554.png]]


Doubling the size of chuck 

![[Pasted image 20241215123745.png]]

