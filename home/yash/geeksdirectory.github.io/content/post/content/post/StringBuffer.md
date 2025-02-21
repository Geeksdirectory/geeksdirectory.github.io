---
title: post StringBuffer
date: 2024-12-22
lastmod: 2025-02-21T03:51:33.684Z
---
Bilkul bhai, **StringBuffer** ko bhi simple example aur clear explanation ke saath samjhata hoon. Agar tu StringBuilder samajh gaya hai, to StringBuffer samajhna aur bhi easy ho jayega, kyunki dono kaafi similar hain.

***

### **StringBuffer Kya Hai?**

* **StringBuffer** bhi ek mutable string class hai, jaise **StringBuilder**.
* Iska kaam bhi wahi hai: **Strings ko modify karna bina naye objects create kare**.
* **Farak?** StringBuffer **thread-safe** hota hai, matlab ye multi-threaded environments ke liye secure hai, lekin ye StringBuilder se **thoda slow** hota hai.

***

### **StringBuffer vs StringBuilder**

| Feature           | StringBuffer                  | StringBuilder        |
| ----------------- | ----------------------------- | -------------------- |
| **Thread-Safety** | Thread-safe                   | Not thread-safe      |
| **Performance**   | Slower (due to thread-safety) | Faster               |
| **Usage**         | Multi-threading apps          | Single-threaded apps |

***

### **StringBuffer Example**

#### **Without StringBuffer (Using String)**

Baar-baar string modify karne pe naye objects bante hain, jo memory aur time waste karta hai.

```java
public class WithoutStringBuffer {
    public static void main(String[] args) {
        String s = "Hello";
        s = s + " World";  // Naya object ban raha hai
        s = s + "!";
        System.out.println(s);  // Output: Hello World!
    }
}
```

***

#### **With StringBuffer**

StringBuffer ek hi object ko baar-baar modify karta hai.

```java
public class WithStringBuffer {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");
        sb.append(" World");  // "World" add karega existing object mein
        sb.append("!");
        System.out.println(sb);  // Output: Hello World!
    }
}
```

Yahan **koi naya object nahi bana**, performance better hai.

***

### **Important Methods of StringBuffer**

#### 1. **`append()`**

String ke end mein kuch add karne ke liye.

```java
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");
System.out.println(sb);  // Output: Hello World
```

***

#### 2. **`insert()`**

String ke specific index par kuch insert karne ke liye.

```java
StringBuffer sb = new StringBuffer("Hello World");
sb.insert(6, "Beautiful ");  // Index 6 par "Beautiful " insert karega
System.out.println(sb);  // Output: Hello Beautiful World
```

***

#### 3. **`replace()`**

String ke ek portion ko replace karne ke liye.

```java
StringBuffer sb = new StringBuffer("I love Java");
sb.replace(7, 11, "Python");  // "Java" ko "Python" se replace karega
System.out.println(sb);  // Output: I love Python
```

***

#### 4. **`delete()`**

String ke specific portion ko delete karne ke liye.

```java
StringBuffer sb = new StringBuffer("Hello Beautiful World");
sb.delete(6, 16);  // Index 6 se 15 tak delete karega
System.out.println(sb);  // Output: Hello World
```

***

#### 5. **`reverse()`**

String ko reverse karne ke liye.

```java
StringBuffer sb = new StringBuffer("Java");
sb.reverse();
System.out.println(sb);  // Output: avaJ
```

***

#### 6. **`capacity()`**

StringBuffer ki **capacity** check karne ke liye.

```java
StringBuffer sb = new StringBuffer();
System.out.println(sb.capacity());  // Default capacity: 16

sb.append("Java Programming");
System.out.println(sb.capacity());  // Capacity dynamically grow karegi
```

***

### **Thread-Safety of StringBuffer**

Thread-safety ka matlab hai ki agar ek StringBuffer object ko multiple threads access karte hain, to usme koi data corruption nahi hoga. Java internally **synchronized blocks** use karta hai, jo ensure karta hai ki ek time pe ek hi thread object ko modify kare.

***

### **StringBuffer vs StringBuilder: Example**

Agar tumhare program mein **multi-threading** use ho raha hai, to StringBuffer use karo.

```java
public class ThreadSafeExample {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");
        
        // Thread 1
        new Thread(() -> {
            sb.append(" World");
            System.out.println(sb);
        }).start();
        
        // Thread 2
        new Thread(() -> {
            sb.append("!");
            System.out.println(sb);
        }).start();
    }
}
```

Yahan pe StringBuffer thread-safe hai, isliye threads ke beech koi issue nahi hoga. Agar yahi StringBuilder hota, to **data corruption** ho sakti thi.

***

### **When to Use StringBuffer?**

1. **Multi-threaded Applications**: Agar tumhare program mein multiple threads ek hi string object ke saath kaam karte hain, to **StringBuffer** use karo.
2. **Repeated String Modifications**: Agar string baar-baar modify karni hai aur thread-safety chahiye.

***

### **Summary**

* **StringBuffer** mutable hai, aur multi-threading ke liye safe hai.
* Agar tum single-threaded program likh rahe ho, to **StringBuilder** faster hoga.
* Agar tum immutable strings chahiye (jise modify nahi karna), to **String** use karo.

Agar koi specific doubt ho ya code chahiye, to bata!
