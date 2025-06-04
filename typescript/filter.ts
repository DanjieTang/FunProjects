interface Person {
    firstName: string,
    lastName: string,
    aka: string
}

const complexJson: Person[] = [
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
]

const shortNamePeopleList: Person[] = complexJson.filter((value: Person) => value.firstName.length <= 4)
shortNamePeopleList[0].aka = "Danjie Tang"

console.log(complexJson);