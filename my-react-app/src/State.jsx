import React, {useState} from "react"

function State(){
    const [name, setName] = useState("Guest");

    const updateName = () => {
        setName("Danjie");
    }

    return (
        <div>
            <p>Name: {name}</p>
            <button onClick={updateName}>Set Name</button>
        </div>
    )
}

export default State;