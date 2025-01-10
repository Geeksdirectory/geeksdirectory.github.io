---
title: Module 1 Activation Functions
date: 2025-01-10
---

The sigmoid activation function takes real values as input and converts them to numbers between 0 and 1 using the sigmoid formula.

![alt text](Pastedimage20241101163942.png)

![alt text](Pastedimage20241101164047.png)

![alt text](Pastedimage20241101164146.png)


RELU
![alt text](Pastedimage20241109101508.png)
![alt text](Pastedimage20241101164213.png)

##### **Leaky ReLU**

- **Function:** 
 ![alt text](Pastedimage20241109111154.png)
 where α alphaα is a small constant (typically 0.01).
- **Description:** Allows a small, non-zero gradient when xxx is negative, which helps keep neurons active.
- **Pros:** Reduces the risk of dead neurons.
- **Cons:** Requires setting an additional parameter (α\alphaα).


![alt text](Pastedimage20241101164234.png)