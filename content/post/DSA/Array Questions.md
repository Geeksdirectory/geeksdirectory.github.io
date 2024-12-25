## 1. Find the largest and smallest element in an array

```java
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int [] arr = {3,2,1,3,4,5,4};
        Arrays.sort(arr);
        
        int smallest = arr[0];
        int largest = arr[arr.length-1];
        
        System.out.println(smallest);
        System.out.println(largest);
    }
}
```

### more  approach:

```java

class Main {
    public static void main(String[] args) {
        int arr[] = {3,2,1,3,4,5,4};
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if(arr[i]>max){
               max = arr[i];   
            }
        }
        System.out.println(max);
        
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if(arr[i]<min){
               min = arr[i];   
            }
        }
        System.out.println(min);
    }
}

```

---

## 2. Reverse an array 


int[] arr = {1,2,3,4,5}
output = 5,4,3,2,1


```java
public class Main{
	public static void main(String[] args){
	int[] arr = {3,2,1,3,4,5};
	int start = 0, end = arr.length - 1;
	while (start < end) {
		int temp = arr[start];
		arr[start] = arr[end];
		arr[end] = temp;
		start ++;
		end --; 
	}
	System.out.println("reversed array"+ java.util.Arrays.toString(arr));
	}
}
```

---
## 3. Check if an Array is Sorted

```java

class Main {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7};
        boolean isSorted = true;
        
        for(int i = 1 ; i < arr.length  ; i++ ){
            if (arr[i] < arr[i - 1]){
                isSorted = false;
            }
        }
        System.out.println("sorted array " + isSorted);
        
     }
}
```

---

## 4. Move all zero to the end

input:array = {0,0,0,23,134,2}
output = {23,134,2,0,0,0}

```java
public class Main {
    public static void main(String[] args) {
        int insertPosition = 0;
        int[] nums = {0,0,0,0,1,3,4};
        for( int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                nums[insertPosition] = nums[i];
                insertPosition++;
            }
        }

        while (insertPosition < nums.length) {
            nums[insertPosition++] = 0;
        }
        System.out.println(java.util.Arrays.toString(nums));
    }
}
```

## 5. **Find the Second Largest Element**
