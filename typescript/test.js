var complexJSON = [
    {
        firstName: "Tony",
        lastName: "Stark",
        company: "Stark Industry"
    },
    {
        firstName: "Steve",
        lastName: "Rogers",
        company: "Government of America"
    }
];
var firstNameArray = complexJSON.map(function (value, index) { return value.firstName; });
console.log(firstNameArray);
