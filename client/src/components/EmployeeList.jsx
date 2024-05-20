import { useEffect, useState } from "react"
import getAllEmployees from '../api/employee.api.js'

export function EmployeeList() {

const [ employees, setEmployees] = useState([])

useEffect(()=> {
 async  function loadEmployees() {
     const res = await getAllEmployees()
     console.log(res);
     setEmployees(res.data);
    }
    loadEmployees() 
}, []);

  return <div>
    {employees.map(employee => (
        <div>
            <h3>Employee: {employee.name} CC: {employee.identification}</h3>
        </div>
    ))}
  </div>
}

export default EmployeeList