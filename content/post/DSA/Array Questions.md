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

