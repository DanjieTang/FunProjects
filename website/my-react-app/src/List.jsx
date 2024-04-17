export default function List(props) {
    const className = props.className
    let students = props.students

    students = students.map((student_info) => <li>{student_info.name} is {student_info.gender}</li>)

    return (<>
        <h1>{className}</h1>
        <ul>
            {students}
        </ul>
    </>);
}

List.defaultProps = {
    className: "Temp",
    students: []
}