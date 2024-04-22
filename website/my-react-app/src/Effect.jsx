import React, { useState, useEffect } from "react";

export default function Effect() {
    const [counter, setCounter] = useState(0);

    function changeTitle() {
        document.title = `Counter: ${counter}`
    }

    function lmao() {
        console.log("Lmao")
    }

    useEffect(changeTitle, [counter]);
    useEffect(lmao);

    function increment() {
        setCounter(c => c + 1);
    }

    return (<>
        <h1>The counter is at {counter}</h1>
        <button onClick={increment}>Add</button>
    </>);
}