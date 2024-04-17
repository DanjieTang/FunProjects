function lmao() {
    console.log("Lmao")
}

let counter = 0;

function myFun(event) {
    console.log(event)
}

export default function Button() {
    return <button onClick={myFun}>Click me</button>
}