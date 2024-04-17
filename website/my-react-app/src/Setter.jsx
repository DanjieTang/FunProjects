import React, { useState } from "react";

export default function Setter() {

    let [age, setAge] = useState(0)

    function changingAge(event) {
        // let inputAge = event.target.value;

        // if (inputAge >= 0) {
        setAge((i) => i + 1);
        // }
        console.log(age)
    }

    return (
        <div>
            <h1>Please enter your age:</h1>
            <input type="number" onChange={changingAge} value={age}></input>
            <h2>Your age is {age}</h2>
        </div>
    );
}