The sigmoid activation function takes real values as input and converts them to numbers between 0 and 1 using the sigmoid formula.

![[Pasted image 20241101163942.png]]

![[Pasted image 20241101164047.png]]

![[Pasted image 20241101164146.png]]


RELU
![[Pasted image 20241109101508.png]]
![[Pasted image 20241101164213.png]]

##### **Leaky ReLU**

- **Function:** 
 ![[Pasted image 20241109111154.png]]
 where α alphaα is a small constant (typically 0.01).
- **Description:** Allows a small, non-zero gradient when xxx is negative, which helps keep neurons active.
- **Pros:** Reduces the risk of dead neurons.
- **Cons:** Requires setting an additional parameter (α\alphaα).


![[Pasted image 20241101164234.png]]