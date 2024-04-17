import React, { useState } from "react";

export default function ShoppingList() {
    let [shoppingList, setShoppingList] = useState(["Apple", "Banana"]);
    let [index, setIndex] = useState(0);

    function addElement() {
        let item = document.getElementById("box").value;
        setShoppingList((s) => [...s, item]);
        document.getElementById("box").value = "";
    }

    function removeElement() {
        let newShoppingList = [...shoppingList];
        newShoppingList.splice(index, 1);
        console.log(newShoppingList);
        setShoppingList(newShoppingList);
    }

    function sanityCheck(event) {
        let index = event.target.value;

        if (index > 0) {
            setIndex(index);
        }

        console.log(index);
    }

    return (
        <div className="counter">
            <h1>Shopping List</h1>
            <ol>
                {shoppingList.map((item) => <li key={item}>{item}</li>)}
            </ol>
            <input type="text" placeholder="Enter item here" id="box"></input>
            <button onClick={addElement}>Add</button>
            <br />
            <input type="number" placeholder="Choose index here" id="index" onChange={sanityCheck} value={index}></input>
            <button onClick={removeElement}>Remove</button>
        </div>
    );
}