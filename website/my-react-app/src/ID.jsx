import React, { useState } from "react";

export default function ID() {
    let [name, setName] = useState()

    function changeName() {
        setName(document.getElementById("box").value);
    }

    return (
        <div>
            <h1>Your name is {name}</h1>
            <input type="text" id="box" placeholder="Enter here"></input>
            <br />
            <button onClick={changeName}>Complete</button>
        </div>
    );
}