---
title: Java recursion problems solved can be asked in interview
date: 2024-09-28
categories:
  - java
  - placement
---
## check if an array is sorted (strictly sorted)


![](https://i.imgur.com/kUDx16x.png)


```java
public class Recursion2 {
  public static boolean isSorted(int arr[], int idx) {
    // Print the current index and the elements being compared
    System.out.println("Checking if arr[" + idx + "] < arr[" + (idx + 1) + "]");

    // Base case: if we're at the last index, the array is sorted
    if (idx == arr.length - 1) {
      System.out.println("Reached the last element, array is sorted.");
      return true;
    }

    // Recursive case: if the current element is less than the next, keep checking
    if (arr[idx] < arr[idx + 1]) {
      System.out.println("arr[" + idx + "] = " + arr[idx] + " is less than arr[" + (idx + 1) + "] = " + arr[idx + 1] + ", checking further.");
      return isSorted(arr, idx + 1);
    } else {
      System.out.println("arr[" + idx + "] = " + arr[idx] + " is NOT less than arr[" + (idx + 1) + "] = " + arr[idx + 1] + ", array is not sorted.");
      return false;
    }
  }

  public static void main(String args[]) {
    int arr[] = {1, 3, 5};  // You can modify this array to test different cases
    System.out.println("Is the array sorted? " + isSorted(arr, 0));
  }
}
```

#### time complexity = O(n)
![](https://i.imgur.com/YsRLkfz.png)



## Move all 'X' to the end of string ("acbcxxd")

Given a string like `"axbcxxd"`, we want to move all the `'x'` characters to the end. The result for this example would be `"abcxdxx"`

- If the current character is **not 'x'**, keep it where it is.
- If the current character **is 'x'**, move it to the end.

Recursion involves solving a problem by breaking it into smaller sub-problems. Here's how we can think about this:

1. If the string is empty, return an empty string (base case).
2. For a string that is not empty:
    - If the first character is **not 'x'**, keep it at the front and call the function recursively on the rest of the string.
    - If the first character **is 'x'**, move it to the end and call the function recursively on the rest of the string.

```java
public class MoveXToEnd {

  // Recursive function to move all 'x' to the end of the string
  public static String moveXToEnd(String str) {
    // Base case: if the string is empty, return the empty string
    if (str.length() == 0) {
      return "";
    }

    // Get the first character of the string
    char firstChar = str.charAt(0);

    // Recursively call moveXToEnd on the rest of the string
    String restOfString = moveXToEnd(str.substring(1));

    // If the first character is 'x', append it to the result of the recursion
    if (firstChar == 'x') {
      return restOfString + firstChar; // Move 'x' to the end
    } else {
      return firstChar + restOfString; // Keep the first character in front
    }
  }

  // Main method to test the function
  public static void main(String[] args) {
    String input = "axbcxxd";
    String result = moveXToEnd(input);
    System.out.println("Result: " + result);
  }
}

```

#### time complexity O(n)

### Remove Duplicates of strings 
 

![](https://i.imgur.com/98boTPH.jpeg)


```java
public class Recursion2 {
  public static boolean[] map = new boolean[26];
  
  public static void removeDuplicates(String str, int idx, String newString){
    if(idx == str.length()) {
      System.out.println(newString);
      return;
    }
    char currChar= str.charAt(idx);
    if(map[currChar - 'a']) {
       removeDuplicates(str, idx+1, newString);
       
    } else {
      newString += currChar;
      map[currChar - 'a'] = true;
      removeDuplicates (str,idx+1, newString);
    }
  }
  
  public static void main (String args[]) {
    String str = "abbcddddaaa";
    removeDuplicates(str,0,"");
  }
}
```


### print all the sub-sequences of a string "abc"

![](https://i.imgur.com/caZ2lxN.png)
![](https://i.imgur.com/eNwoPlV.png)
 


```java
public class Recursion2 {
  public static void subsequence(String str, int idx, String newString){
    
    if(idx == str.length())  {
      System.err.println(newString);
      return;
    }  
    char currcharr = str.charAt(idx);
    
    subsequence(str, idx+1, newString + currcharr);
    
    subsequence(str,idx+1,newString);
  
  }
  
  public static void main (String args[]) {
    String str = "abc";
    subsequence(str,0,"");
  }
}
```

#### time complexity = 2^n

### Print keypad combnation

![](https://i.imgur.com/V5RJ7U9.jpeg)



```java
import java.util.HashSet;

public class Recursion2 {
  public static String[] keypad =  {".","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"};
  
  public static void printComb(String str, int idx, String combination) {
    if(idx == str.length()) {
      System.out.println(combination);
      return;
    }
    char currChar = str.charAt(idx);
    String mapping = keypad[currChar - '0'];
    
    for(int i =0; i<mapping.length(); i++){
      printComb(str, idx+1,combination+mapping.charAt(i));
    }
  }
  
  public static void main (String args[]){
    String str = "41";
    printComb(str,0,"");
  }
  
}
```