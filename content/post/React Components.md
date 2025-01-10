---
title: post React Components
date: 2024-12-24
---

[[react components hinglsih]]

### **What Are React Components?**

Think of **React components** as the **==building blocks==** of a React app. Each component is responsible for rendering a specific part of the UI (User Interface).

#### Example:

If your app is like a car:

- The **steering wheel** is a component.
- The **seats** are components.
- The **engine** is another component.

All these components come together to form the **car (your app)**.

---

### **Types of React Components**

React has two main types of components:

1. **Functional Components** (Modern way):
    
    - They are plain JavaScript functions.
    - Lightweight and easier to write.
    - Use ==**Hooks** for managing state and lifecycle==.
    
    ```jsx
    function Welcome() {
        return <h1>Welcome to React!</h1>;
    }
    ```
    
2. **Class Components** (Older way):
    
    - They are JavaScript classes that extend `React.Component`.
    - Used for managing state and lifecycle in older React versions.
    
    ```jsx
    class Welcome extends React.Component {
        render() {
            return <h1>Welcome to React!</h1>;
        }
    }
    ```
    
    Modern React prefers **Functional Components** because they're simpler and more powerful with Hooks.
    

---

### **How to Create a React Component?**

1. **Define a Function/Class**:
    
    - ==Always name the component with a **capital letter** (important for React to recognize it as a component).==
2. **Return JSX**:
    
    - The component must return **JSX**, which is HTML-like code combined with JavaScript.
    
    ```jsx
    function MyComponent() {
        return <div>This is my component!</div>;
    }
    ```
    
3. **Use the Component**:
    
    - Once created, a component can be reused in other components.
    
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

### **Props (Properties) - Passing Data to Components**

If you want to pass data to a component, you use **props** (short for properties).

#### Example:

Passing text to a `Button` component:

```jsx
function Button(props) {
    return <button>{props.text}</button>;
}

function App() {
    return <Button text="Click Me!" />;
}
```

- Here, `text` is a **prop** sent to the `Button` component, and it renders it inside the `<button>` tag.

---

### **State - Managing Dynamic Data**

When a component needs to **store and manage its own data** that can change, you use **state**.

#### Example:

A counter app:

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

- `useState(0)` initializes the state with `0`.
- `count` holds the current state value.
- `setCount` updates the state.

Whenever you click the button, the `setCount` function updates the value of `count`, and React re-renders the UI.

---

### **React Lifecycle (For Class Components)**

If you're using class components, they have lifecycle methods:

1. **Mounting (Component Loads)**:
    
    - `componentDidMount()` is called after the component is rendered.
2. **Updating (Component Updates)**:
    
    - `componentDidUpdate()` is called after the component’s state or props change.
3. **Unmounting (Component is Removed)**:
    
    - `componentWillUnmount()` is called before the component is removed.

For **functional components**, you use the **useEffect Hook** to handle lifecycle events.

#### Example:

A timer that updates every second:

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

### **Parent-Child Relationship in Components**

Components can contain other components, forming a parent-child relationship.

```jsx
function Header() {
    return <h1>Welcome!</h1>;
}

function Footer() {
    return <p>Thanks for visiting.</p>;
}

function App() {
    return (
        <div>
            <Header />
            <Footer />
        </div>
    );
}
```

Here:

- `Header` and `Footer` are **child components** of `App`.

---

### **Advantages of React Components**

1. **Reusability**: Write a component once, reuse it everywhere.
2. **Maintainability**: Break down the UI into smaller, manageable pieces.
3. **Performance**: React only updates the components that need to change.
4. **Testability**: Small, isolated components are easier to test.

---

### **Complete Example**

Here’s a simple app that shows how to pass data (props) and use components:

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

- The `Greeting` component takes a `name` prop and displays it.
- The `App` component uses `Greeting` three times with different names.

---