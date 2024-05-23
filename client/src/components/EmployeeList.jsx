import { useEffect, useState } from "react"
import { getAllPeople } from '../api/employee.api.js'
import EmployeeCard from "./EmployeeCard.jsx";

export function EmployeeList() {

const [ employees, setEmployees] = useState([])

useEffect(()=> {
  //la funcion carga los empleados
 async  function loadEmployees() {
      //llama el metodo para traer los empleados del back
     const res = await getAllPeople()
     console.log(res);
     //guarda los empleados
     setEmployees(res.data);
    }
    loadEmployees() 
}, []);

  return <div>
    {employees.map(employee => (
        <EmployeeCard key={employee.id} employee={employee}/>
    ))}
  </div>
}

export default EmployeeList