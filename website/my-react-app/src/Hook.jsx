import React, { useState } from "react";

export default function Hooking() {
    const [name, setName] = useState("Guest")
    const updateName = function () {
        setName("Danjie")
    }

    return (
        <div>
            <p>Name: {name}</p>
            <button onClick={updateName}>Set Name</button>
        </div>
    );
}