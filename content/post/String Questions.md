![[Pasted image 20241221134403.png]]

here we have to find two substring ( left ) a ( right )
and modify smallest substring beside "a".

eg: h==a==ckerrank here h is the smallest substring then ckerrank

so only modify h 

```java
class Main {
    public static String getSmallestString(String s) {
        char[] charArray = s.toCharArray();
        boolean modified = false;
        
        
        for(int i =0; i <= charArray.length; i++){
            if (charArray[i] == 'a' ){
                if (modified) {
                    break;
                }
                continue;
            }
            modified = true ;
            charArray[i] = (char) (charArray[i] - 1);
        }
        if (!modified){
            charArray[charArray.length - 1] = (char) (charArray[charArray.length - 1] - 1);
        }
        
        return new String(charArray);
        
    }
    
    public static void main(String[] args) {
        String s = "hackerrank";
        String result = getSmallestString(s);
        System.out.println(result);
    }
}
```




# Basic Easy questions 

### 1. reverse a string

input = hello
output = olleh

```java
class Main {
    public static void main(String[] args) {
        String str = "yash";
        String reversed = new StringBuilder(str).reverse().toString();
        System.out.println(reversed);
    }
}
```

## 2. Check if string is Palindrome or not

input: madam
output: true

```java
class Main {
	public static void main(String[] args){
	String str = "madam";
	String reverse = new StringBuilder(str).reverse().toString();
    boolean isPlaindrome = reverse.equals(str);
    System.out.println(isPlaindrome);
	}
}
```

code 2 

```java
class Main {
    public static void main(String[] args) {
        String str = "madam"; // Corrected string initialization
        String reverse = new StringBuilder(str).reverse().toString(); // Fixed toString() method
        
        if (reverse.equals(str)) { // Compare content using equals()
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }
    }
}
```

