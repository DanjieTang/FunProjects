import React, { useState } from "react";

export default function ToDoList() {
    let [toDoList, setToDoList] = useState(["Wake up", "Go to work"])

    function addTask() {
        let newTask = document.getElementById("task").value;
        if (newTask.trim() === "") {
            return
        }
        setToDoList(t => [...t, newTask]);
        document.getElementById("task").value = '';
    }

    function deleteTask(index) {
        const updatedTasks = toDoList.filter((_, i) => i !== index)

        setToDoList(updatedTasks)
    }

    function upTask(index) {
        if (index > 0) {
            const updatedTasks = [...toDoList];
            let temp = updatedTasks[index - 1];
            updatedTasks[index - 1] = updatedTasks[index];
            updatedTasks[index] = temp;
            setToDoList(updatedTasks)
        }
    }

    function downTask(index) {
        if (index < toDoList.length - 1) {
            const updatedTasks = [...toDoList];
            let temp = updatedTasks[index + 1];
            updatedTasks[index + 1] = updatedTasks[index];
            updatedTasks[index] = temp;
            setToDoList(updatedTasks)
        }
    }

    let display = <div className="to-do">
        <h1> To Do List: </h1>
        <input type="text" placeholder="Enter a task..." id="task"></input>
        <button className="button" onClick={addTask}> Enter </button>
        {toDoList.map((item, index) => <div className="to-do-item" key={index}> <p>{item}</p> <button className="delete" onClick={() => deleteTask(index)}>Delete</button> <button className="up" onClick={() => upTask(index)}>Up</button> <button className="down" onClick={() => downTask(index)}>Down</button></div>)}
    </div>
    return (display);
}