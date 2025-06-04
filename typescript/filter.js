var complexJson = [
    {
        firstName: "Tony",
        lastName: "Stark",
        aka: "Iron Man"
    },
    {
        firstName: "Steve",
        lastName: "Rogers",
        aka: "Captain America"
    },
    {
        firstName: "Peter",
        lastName: "Parker",
        aka: "Spider Man"
    }
];
var shortNamePeopleList = complexJson.filter(function (value) { return value.firstName.length <= 4; });
shortNamePeopleList[0].aka = "Danjie Tang";
console.log(complexJson);
