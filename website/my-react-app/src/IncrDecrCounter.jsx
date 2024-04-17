import React, { useState } from "react"

export default function Counter() {
    const header = <h1 className="same-line">Counter:</h1>
    let [counter, setCounter] = useState(0)
    const number = <h1 className="same-line">{counter}</h1>

    function increase() {
        setCounter(c => c + 1);
    }

    function decrease() {
        setCounter(c => c - 1);
    }

    function zero() {
        setCounter(0);
    }

    const button1 = <button className="button" onClick={decrease}> Decrease </button>
    const button2 = <button className="button" onClick={zero}> Zero </button>
    const button3 = <button className="button" onClick={increase}> Increase </button>
    return (
        <div className="counter">
            <div>
                {header}
                {number}
            </div>
            <div>
                {button1}
                {button2}
                {button3}
            </div>
        </div>
    )
}