interface Individual {
    firstName: string,
    lastName: string,
    company: string
}

const complexJSON: Individual[] = [
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
]

const firstNameArray: string[] = complexJSON.map((value: Individual, index: number) => value.firstName)

console.log(firstNameArray);