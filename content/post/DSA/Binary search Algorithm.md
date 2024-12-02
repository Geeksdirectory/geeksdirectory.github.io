https://youtu.be/f6UU7V3szVw?si=26WxPdb9UAUEqpAx

- Used for sorted arrays
- in ascending or descending order
- It works by repeatedly dividing the search interval in half and comparing the target with the middle element.
---

### Algo

1. find the middle element
2. target ele > mid ele => search in right else search in left
3. if mid ele == target ele => ans

---

### Time Complexity:![[Pasted image 20241126204755.png]]


- **Best Case**: O(1) (target found at the middle).
- **Worst Case**: O(log⁡n)   (array size halved each step).

----
### Space Complexity:

- O(1) (iterative approach, no extra memory used).

---
> while coding
![[Pasted image 20241128052751.png]]

![[Pasted image 20241128052907.png]]

---
### code for binary search [[hinglish explaination of code]]

![[Pasted image 20241128054208.png]]

### Order agnostic binary search

![[Pasted image 20241128061939.png]]




