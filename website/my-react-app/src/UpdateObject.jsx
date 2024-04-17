import React, { useState } from "react"

export default function UpdateCar() {
    let [car, setCar] = useState({ year: 2024, manufacture: "Tesla", model: "Y" })

    function setYear(event) {
        setCar(car => ({ ...car, year: event.target.value }));
    }

    function setManufacture(event) {
        setCar(car => ({ ...car, manufacture: event.target.value }));
    }

    function setModel(event) {
        setCar(car => ({ ...car, model: event.target.value }));
    }

    return (
        <div>
            <h1>Your car is: {car.year} {car.manufacture} {car.model}</h1>
            <input onChange={setYear} type="number" value={car.year}></input>
            <input onChange={setManufacture}  value={car.manufacture}></input>
            <input onChange={setModel}  value={car.model}></input>
        </div>
    )
}