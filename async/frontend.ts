async function fetchWithAwait() {
    console.log("Start fetchWithThen");

    try{
        const response: Response = await fetch("http://localhost:8000/api/user");
        console.log("We've retrieved it")
        const data: string = await response.text();
        console.log(data)
    }catch{
        console.error("Oh no")
    }
    console.log("End fetchWithThen");
}

function main(){
    console.log("This is where everything begins")
    fetchWithAwait();
    console.log("Grinding hard");
}

main();