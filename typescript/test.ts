interface Person {
    "First Name": string,
    "Last Name": string,
    Age?: number
}

let myFirstObject: Person = {
    "First Name": "Tony",
    "Last Name": "Stark"
};

myFirstObject["First Name"] = "Danjie";
myFirstObject["Last Name"] = "Tang";
myFirstObject["Age"] = 22;

console.log(myFirstObject["First Name"] + " " + myFirstObject["Last Name"] + " " + myFirstObject["Age"])