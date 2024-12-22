qBilkul bhai! Java mein `String` ek kaafi important topic hai. Main tujhe step-by-step `String` ke basics se lekar advanced concepts tak revise karwata hoon.

---

### **1. String Introduction**

- `String` ek **class** hai jo Java mein **java.lang.String** package ka part hai.
- String ko **immutable** bola jata hai, iska matlab hai ek baar string banne ke baad usko change nahi kar sakte.
- String ko ya to **String literals** ke through ya phir **new keyword** se create karte hain.

**Example:**

```java
// Using String literal
String str1 = "Hello";

// Using new keyword
String str2 = new String("World");
```

---

### **2. Important Methods of String**

#### (a) **Length of a String**

String ka length nikalne ke liye `length()` method use hota hai.

```java
String str = "Java";
System.out.println(str.length()); // Output: 4
```

#### (b) **Concatenation (Join Strings)**

Strings ko combine karne ke liye `+` operator ya `concat()` method ka use hota hai.

```java
String s1 = "Hello";
String s2 = "World";
System.out.println(s1 + " " + s2);  // Output: Hello World
System.out.println(s1.concat(" " + s2));  // Output: Hello World
```

#### (c) **Character Extraction**

1. `charAt(index)` - Kisi specific index ka character nikalta hai.
2. `substring(startIndex, endIndex)` - Ek substring nikalta hai.

```java
String s = "Hello";
System.out.println(s.charAt(1)); // Output: e
System.out.println(s.substring(1, 4)); // Output: ell
```

#### (d) **String Comparison**

1. `equals()` - Dono strings ka exact match check karta hai.
2. `equalsIgnoreCase()` - Case ko ignore karke strings compare karta hai.
3. `compareTo()` - Lexicographical comparison karta hai.

```java
String s1 = "Hello";
String s2 = "hello";

// Case-sensitive
System.out.println(s1.equals(s2)); // Output: false

// Case-insensitive
System.out.println(s1.equalsIgnoreCase(s2)); // Output: true

// Lexicographical comparison
System.out.println(s1.compareTo(s2)); // Output: -32
```

#### (e) **Searching in String**

1. `indexOf(char)` - Character ka first occurrence batata hai.
2. `lastIndexOf(char)` - Character ka last occurrence batata hai.
3. `contains(String)` - String ke andar substring check karta hai.

```java
String s = "Java Programming";
System.out.println(s.indexOf('a')); // Output: 1
System.out.println(s.lastIndexOf('a')); // Output: 13
System.out.println(s.contains("Java")); // Output: true
```

#### (f) **String Replacement**

`replace(oldChar, newChar)` aur `replaceAll(regex, replacement)` ka use hota hai.

```java
String s = "Java is fun";
System.out.println(s.replace('a', 'e')); // Output: Jeve is fun
System.out.println(s.replaceAll("fun", "awesome")); // Output: Java is awesome
```

#### (g) **Case Conversion**

1. `toUpperCase()` - String ko uppercase mein convert karta hai.
2. `toLowerCase()` - String ko lowercase mein convert karta hai.

```java
String s = "Hello World";
System.out.println(s.toUpperCase()); // Output: HELLO WORLD
System.out.println(s.toLowerCase()); // Output: hello world
```

---

### **3. Immutable vs Mutable Strings**

- Immutable String: `String` class immutable hoti hai.
- Mutable String: `StringBuilder` aur `StringBuffer` mutable hote hain.

**Example of Immutable:**

```java
String s = "Hello";
s.concat(" World");
System.out.println(s); // Output: Hello (original string unchanged)
```

**Example of Mutable (StringBuilder):**

```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
System.out.println(sb); // Output: Hello World
```

---

### **4. String Pool**

- String literals `String Pool` mein store hote hain (Heap ke andar ek special memory).
- Agar ek hi string literal do alag variables mein use ho raha hai, to dono same memory location point karte hain.

**Example:**

```java
String s1 = "Java";
String s2 = "Java";
System.out.println(s1 == s2); // Output: true
```

But agar `new` keyword use karenge to alag memory allocate hoti hai.

```java
String s1 = new String("Java");
String s2 = new String("Java");
System.out.println(s1 == s2); // Output: false
System.out.println(s1.equals(s2)); // Output: true
```

---

### **5. StringTokenizer (for Splitting)**

Java mein `StringTokenizer` ka use string ko split karne ke liye hota hai.

```java
import java.util.StringTokenizer;

StringTokenizer st = new StringTokenizer("Java is fun", " ");
while (st.hasMoreTokens()) {
    System.out.println(st.nextToken());
}
// Output:
// Java
// is
// fun
```

---

### **6. Advanced Topics**

1. **String Joiner**: Strings ko join karne ke liye.
    
    ```java
    import java.util.StringJoiner;
    
    StringJoiner sj = new StringJoiner(", ");
    sj.add("Java").add("Python").add("C++");
    System.out.println(sj); // Output: Java, Python, C++
    ```
    
2. **String Format**: Formatted strings create karna.
    
    ```java
    String s = String.format("Name: %s, Age: %d", "Ali", 25);
    System.out.println(s); // Output: Name: Ali, Age: 25
    ```
    
3. **[[StringBuilder]] vs [[StringBuffer]]**:
    
    - `StringBuilder` fast hai but thread-safe nahi hai.
    - `StringBuffer` slow hai but thread-safe hai.

---

Yeh tha Java Strings ka ek detailed revision! Agar kisi point mein doubt ho ya code ka example chahiye, to bata de.