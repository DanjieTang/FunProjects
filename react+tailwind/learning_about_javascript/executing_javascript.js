function haha() {
    let a = 10;
    let b = 20;
    return [a, b];
}

let a;
let b;
[a, b] = haha();

console.log(a);
console.log(b);