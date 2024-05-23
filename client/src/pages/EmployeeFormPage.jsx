import { createPerson } from "../api/employee.api"
import {useForm} from 'react-hook-form'
import {useNavigate} from 'react-router-dom'

export function EmployeeFormPage() {

  // desestructuracion para obtener el valor de los inputs
  const {
    register,
    handleSubmit,
    formState: {errors},
  } = useForm();
  
  // redirige a una ruta 
  const navigate = useNavigate()

  // se ejecuta al guardar el form
  const onSubmit = handleSubmit(async (data) => {
    // ejecuta el metodo para crear una persona
    await createPerson(data)
    // redirige despues de crear
    navigate("/employeePage")
    
    
  })

  return (
    <div>
      {/* con onSubmit captura la data de los inputs cuando se da clic en enviar */}
      <form onSubmit={onSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" name="name" placeholder="Name"
          {...register("name", {required: true})} />
        </div>
        {errors.name && <span>The Name is required</span>} 

        <div>
          <label htmlFor="identification">Identification:</label>
          <input type="text" id="identification" name="identification" placeholder="Identification"
           {...register("identification", {required: true})} />
        </div>
        {errors.identification && <span>The identification is required</span>} 

        <div>
          <label htmlFor="id_type_document">Document Type:</label>
          <select id="id_type_document" name="id_type_document"
           {...register("id_type_document", {required: true})}>
            <option value="">Select Document Type</option>
            <option value="1">C.C</option>
            <option value="2">C.E</option>
          </select>
        </div>
        {errors.name && <span>The type of document is required</span>} 

        <div>
          <label htmlFor="state">State:</label>
          <input type="checkbox" id="state" name="state"
          {...register("state", {required:true})} />
        </div>
        {errors.name && <span>The State is required</span>} 

        <div>
          <label htmlFor="id_area">Area:</label>
          <select id="id_area" name="id_area"
           {...register("id_area", {required: true})}>
            <option value="">Select Area</option>
            <option value="1">Area 1</option>
            <option value="2">Area 2</option>
          </select>
        </div>
        {errors.area && <span>The area is required</span>} 

        <div>
          <label htmlFor="id_person_picture">Person Picture:</label>
          <input type="file" id="id_person_picture" name="id_person_picture" accept="image/*" 
           {...register("picture")}/>
        </div>


        <button type="submit">Submit</button>
      </form>

    </div>
  )
}

export default EmployeeFormPage