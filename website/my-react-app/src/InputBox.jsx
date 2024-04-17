import React, { useState } from "react"

export default function InputBox() {
    let [name, setName] = useState("")
    let [comment, setComment] = useState("")

    function myName(event) {
        setName(event.target.value)
        console.log(event.target.value)
    }

    function myComment(event) {
        setComment(event.target.value);
    }

    return (
        <div>
            <input value={name} onChange={myName} type="number"></input>
            <p>{name}</p>
            <textarea value={comment} onChange={myComment} placeholder="Lmao"> hi</textarea>
            <p>{comment}</p>
        </div>
    )
}