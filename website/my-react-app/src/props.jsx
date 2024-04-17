import PropTypes from "prop-types"

export default function Student(props) {
    return (
        <div className="student">
            <p>Name: {props.name}</p>
            <h1>Age: {props.age}</h1>
            <h2>IsStudent: {props.isStudent ? "Yes" : "No"}</h2>
        </div>
    );
}

Student.defaultProps = {
    name: "guest",
    age: 0,
    isStudent: false
}