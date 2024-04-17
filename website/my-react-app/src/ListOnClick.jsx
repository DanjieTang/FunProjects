export default function ListClick() {
    let myArray = ["Apple", "Orange", "Banana"]
    function myFun(index) {
        console.log(index)
    }

    return (
        <div>
            {myArray.map((item, index) => <li key={index} onClick={() => myFun(index)}>{item}</li>)}
        </div>
    );
}