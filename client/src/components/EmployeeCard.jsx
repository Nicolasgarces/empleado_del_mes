


//recibe la propiedad task en la se obtienen los datos del empleado
export function EmployeeCard({ employee }) {
    return (
        <div>
            <h3>Employee: {employee.name}</h3>
            <p> CC: {employee.identification}</p>
            <p> state: {employee.state}</p>
            <p> Area: {employee.id_area}</p>
            <hr />
        </div>
    )
}

export default EmployeeCard