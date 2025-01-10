---
title: post react components hinglsih
date: 2024-12-24
---

components are reusable

React mein **Components** kya hote hain? Samjho ki React ka kaam hai web app banane ka, aur components us app ke **==building blocks==** hote hain. Har ek component ek **chhoti si chiz** ya ek **kaam** ko handle karta hai.

- **Real-life example**: Ek car le lo.
    - Car ka **steering wheel** ek component hai.
    - **Seats**, ek component hai.
    - **Engine**, ek aur component.
    - Milke ye saare components ek car banate hain.

Similarly, ==React app mein **components milkar pura UI banate hain==**.

---

### **Types of React Components**

React mein do tarah ke components hote hain:

1. **Functional Components**:
    
    - Yeh sirf ek ==JavaScript function== hote hain.
    - Lightweight aur seedhe simple kaam karte hain.
    - Modern React mein yeh zyada use hote hain.
    
    ```jsx
    function HelloWorld() {
        return <h1>Hello, World!</h1>;
    }
    ```
    
2. **Class Components**:
    
    - Yeh JavaScript classes hoti hain (ES6 class syntax ka use karke).
    - ==Purane React mein zyada use== hote the.
    - Lifecycle methods aur state ke liye use hote hain.
    
    ```jsx
    class HelloWorld extends React.Component {
        render() {
            return <h1>Hello, World!</h1>;
        }
    }
    ```
    

**Naya React** functional components aur **==Hooks** pe zyada focus karta hai, toh functional wale ko hi samajhna zyada zaroori hai.==

---

### **React Component Banane ke Steps**

1. **Create a Function/Class**:
    - Function ko banate waqt `function` keyword ya `arrow function` ka use hota hai.
    - Component ka naam hamesha capital letter se shuru hota hai (React ke liye ye important hai).
    - 
1. **Return JSX**:
    - Component ka kaam hota hai **HTML ko render karna**.
    - React mein hum JSX (JavaScript XML) ka use karte hain.
    - JSX = HTML + JavaScript ka combination.
    
    ```jsx
    function MyComponent() {
        return <div>This is my component!</div>;
    }
    ```
    
3. **Use Component in App**:
    
    - Ek baar component ban gaya, toh isko kisi aur component ke andar use kar sakte ho.
    
    ```jsx
    function App() {
        return (
            <div>
                <MyComponent />
            </div>
        );
    }
    ```
    

---

### **Props (Properties) - Component ko Data Do**

Agar tumhe ek component ko data dena ho, toh tum **props** ka use karte ho.

- **Example**: Ek button component ko text dena ho.
    
    ```jsx
    function Button(props) {
        return <button>{props.text}</button>;
    }
    
    function App() {
        return <Button text="Click Me!" />;
    }
    ```
    
- Yahan `text` ek prop hai, jo `Button` component ko mil raha hai.
    

---

### **State - Component ke Andar ka Data**

Agar tumhe ek component ke andar data store karna ho, jo change ho sake, toh tum **state** use karte ho.

- Functional component mein **useState Hook** ka use hota hai.
    
    ```jsx
    import React, { useState } from 'react';
    
    function Counter() {
        const [count, setCount] = useState(0);
    
        return (
            <div>
                <p>Count: {count}</p>
                <button onClick={() => setCount(count + 1)}>Increment</button>
            </div>
        );
    }
    ```
    
- Yahan:
    
    - `count` hai current state.
    - `setCount` function state ko update karne ke liye.
    - `useState(0)` ka matlab hai ki shuru mein state 0 hogi.

---

### **Component Lifecycle (Sirf Class Components ke liye)**

Agar tum purane class components ka use karte ho, toh lifecycle methods zaroori hote hain.

- **Mounting** (jab component load hota hai):
    - `componentDidMount()`
- **Updating** (jab data ya state change hoti hai):
    - `componentDidUpdate()`
- **Unmounting** (jab component hata diya jata hai):
    - `componentWillUnmount()`

Lekin Hooks ke saath lifecycle ko `useEffect` hook se handle karte hain. Example:

```jsx
import React, { useState, useEffect } from 'react';

function Timer() {
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setSeconds((prev) => prev + 1);
        }, 1000);

        return () => clearInterval(interval); // Cleanup
    }, []);

    return <p>Timer: {seconds} seconds</p>;
}
```

---

### **React Component Architecture**

1. **Parent-Child Relationship**:
    
    - Ek component ke andar doosra component ho sakta hai.
    
    ```jsx
    function App() {
        return (
            <div>
                <Header />
                <Footer />
            </div>
        );
    }
    ```
    
2. **Reusability**:
    
    - Ek baar component ban gaya toh usko bar-bar use kar sakte ho.

---

### **React mein Components ke Advantages**

- **Reusable**: Ek baar likho, har jagah use karo.
- **Testable**: Chhoti-chhoti files, asaan testing.
- **Readable**: Code structured aur clean lagta hai.
- **Performance**: Sirf wahi components update hote hain jo zarurat hain (React ka diffing algorithm).

---

### **Practical Example**

Ek basic app banate hain jisme tumhe React components aur props ka use dikhata hoon:

```jsx
function Greeting(props) {
    return <h1>Hello, {props.name}!</h1>;
}

function App() {
    return (
        <div>
            <Greeting name="Amit" />
            <Greeting name="Sita" />
            <Greeting name="John" />
        </div>
    );
}
```

Is example mein:

- **Greeting** component ko ek `name` prop diya ja raha hai.
- Alag-alag naam ke saath woh render ho raha hai.

---

Bhai, agar abhi bhi kuch confusion ho, toh bata! Ek aur step by step samjha dunga ya code likhwa ke karwa dunga! 😎