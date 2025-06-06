async function first() {
    console.log("Start first");
    const response: Response = await fetch("http://localhost:8000/api/user");
    const data: string = await response.text();
    console.log("End first")
}

async function second() {
    console.log("Start second");
    const response: Response = await fetch("http://localhost:8000/api/user");
    const data: string = await response.text();
    console.log("End second");
}

function main(){
    first();
    second();
}

main();